"""Full-modal stress test for a barrier-assisted composite scalar converter.

The calculation is deliberately diagnostic rather than asymptotic evidence.  It
compares an X/Z pulse sequence in its ideal compressed two-state model with the
same scalar masks acting on a spherical-harmonic Galerkin space.  The Galerkin
space contains every degree ``n <= 4 ell`` with azimuthal number a multiple of
``ell``; this is the sector reached by the four X pulses in the recorded
seven-pulse sequence.

The barrier is a smooth zonal equatorial belt, normalized so that its compressed
block on span{e0,h_ell} is diag(0,1).  The X mask is h_ell/||h_ell||_infinity.
Neither Galerkin success nor failure proves anything about the full converter.
The point is to expose the complementary modes hidden by the 2x2 compression.
"""

from __future__ import annotations

import argparse
import json

import numpy as np
from scipy.linalg import eigh
from scipy.optimize import minimize
from scipy.special import roots_legendre, sph_harm_y


RECORDED_ANGLES = np.array(
    [
        0.8455686265,
        0.8459271868,
        -4.6990459265,
        -2.1055526944,
        3.5935879051,
        -0.2570435312,
        -5.8714438527,
    ]
)


def compressed_fidelities(angles: np.ndarray, samples: np.ndarray) -> np.ndarray:
    """Fidelities for alternating X, Z, ..., X rotations."""

    values = []
    for s in samples:
        state = np.array([1.0 + 0.0j, 0.0j])
        for j, angle in enumerate(angles):
            scaled = s * angle
            if j % 2 == 0:
                cosine = np.cos(scaled)
                sine = -1.0j * np.sin(scaled)
                state = np.array(
                    [
                        cosine * state[0] + sine * state[1],
                        sine * state[0] + cosine * state[1],
                    ]
                )
            else:
                state[1] *= np.exp(-1.0j * scaled)
        values.append(float(abs(state[1]) ** 2))
    return np.asarray(values)


class SphereCompositeModel:
    def __init__(
        self,
        ell: int,
        mu: float,
        belt_exponent: float,
        quadrature_order: int | None = None,
    ) -> None:
        if ell % 2:
            raise ValueError("This diagnostic uses an even ell for a real cosine beam.")
        self.ell = ell
        self.mu = mu
        self.max_degree = 4 * ell
        self.basis = [
            (degree, order)
            for order in range(-4 * ell, 4 * ell + 1, ell)
            for degree in range(abs(order), self.max_degree + 1)
        ]
        dimension = len(self.basis)
        order = quadrature_order or max(120, 2 * self.max_degree + 30)
        x, weights = roots_legendre(order)
        theta = np.arccos(x)
        harmonics = np.column_stack(
            [sph_harm_y(n, m, theta, 0.0) for n, m in self.basis]
        )

        highest = sph_harm_y(ell, ell, theta, 0.0)
        h_axis = np.sqrt(2.0) * highest.real
        maximum = float(
            np.sqrt(2.0) * sph_harm_y(ell, ell, np.pi / 2.0, 0.0).real
        )
        self.beta = float(1.0 / (np.sqrt(4.0 * np.pi) * maximum))

        width = ell ** (-belt_exponent)
        cutoff = np.exp(-((np.abs(x) / width) ** 8))
        mean = float(0.5 * np.dot(weights, cutoff))
        high_mean = float(np.pi * np.dot(weights, cutoff * h_axis**2))
        belt = (cutoff - mean) / (high_mean - mean)

        belt_matrix = np.zeros((dimension, dimension), dtype=np.complex128)
        mixer_matrix = np.zeros_like(belt_matrix)
        orders = range(-4 * ell, 4 * ell + 1, ell)
        groups = {
            m: np.array(
                [j for j, (_, order_j) in enumerate(self.basis) if order_j == m]
            )
            for m in orders
        }
        for m, rows in groups.items():
            y_rows = harmonics[:, rows]
            belt_matrix[np.ix_(rows, rows)] = 2.0 * np.pi * (
                y_rows.conj().T @ ((weights * belt)[:, None] * y_rows)
            )
            for adjacent in (m - ell, m + ell):
                if adjacent not in groups:
                    continue
                columns = groups[adjacent]
                y_columns = harmonics[:, columns]
                mixer_matrix[np.ix_(rows, columns)] = np.pi * (
                    y_rows.conj().T
                    @ ((weights * h_axis / maximum)[:, None] * y_columns)
                )

        self.belt = 0.5 * (belt_matrix + belt_matrix.conj().T)
        self.mixer = 0.5 * (mixer_matrix + mixer_matrix.conj().T)
        self.free = np.diag(
            [n * (n + 1) / ell**2 for n, _ in self.basis]
        ).astype(np.complex128)
        self.centrifugal_gap = float(ell * (ell + 1) / ell**2)
        self.base = self.free - self.centrifugal_gap * self.belt

        self.constant = np.zeros(dimension, dtype=np.complex128)
        self.constant[self.basis.index((0, 0))] = 1.0
        self.target = np.zeros_like(self.constant)
        self.target[self.basis.index((ell, ell))] = 1.0 / np.sqrt(2.0)
        self.target[self.basis.index((ell, -ell))] = 1.0 / np.sqrt(2.0)

        self.belt_cost_density = float(
            np.vdot(self.belt @ self.constant, self.belt @ self.constant).real
        )
        self.mixer_cost_density = float(
            np.vdot(self.mixer @ self.constant, self.mixer @ self.constant).real
        )
        self.base_constant_residual = self._complement_residual(
            self.base @ self.constant
        )
        self.base_target_residual = self._complement_residual(self.base @ self.target)
        self.width = float(width)
        self.belt_mean = mean
        self.belt_high_mean = high_mean
        self._diagonalizations = self._diagonalize_pulses()

    def _complement_residual(self, vector: np.ndarray) -> float:
        vector = vector.copy()
        vector -= self.constant * np.vdot(self.constant, vector)
        vector -= self.target * np.vdot(self.target, vector)
        return float(np.linalg.norm(vector))

    def _diagonalize_pulses(self) -> dict[tuple[str, int], tuple[np.ndarray, np.ndarray]]:
        result = {}
        for pulse_type in ("X", "Z"):
            for sign in (-1, 1):
                if pulse_type == "X":
                    hamiltonian = (
                        self.base + sign * (self.mu / self.beta) * self.mixer
                    )
                else:
                    hamiltonian = self.free + (
                        -self.centrifugal_gap + sign * self.mu
                    ) * self.belt
                result[(pulse_type, sign)] = eigh(hamiltonian)
        return result

    def _apply_pulse(
        self, state: np.ndarray, pulse_type: str, angle: float, s: float
    ) -> np.ndarray:
        sign = 1 if angle >= 0 else -1
        eigenvalues, eigenvectors = self._diagonalizations[(pulse_type, sign)]
        duration = abs(angle) / self.mu
        coefficients = eigenvectors.conj().T @ state
        coefficients *= np.exp(-1.0j * s * duration * eigenvalues)
        return eigenvectors @ coefficients

    def fidelities(self, angles: np.ndarray, samples: np.ndarray) -> np.ndarray:
        values = []
        for s in samples:
            state = self.constant.copy()
            for j, angle in enumerate(angles):
                pulse_type = "X" if j % 2 == 0 else "Z"
                state = self._apply_pulse(state, pulse_type, float(angle), float(s))
            values.append(float(abs(np.vdot(self.target, state)) ** 2))
        return np.asarray(values)

    def charged_cost(self, angles: np.ndarray) -> float:
        total = 0.0
        for j, angle in enumerate(angles):
            sign = 1 if angle >= 0 else -1
            duration = abs(float(angle)) / self.mu
            if j % 2 == 0:
                coefficient = self.mu / self.beta
                density = (
                    self.centrifugal_gap**2 * self.belt_cost_density
                    + coefficient**2 * self.mixer_cost_density
                )
            else:
                coefficient = -self.centrifugal_gap + sign * self.mu
                density = coefficient**2 * self.belt_cost_density
            total += duration * density
        return float(total)


def summarize(values: np.ndarray) -> dict[str, float]:
    return {
        "minimum": float(values.min()),
        "mean": float(values.mean()),
        "maximum": float(values.max()),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ell", type=int, default=8)
    parser.add_argument("--s-min", type=float, default=0.9)
    parser.add_argument("--s-max", type=float, default=1.1)
    parser.add_argument("--samples", type=int, default=41)
    parser.add_argument("--mu", type=float, default=0.12)
    parser.add_argument("--belt-exponent", type=float, default=0.35)
    parser.add_argument("--optimize-full", action="store_true")
    parser.add_argument("--maxiter", type=int, default=1500)
    args = parser.parse_args()

    samples = np.linspace(args.s_min, args.s_max, args.samples)
    model = SphereCompositeModel(
        ell=args.ell,
        mu=args.mu,
        belt_exponent=args.belt_exponent,
    )
    angles = RECORDED_ANGLES.copy()
    before = model.fidelities(angles, samples)

    optimization = None
    if args.optimize_full:
        training_samples = np.linspace(args.s_min, args.s_max, 7)

        def objective(candidate: np.ndarray) -> float:
            fidelity = model.fidelities(candidate, training_samples)
            return float(
                np.mean((1.0 - fidelity) ** 2)
                + 0.05 * (1.0 - fidelity.mean())
            )

        result = minimize(
            objective,
            angles,
            method="Nelder-Mead",
            options={
                "maxiter": args.maxiter,
                "xatol": 1.0e-8,
                "fatol": 1.0e-11,
            },
        )
        angles = result.x
        optimization = {
            "success": bool(result.success),
            "iterations": int(result.nit),
            "objective": float(result.fun),
        }

    after = model.fidelities(angles, samples)
    compressed = compressed_fidelities(RECORDED_ANGLES, samples)
    output = {
        "ell": args.ell,
        "dimension": len(model.basis),
        "s_interval": [args.s_min, args.s_max],
        "mu": args.mu,
        "belt_width": model.width,
        "beta": model.beta,
        "base_constant_residual": model.base_constant_residual,
        "base_target_residual": model.base_target_residual,
        "compressed_recorded_sequence": summarize(compressed),
        "full_recorded_sequence": summarize(before),
        "full_final_sequence": summarize(after),
        "charged_cost_final_sequence": model.charged_cost(angles),
        "angles_final": angles.tolist(),
        "optimization": optimization,
        "status": (
            "finite Galerkin diagnostic only; neither success nor failure is "
            "asymptotic evidence for the full scalar converter"
        ),
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
