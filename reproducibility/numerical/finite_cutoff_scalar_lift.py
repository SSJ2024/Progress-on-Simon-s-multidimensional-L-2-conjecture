"""Numerical rank/conditioning test for a cutoff-edge scalar two-state lift.

The real spherical-harmonic cutoff is degrees <= L.  The selected high state
is the real highest-weight harmonic h_L.  Low-degree coefficients of a real
scalar multiplier v are fixed by the requested e0-column.  Coefficients of v
in degrees L+1,...,2L are then used to cancel every unwanted component of
P_L(v h_L).  This script measures the rank and minimum-L2-norm solution.

This is a diagnostic, not a proof: Gaunt coefficients are evaluated by
high-order product quadrature and the reported singular values are numerical.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.special import sph_harm_y


@dataclass(frozen=True)
class Mode:
    ell: int
    m: int
    kind: str  # "z" for m=0, "c" for cosine, "s" for sine


def modes(lo: int, hi: int) -> list[Mode]:
    out: list[Mode] = []
    for ell in range(lo, hi + 1):
        out.append(Mode(ell, 0, "z"))
        for m in range(1, ell + 1):
            out.append(Mode(ell, m, "c"))
            out.append(Mode(ell, m, "s"))
    return out


def eval_real_modes(ms: list[Mode], theta: np.ndarray, phi: np.ndarray) -> np.ndarray:
    vals = np.empty((len(ms), theta.size), dtype=np.float64)
    for j, mode in enumerate(ms):
        y = sph_harm_y(mode.ell, mode.m, theta, phi)
        if mode.kind == "z":
            vals[j] = y.real
        elif mode.kind == "c":
            vals[j] = np.sqrt(2.0) * y.real
        else:
            vals[j] = np.sqrt(2.0) * y.imag
    return vals


def quadrature(L: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    # Triple products have degree <= 4L in the polynomial/azimuthal variables.
    n_theta = 4 * L + 12
    n_phi = 8 * L + 17
    x, wx = np.polynomial.legendre.leggauss(n_theta)
    theta_1d = np.arccos(x)
    phi_1d = 2.0 * np.pi * np.arange(n_phi) / n_phi
    theta, phi = np.meshgrid(theta_1d, phi_1d, indexing="ij")
    weights = np.repeat(wx, n_phi) * (2.0 * np.pi / n_phi)
    return theta.ravel(), phi.ravel(), weights


def solve_case(
    A: np.ndarray,
    rhs: np.ndarray,
    high: np.ndarray,
    v_low: np.ndarray,
    weights: np.ndarray,
) -> dict[str, float | int]:
    solution, residuals, rank, singular = np.linalg.lstsq(A, rhs, rcond=1e-12)
    residual = np.linalg.norm(A @ solution - rhs)
    rhs_norm = np.linalg.norm(rhs)
    v_grid = v_low + solution @ high
    v_norm = np.sqrt(np.dot(v_low * weights, v_low) + np.dot(solution, solution))
    positive = singular[singular > singular[0] * 1e-12]
    sigma_min = float(positive[-1]) if positive.size else 0.0
    return {
        "rank": int(rank),
        "sigma_max": float(singular[0]),
        "sigma_min_numeric": sigma_min,
        "rhs_norm": float(rhs_norm),
        "residual": float(residual),
        "relative_residual": float(residual / max(rhs_norm, 1e-300)),
        "high_correction_norm": float(np.linalg.norm(solution)),
        "full_multiplier_norm": float(v_norm),
        "sampled_multiplier_sup": float(np.max(np.abs(v_grid))),
        "max_coefficient": float(np.max(np.abs(solution))),
    }


def analyze(L: int) -> dict[str, object]:
    low_modes = modes(0, L)
    high_modes = modes(L + 1, 2 * L)
    theta, phi, weights = quadrature(L)
    low = eval_real_modes(low_modes, theta, phi)
    high = eval_real_modes(high_modes, theta, phi)

    h_index = low_modes.index(Mode(L, L, "c"))
    e_index = low_modes.index(Mode(0, 0, "z"))
    h = low[h_index]

    # A_{j,q} = <Y_j, h Y_q>, q in the high multiplier sector.
    A = (low * (weights * h)[None, :]) @ high.T

    # Case 1: desired off-diagonal block [[0,1],[1,0]].  The fixed low part
    # of the scalar multiplier is sqrt(4*pi) h, since <h,v e0>=1.
    sphere_area = 4.0 * np.pi
    v_low = np.sqrt(sphere_area) * h
    low_vh = (low * weights[None, :]) @ (v_low * h)
    target = np.zeros(len(low_modes))
    target[e_index] = 1.0
    offdiag = solve_case(A, target - low_vh, high, v_low, weights)

    # Case 2: a high-only diagonal block: P_L(v e0)=0 and
    # P_L(v h)=h.  This is the exact finite-cutoff analogue of a barrier.
    v_zero = np.zeros_like(h)
    target_diag = np.zeros(len(low_modes))
    target_diag[h_index] = 1.0
    diagonal = solve_case(A, target_diag, high, v_zero, weights)

    return {
        "L": L,
        "low_dim": len(low_modes),
        "high_dim": len(high_modes),
        "offdiag": offdiag,
        "diagonal": diagonal,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-L", type=int, default=2)
    parser.add_argument("--max-L", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    rows = []
    for L in range(args.min_L, args.max_L + 1):
        row = analyze(L)
        rows.append(row)
        print(json.dumps(row, sort_keys=True))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(rows, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
