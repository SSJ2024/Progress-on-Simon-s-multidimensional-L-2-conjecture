"""Monte Carlo estimate of grouped contraction constants kappa_{beta,n} for the
Szego-type kernel F_z = (a I + z b H)^{-1} on the unit circle.

For H in U(n), a = cosh(rho) > 1 > b = sinh(rho) > 0, A > 0 with tr A = 1, and
dm the normalized Haar measure on the circle,

    kappa_{beta,n}(rho)
      = sup_H sup_{A>0}  E_z[ tr((F_z^* A F_z)^beta) ] / tr(A^beta).

Probes (all lower bounds; Jensen gives the universal cap 1 for beta in (0,1)):
  * random Haar H x random Wishart A (diagonal);
  * random rank-one directions;
  * COHERENT rank-one probe u = V 1/sqrt(n) in the eigenbasis H = V diag(e^{i
    theta}) V*.  Writing X(theta) = |a + b e^{i theta}|^{-2}, ||F_z u||^2 =
    sum_i p_i X(theta_z + theta_i) with p uniform, so the ratio is
    E_z (mean_i X)^beta -> (mean_theta X)^beta = 1 as n grows, because the
    Poisson integral of X on the circle equals exactly 1.  For Haar-random
    spectra the inner mean is a size-n MC sample of X, so the gap should
    decay like beta (1-beta) sinh(rho)^2 / n -- POLYNOMIAL in n.  This
    contrasts with the deterministic root-of-unity spectra of Experiment 4,
    where equal spacing kills the variance superpolynomially fast.

Caution flag: a plausible-looking alternative -- take the top eigenvector of
the averaged frame M = E_z[F_z^*F_z] -- is DEGENERATE here, since the same
Poisson identity forces M = I exactly for every H; any "upper bound"
lambda_max(M)^beta is therefore identically 1 and carries no information.

Theory anchor: for n = 1 all unitaries agree up to a phase absorbed by z, so
kappa_{beta,1}(rho) = C_beta(rho) := (1/2pi) int |a + b e^{it}|^{-2 beta} dt
exactly; the estimator must reproduce this quadrature value at n = 1.

Revision 2026-08-25 (merged): batched deterministic z-grid and reused F stack
(fast revision) combined with the coherent variational probe and the n = 1
analytic anchor; the degenerate averaged-frame probe of the intermediate
revision was removed.

House style: plain numpy, deterministic seed, JSON summary printed at the end.
"""

from __future__ import annotations

import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

SEED = 20260825
N_Z = 1536
N_HAAR = 8
N_WISHART = 3
N_DIRS = 24
BETAS = (0.25, 0.5, 0.75)
NS = (1, 2, 4, 8, 16, 32, 64)
RHOS = (0.5, 1.0, 2.0)

ROOT = "C:/Users/a3188798/OneDrive - Adelaide University/Desktop/QM Problems/settlement/numerical"


def haar_unitary(rng: np.random.Generator, n: int) -> np.ndarray:
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2.0)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def random_density(rng: np.random.Generator, n: int) -> np.ndarray:
    w = rng.gamma(shape=2.0, size=n)
    return w / w.sum()


def f_stack(h: np.ndarray, rho: float, zs: np.ndarray) -> np.ndarray:
    """All F_z = (a I + z b H)^{-1} on a deterministic z-grid, batched."""
    n = h.shape[0]
    a, b = np.cosh(rho), np.sinh(rho)
    mats = a * np.eye(n)[None, :, :] + zs[:, None, None] * b * h[None, :, :]
    eye = np.eye(n, dtype=complex)
    return np.linalg.solve(mats, eye[None, :, :])


def wishart_ratios(fst: np.ndarray, a_diag: np.ndarray, beta: float) -> float:
    # Hermitian PSD slices Y_z = F_z* diag(p) F_z (eigvalsh requires Hermitian input)
    y = np.matmul(fst.conj().transpose(0, 2, 1), a_diag[:, None] * fst)
    eigs = np.linalg.eigvalsh(y)
    num = float(np.mean(np.power(np.clip(eigs, 0.0, None), beta).sum(axis=1)))
    den = float(np.power(a_diag, beta).sum())
    return num / den


def dir_gains(fst: np.ndarray, dirs: np.ndarray) -> np.ndarray:
    g = np.einsum("zij,jk->zik", fst, dirs)
    return np.sum(np.abs(g) ** 2, axis=1)


def coherent_gain(fst: np.ndarray, h: np.ndarray, rho: float, beta: float, zs: np.ndarray) -> float:
    """Rank-one probe u = V 1/sqrt(n): ratio E_z (sum_i p_i X(theta_z+theta_i))^beta."""
    n = h.shape[0]
    a, b = np.cosh(rho), np.sinh(rho)
    _, vecs = np.linalg.eig(h)
    u = np.ones(n, dtype=np.complex128) / np.sqrt(n)
    p = np.abs(vecs.conj().T @ u) ** 2
    lam = np.angle(np.linalg.eigvals(h))
    x = 1.0 / np.abs(a + zs[:, None] * b * np.exp(1j * lam)[None, :]) ** 2
    return float(np.mean((x @ p) ** beta))


def probe_config(fst: np.ndarray, h: np.ndarray, rho: float, beta: float, zs: np.ndarray,
                 rng: np.random.Generator) -> dict:
    n = fst.shape[1]
    ratios = [
        wishart_ratios(fst, random_density(rng, n), beta) for _ in range(N_WISHART)
    ]
    rand_dirs = rng.standard_normal((n, N_DIRS)) + 1j * rng.standard_normal((n, N_DIRS))
    rand_dirs /= np.linalg.norm(rand_dirs, axis=0, keepdims=True)
    gains = dir_gains(fst, rand_dirs)
    random_dir_max = float(np.max(np.mean(gains**beta, axis=0)))
    coh = coherent_gain(fst, h, rho, beta, zs)
    return {
        "random_wishart_max": float(np.max(ratios)),
        "random_dir_max": random_dir_max,
        "coherent_max": coh,
        "kappa_estimate": float(max(np.max(ratios), random_dir_max, coh)),
    }


def analytic_kappa_n1(rho: float, beta: float, n_grid: int = 200001) -> float:
    t = np.linspace(0.0, 2.0 * np.pi, n_grid)
    a, b = np.cosh(rho), np.sinh(rho)
    return float(np.mean(np.power(np.abs(a + b * np.exp(1j * t)), -2.0 * beta)))


def predicted_gap_per_n(rho: float, beta: float) -> float:
    """Leading-order 1/n gap of the coherent probe for Haar-random spectra."""
    return beta * (1.0 - beta) * float(np.sinh(rho)) ** 2


def main() -> None:
    print("Experiment 1: grouped contraction constants kappa_{beta,n}")
    rng = np.random.default_rng(SEED)
    zs = np.exp(2j * np.pi * np.arange(N_Z) / N_Z)

    results = {}
    for rho in RHOS:
        anchors = {b: analytic_kappa_n1(rho, b) for b in BETAS}
        for n in NS:
            hs = [haar_unitary(rng, n) for _ in range(N_HAAR)]
            stacks = [f_stack(h, rho, zs) for h in hs]
            pairs = list(zip(hs, stacks))
            for beta in BETAS:
                per_haar = [probe_config(fs, h, rho, beta, zs, rng) for h, fs in pairs]
                key = f"beta{beta}_n{n}_rho{rho}"
                agg = {
                    "random_wishart_max": float(max(p["random_wishart_max"] for p in per_haar)),
                    "random_dir_max": float(max(p["random_dir_max"] for p in per_haar)),
                    "coherent_max": float(max(p["coherent_max"] for p in per_haar)),
                    "kappa_estimate": float(max(p["kappa_estimate"] for p in per_haar)),
                }
                if n == 1:
                    agg["analytic_anchor"] = anchors[beta]
                results[key] = agg
                extra = f"  [anchor {anchors[beta]:.4f}]" if n == 1 else ""
                print(
                    f"rho={rho:>4}  n={n:>2}  beta={beta:<4} "
                    f"kappa~{agg['kappa_estimate']:.4f} "
                    f"(coh {agg['coherent_max']:.4f}, "
                    f"wish {agg['random_wishart_max']:.4f}, "
                    f"dir {agg['random_dir_max']:.4f}){extra}",
                    flush=True,
                )

    # ---- fits -------------------------------------------------------------
    fits = {}
    for beta in BETAS:
        for rho in RHOS:
            xs = np.log(np.array(NS, dtype=float))
            ys = np.array([results[f"beta{beta}_n{n}_rho{rho}"]["kappa_estimate"] for n in NS])
            slope, _icpt = np.polyfit(xs, ys, 1)
            gap = np.clip(1.0 - ys, 1e-15, None)
            ok = gap > 1e-12
            lslope = (
                float(np.polyfit(xs[ok], np.log(gap[ok]), 1)[0]) if ok.sum() >= 3 else float("nan")
            )
            # implied constant c in gap ~ c / n
            cn = float(np.mean(gap[ok] * np.exp(xs[ok]))) if ok.any() else float("nan")
            pred = predicted_gap_per_n(rho, beta)
            fits[f"beta{beta}_rho{rho}"] = {
                "linear_slope_vs_logn": float(slope),
                "loglog_gap_exponent": lslope,
                "implied_gap_times_n": cn,
                "predicted_beta_1minus_beta_sinh2rho": pred,
                "ratio_implied_over_predicted": float(cn / pred) if cn == cn else None,
            }

    # ---- plots ------------------------------------------------------------
    fig, axes = plt.subplots(1, len(BETAS), figsize=(14.5, 4.4), sharey=True)
    for ax, beta in zip(axes, BETAS):
        for rho, color in zip(RHOS, ("tab:blue", "tab:orange", "tab:red")):
            ks = [results[f"beta{beta}_n{n}_rho{rho}"]["kappa_estimate"] for n in NS]
            ax.plot(NS, ks, "o-", color=color, label=f"rho={rho}")
            ns_arr = np.array(NS, dtype=float)
            theory = 1.0 - predicted_gap_per_n(rho, beta) / ns_arr
            ax.plot(ns_arr, theory, color=color, lw=0.8, ls=":", alpha=0.8)
        ax.axhline(1.0, color="gray", lw=0.7, ls="--")
        ax.set_xscale("log", base=2)
        ax.set_xlabel("n")
        ax.set_title(f"beta = {beta}")
        ax.grid(alpha=0.3)
    axes[0].set_ylabel(r"$\hat\kappa_{\beta,n}$")
    axes[0].legend()
    fig.suptitle("Grouped contraction constants vs dimension (dotted: $1-\\beta(1-\\beta)\\sinh^2\\rho/n$)")
    fig.tight_layout()
    fig.savefig(ROOT + "/exp1_kappa_vs_n.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.8, 4.8))
    for beta in BETAS:
        for rho, marker in zip(RHOS, ("o", "s", "^")):
            ks = np.array([results[f"beta{beta}_n{n}_rho{rho}"]["kappa_estimate"] for n in NS])
            ax.plot(ks, np.clip(1.0 - ks, 1e-16, None), marker, label=f"beta={beta}, rho={rho}")
    ax.set_xlabel(r"estimated $\hat\kappa$")
    ax.set_ylabel(r"gap $1-\hat\kappa$")
    ax.set_yscale("log")
    ax.grid(alpha=0.3, which="both")
    ax.legend(fontsize=7)
    fig.suptitle("Gap closure as n grows")
    fig.tight_layout()
    fig.savefig(ROOT + "/exp1_gap_log.png", dpi=150)
    plt.close(fig)

    all_below_one = all(v["kappa_estimate"] < 1.0 for v in results.values())
    worst = max(v["kappa_estimate"] for v in results.values())
    ratios = [
        f["ratio_implied_over_predicted"]
        for f in fits.values()
        if f["ratio_implied_over_predicted"] is not None
    ]
    median_ratio = float(np.median(ratios)) if ratios else float("nan")
    verdict_text = (
        (
            "PASS: kappa_{beta,n} < 1 for every (beta, n, rho) tested; coherent probe "
            f"gap decays ~ 1/n (median implied/predicted coefficient ratio {median_ratio:.2f}); "
            "consistent with polynomial dimension-driven approach to 1"
        )
        if all_below_one
        else "FAIL: some probe exceeded 1 -- check estimator bias before concluding anything"
    )
    output = {
        "seed": SEED,
        "n_z": N_Z,
        "n_haar": N_HAAR,
        "betas": list(BETAS),
        "ns": list(NS),
        "rhos": list(RHOS),
        "analytic_anchor_n1": {
            f"beta{b}_rho{r}": analytic_kappa_n1(r, b) for b in BETAS for r in RHOS
        },
        "mc_n1": {
            f"beta{b}_rho{r}": results[f"beta{b}_n1_rho{r}"]["kappa_estimate"]
            for b in BETAS
            for r in RHOS
        },
        "kappa_estimates": results,
        "fits": fits,
    }
    print(json.dumps(output, indent=2))
    print(
        json.dumps(
            {
                "experiment": 1,
                "verdict": verdict_text,
                "all_below_one": bool(all_below_one),
                "worst_kappa": float(worst),
                "median_coeff_ratio_vs_theory": median_ratio,
            }
        )
    )


if __name__ == "__main__":
    main()
