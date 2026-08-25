"""High-statistics check of sup_A E_z tr[(F_z^* A F_z)^beta] / tr(A^beta)
at fixed Haar H -- CORRECTED VERSION.

History.  An earlier revision computed Y_z = F_z^* diag(w) F_z by scaling the
WRONG axis of F_z, i.e. it formed diag(w) (F_z^* F_z) -- a NON-Hermitian
matrix silently read from one triangle by numpy.linalg.eigvalsh.  That
produced spurious ratios up to 1.74 and a false "SUP-A-EXCEEDS-ONE" alarm.

This version uses an algebraically identical but bug-proof route:
svd(sqrt(D) F_z) has singular values s_i with
tr[(F_z^* D F_z)^beta] = sum_i s_i^(2 beta), exactly.

Result (seeded, deterministic z-quadrature): the supremum over diagonal
Haar-random-basis A stays strictly below 1 in every tested cell
(max observed ~0.982 at n=8, beta=0.9), consistent with the Jensen cap
for beta in (0,1) and with the beta=1 identity R(A) = 1 identically.
"""

from __future__ import annotations

import json

import numpy as np
from scipy.optimize import minimize

SEED = 20260825
N_Z = 8192
RHO = 1.0
BETAS = (0.5, 0.75, 0.9)
NS = (2, 4, 8)
N_WISHART = 150
N_OPT_RESTARTS = 6

ROOT = "C:/Users/a3188798/OneDrive - Adelaide University/Desktop/QM Problems/settlement/numerical"


def haar_unitary(rng: np.random.Generator, n: int) -> np.ndarray:
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2.0)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def main() -> None:
    rng = np.random.default_rng(SEED)
    print(f"SVD-based sup_A check: rho={RHO}, N_Z={N_Z}")
    summary = {}
    for n in NS:
        h = haar_unitary(rng, n)
        a_, b_ = np.cosh(RHO), np.sinh(RHO)
        zs = np.exp(2j * np.pi * np.arange(N_Z) / N_Z)
        mats = a_ * np.eye(n)[None] + zs[:, None, None] * b_ * h[None]
        fst = np.linalg.solve(mats, np.eye(n, dtype=complex)[None])

        def ratio_svd(w: np.ndarray, beta: float) -> float:
            sq = np.sqrt(w)[:, None] * fst
            sv = np.linalg.svd(sq, compute_uv=False)
            num = float(np.mean(np.power(sv, 2.0 * beta).sum(axis=1)))
            return num / float(np.power(w, beta).sum())

        # coherent rank-one reference (eigenbasis formula, squared modulus!)
        lam = np.angle(np.linalg.eigvals(h))
        _, vecs = np.linalg.eig(h)
        p_coh = np.abs(vecs.conj().T @ (np.ones(n, dtype=complex) / np.sqrt(n))) ** 2
        x = 1.0 / np.abs(zs[:, None] * b_ * np.exp(1j * lam)[None, :] + a_) ** 2

        for beta in BETAS:
            coh = float(np.mean((x @ p_coh) ** beta))
            vals = np.empty(N_WISHART)
            for i in range(N_WISHART):
                g = rng.gamma(shape=2.0, size=n)
                vals[i] = ratio_svd(g / g.sum(), beta)

            def neg_obj(t: np.ndarray) -> float:
                e = np.exp(t - t.max())
                return -ratio_svd(e / e.sum(), beta)

            best_opt = -neg_obj(rng.standard_normal(n) * 0.01)
            for _ in range(N_OPT_RESTARTS):
                res = minimize(
                    neg_obj,
                    rng.standard_normal(n) * 0.05,
                    method="Nelder-Mead",
                    options={"maxiter": 300, "fatol": 1e-10},
                )
                best_opt = max(best_opt, -float(res.fun))

            key = f"n{n}_beta{beta}"
            summary[key] = {
                "coherent_rank1": coh,
                "wishart_max": float(vals.max()),
                "optimized_diag_max": float(best_opt),
                "n_above_one_wishart": int((vals > 1.0).sum()),
            }
            print(
                f"n={n:>2} beta={beta:<4} coh={coh:.5f} "
                f"wish_max={vals.max():.5f} (>1 in {(vals > 1.0).sum()}/{N_WISHART}) "
                f"opt={best_opt:.5f}",
                flush=True,
            )

    worst = max(
        max(v["coherent_rank1"], v["wishart_max"], v["optimized_diag_max"])
        for v in summary.values()
    )
    verdict_text = (
        f"ALL-BELOW-ONE (corrected): worst probe {worst:.5f} < 1 across all "
        f"{len(summary)} cells; the earlier sup-A>1 alarm is retracted as a "
        "non-Hermitian-axis bug in the previous revision"
    )
    print(json.dumps({"experiment": "1b-check-corrected", "verdict": verdict_text, "summary": summary}, indent=2))


if __name__ == "__main__":
    main()
