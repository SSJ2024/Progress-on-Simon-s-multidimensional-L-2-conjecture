import math
import sys

import numpy as np


def maximal_tensor_basis(ell: int):
    """Matrices for the saturated spin-(2 ell + 1) tensor, up to phases."""
    j1 = ell + 1
    j2 = ell
    J = 2 * ell + 1
    ms_in = list(range(-j2, j2 + 1))
    ms_out = list(range(-j1, j1 + 1))
    mats = []
    for M in range(-J, J + 1):
        mat = np.zeros((2 * j1 + 1, 2 * j2 + 1), dtype=np.complex128)
        for row, mp in enumerate(ms_out):
            for col, m in enumerate(ms_in):
                if mp - m != M:
                    continue
                numerator = (
                    math.comb(2 * j1, j1 + mp)
                    * math.comb(2 * j2, j2 - m)
                )
                denominator = math.comb(2 * J, J + M)
                mat[row, col] = ((-1) ** (j2 - m)) * math.sqrt(
                    numerator / denominator
                )
        mats.append(mat)
    return np.stack(mats)


def objective_and_gradient(q, basis):
    C = np.einsum("k,kij->ij", q, basis)
    gram = C.conj().T @ C
    dim = gram.shape[0]
    scalar = np.trace(gram).real / dim
    residual = gram - scalar * np.eye(dim)
    objective = np.linalg.norm(residual, "fro") ** 2
    gradient = np.empty_like(q)
    for k, Ak in enumerate(basis):
        gradient[k] = 2 * np.trace(Ak.conj().T @ C @ residual)
    gradient -= q * np.real(np.vdot(q, gradient))
    return objective, gradient, np.linalg.eigvalsh(gram)


def search(ell: int, restarts: int = 5, steps: int = 4000):
    basis = maximal_tensor_basis(ell)
    rng = np.random.default_rng(20260723 + ell)
    best = None
    for _ in range(restarts):
        q = rng.normal(size=basis.shape[0]) + 1j * rng.normal(size=basis.shape[0])
        q /= np.linalg.norm(q)
        rate = 0.05
        value, gradient, eigs = objective_and_gradient(q, basis)
        for _ in range(steps):
            proposal = q - rate * gradient
            proposal /= np.linalg.norm(proposal)
            new_value, new_gradient, new_eigs = objective_and_gradient(proposal, basis)
            if new_value <= value:
                q, value, gradient, eigs = (
                    proposal,
                    new_value,
                    new_gradient,
                    new_eigs,
                )
                rate = min(rate * 1.01, 0.2)
            else:
                rate *= 0.5
            if value < 1e-24 or rate < 1e-14:
                break
        if best is None or value < best[0]:
            best = (value, eigs, q)
    value, eigs, q = best
    spread = (eigs.max() - eigs.min()) / eigs.mean()
    print(
        f"ell={ell} dim={2 * ell + 1}->{2 * ell + 3} "
        f"objective={value:.6e} relative_eigen_spread={spread:.6e}"
    , flush=True)
    print("eigenvalues", " ".join(f"{x:.10g}" for x in eigs), flush=True)
    print("q", " ".join(f"{z.real:.8g}{z.imag:+.8g}j" for z in q), flush=True)


if __name__ == "__main__":
    for argument in sys.argv[1:] or ["1", "2", "3"]:
        search(int(argument))
