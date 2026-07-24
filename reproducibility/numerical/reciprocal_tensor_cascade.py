import argparse
import math

import numpy as np


def embed_local(u: np.ndarray, site: int, m: int) -> np.ndarray:
    factors = []
    eye = np.eye(2, dtype=complex)
    for j in range(m):
        factors.append(u if j == site else eye)
    out = factors[0]
    for factor in factors[1:]:
        out = np.kron(out, factor)
    return out


def one_sample(m: int, delta: float, rho: float, angle: float,
               h: np.ndarray, rng: np.random.Generator,
               localized: bool) -> tuple[float, float]:
    dim = 2 ** m
    c, s = math.cos(angle), math.sin(angle)
    u_real = np.array([[c, -s], [s, c]], dtype=complex)
    u = np.diag(np.exp(1j * delta * h)) @ u_real
    a, b = math.cosh(rho), math.sinh(rho)
    jost = np.eye(dim, dtype=complex)
    phases = rng.uniform(0.0, 2.0 * math.pi, size=m)
    for site, phase in enumerate(phases):
        U = embed_local(u, site, m)
        if localized:
            p_local = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
            P = embed_local(p_local, site, m)
            A = np.eye(dim, dtype=complex) + (a - 1.0) * P
            B = b * P
            jost = (
                jost @ U.conj().T @ A
                + np.exp(1j * phase) * jost.conj() @ U.T @ B
            )
        else:
            K = jost @ U.conj().T
            jost = a * K + b * np.exp(1j * phase) * K.conj()
    e0 = np.zeros(dim, dtype=complex)
    e0[0] = 1.0
    x = np.linalg.solve(jost, e0)
    coherence = abs(x.T @ x) / float(np.vdot(x, x).real)
    return -math.log(np.linalg.norm(x)), coherence


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=120)
    parser.add_argument("--max-m", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20260722)
    parser.add_argument("--localized", action="store_true")
    args = parser.parse_args()

    rho = 0.28
    angle = 0.55
    h = np.array([0.7, -0.4])
    deltas = [0.0, 0.02, 0.05, 0.10, 0.20]
    target = math.log(math.cosh(rho))
    print(f"rho={rho:.3f}; tuned one-step lower bound={target:.8f}", flush=True)
    for delta in deltas:
        rng = np.random.default_rng(args.seed + round(1000 * delta))
        print(f"delta={delta:.3f}", flush=True)
        for m in range(1, args.max_m + 1):
            pairs = np.array([
                one_sample(m, delta, rho, angle, h, rng, args.localized)
                for _ in range(args.samples)
            ])
            vals = pairs[:, 0]
            coherences = pairs[:, 1]
            sem = vals.std(ddof=1) / math.sqrt(args.samples)
            print(
                f"  m={m:2d} mean={vals.mean(): .8f} "
                f"per_stage={vals.mean()/m: .8f} sem={sem:.8f} "
                f"coherence={coherences.mean():.8f}",
                flush=True,
            )


if __name__ == "__main__":
    main()
