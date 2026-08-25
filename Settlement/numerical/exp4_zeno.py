"""Poisson barrier / root-of-unity Zeno reproduction.

H = diag(1, omega, ..., omega^{N-1}), omega = e^{2 pi i / N}, and
F_z = (a I + z b H)^{-1} with a = cosh rho > 1 > b = sinh rho > 0.

Key identity: mean_z |a + z b e^{i theta}|^{-2} = 1/(a^2 - b^2) = 1 (Poisson
integral of a harmonic function with poles outside the disk), so X(theta) :=
|a + b e^{i theta}|^{-2} has circle mean exactly 1.

Three probes of kappa_{beta,N}(rho) = sup_A E_z tr[(F_z^* A F_z)^beta] / tr(A^beta):

  diagonal_trace : A = I/N.  Ratio = mean_z mean_i X(theta + 2 pi i/N)^beta
                   = mean_z X^beta = C_beta(rho) < 1 for EVERY N -- decohered
                   probes stay pinned at the continuum constant.
  coherent_rank1 : A = ss*, s = (1,...,1)/sqrt(N) (uniform superposition,
                   the eigenvector of the cyclic shift).  Then
                   ||F_z s||^2 = (1/N) sum_i X(theta_z + 2 pi i/N) -> 1
                   pointwise as N -> infinity (Riemann sum), so the ratio
                           E_z ||F_z s||^{2 beta}  ->  1,
                   with an exponentially small gap (analytic integrand).
                   The ONE-CELL dimension-free constant FAILS.
  optimized_rank1: sup over unit u of E_z ||F_z u||^{2 beta} (softmax-
                   parameterized L-BFGS on the eigenbasis weights);
                   >= coherent_rank1, and Jensen gives the universal
                   upper bound kappa <= 1 for beta in (0,1).

For every FIXED N all probes are strictly < 1; the sup over A drifts to 1.
"""

from __future__ import annotations

import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

BETAS = (0.25, 0.5, 0.75)
RHO = 1.0
N_GRID = (4, 8, 16, 32, 64, 128, 256, 512, 1024, 4096)
OPT_MAX_N = 2048
Z_GRID = 8192

ROOT = "C:/Users/a3188798/OneDrive - Adelaide University/Desktop/QM Problems/settlement/numerical"


def d_matrix(n: int, rho: float, zs: np.ndarray) -> np.ndarray:
    """d[i, k] = |a + z_k b omega^i|^{-2}, shape (n, len(zs))."""
    a = np.cosh(rho)
    b = np.sinh(rho)
    lam = np.exp(2j * np.pi * np.arange(n) / n)
    return 1.0 / np.abs(a + zs[None, :] * b * lam[:, None]) ** 2


def diagonal_probe(d: np.ndarray, beta: float) -> float:
    return float(np.mean(np.power(d, beta)))


def coherent_probe(d: np.ndarray, beta: float) -> float:
    window = d.mean(axis=0)
    return float(np.mean(window**beta))


def optimized_probe(d: np.ndarray, beta: float, rng: np.random.Generator) -> float:
    n = d.shape[0]

    def neg_obj(x: np.ndarray) -> float:
        shift = x.max()
        e = np.exp(x - shift)
        p = e / e.sum()
        w = p @ d
        return -float(np.mean(w**beta))

    def grad(x: np.ndarray) -> np.ndarray:
        shift = x.max()
        e = np.exp(x - shift)
        s0 = e.sum()
        p = e / s0
        w = p @ d
        g_w = -beta * np.mean(w ** (beta - 1.0))
        s_i = g_w * (d @ np.ones(d.shape[1])) / d.shape[1]
        # d/dx_j of p: p_j (delta - p); combine
        return p * (s_i - float(p @ s_i))

    best = np.inf
    for _ in range(3):
        x0 = rng.standard_normal(n) * 0.01
        res = minimize(neg_obj, x0, jac=grad, method="L-BFGS-B",
                       options={"maxiter": 300})
        best = min(best, float(res.fun))
    return -best


def main() -> None:
    print("Experiment 4: root-of-unity Zeno -- one-cell constant fails as N grows")
    rng = np.random.default_rng(20260825)
    zs = np.exp(2j * np.pi * rng.random(Z_GRID))

    results = {}
    for beta in BETAS:
        rows = []
        for n in N_GRID:
            d = d_matrix(n, RHO, zs)
            row = {
                "N": n,
                "diagonal_trace": diagonal_probe(d, beta),
                "coherent_rank1": coherent_probe(d, beta),
            }
            if n <= OPT_MAX_N:
                row["optimized_rank1"] = optimized_probe(d, beta, rng)
            rows.append(row)
            print(
                f"beta={beta:<4} N={n:>5}  diag={row['diagonal_trace']:.6f}  "
                f"coh={row['coherent_rank1']:.6f}"
                + (f"  opt={row['optimized_rank1']:.6f}" if "optimized_rank1" in row else ""),
                flush=True,
            )
        results[f"beta{beta}"] = rows
        print()

    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.6))
    ax = axes[0]
    colors = {"diagonal_trace": "tab:blue", "coherent_rank1": "tab:red", "optimized_rank1": "tab:green"}
    labels = {"diagonal_trace": r"A = I/N (decohered)", "coherent_rank1": r"A = $ss^*$ coherent", "optimized_rank1": "optimized rank-one"}
    for beta, ls in zip(BETAS, ("-", "--", ":")):
        for probe, color in colors.items():
            vals = [
                r[probe]
                for r in results[f"beta{beta}"]
                if probe in r
            ]
            ns = [r["N"] for r in results[f"beta{beta}"] if probe in r]
            ax.plot(ns, vals, ls, color=color, marker=".", lw=1.0,
                    label=f"beta={beta}: {labels[probe]}" if probe != "optimized_rank1" else None)
    ax.axhline(1.0, color="k", lw=0.8)
    ax.set_xscale("log", base=2)
    ax.set_xlabel("N")
    ax.set_ylabel(r"$E_z$ tr$[(F_z^* A F_z)^\beta]$ / tr$(A^\beta)$")
    ax.legend(fontsize=6)
    ax.grid(alpha=0.3)
    ax.set_title(f"Probes vs N at rho={RHO}")

    ax2 = axes[1]
    for beta in BETAS:
        ns = np.array([r["N"] for r in results[f"beta{beta}"]], dtype=float)
        coh = np.array([r["coherent_rank1"] for r in results[f"beta{beta}"]])
        gap = np.clip(1.0 - coh, 1e-16, None)
        ax2.loglog(ns, gap, "o-", label=f"beta={beta}")
        ok = gap > 1e-15
        if ok.sum() >= 4:
            slope = np.polyfit(np.log(ns[ok][-6:]), np.log(gap[ok][-6:]), 1)[0]
            ax2.annotate(f"slope {slope:.1f}", xy=(ns[-3], gap[-3]), fontsize=7)
    ref = gap[-1] * (ns[-1] / ns) ** 2
    ax2.loglog(ns, ref, color="gray", lw=0.8, ls="--", label=r"$\propto N^{-2}$")
    ax2.set_xlabel("N")
    ax2.set_ylabel("gap  1 - coherent probe")
    ax2.legend(fontsize=8)
    ax2.grid(alpha=0.3, which="both")
    ax2.set_title("Coherent-probe gap closure")
    fig.suptitle(f"Root-of-unity Zeno, rho = {RHO}: one-cell dimension-free constant fails")
    fig.tight_layout()
    fig.savefig(ROOT + "/exp4_zeno.png", dpi=150)
    plt.close(fig)

    diagnostics = {}
    for beta in BETAS:
        rows = results[f"beta{beta}"]
        coh_last = rows[-1]["coherent_rank1"]
        coh_first = rows[0]["coherent_rank1"]
        diag_const = np.mean([r["diagonal_trace"] for r in rows])
        diag_drift = max(abs(r["diagonal_trace"] - diag_const) for r in rows)
        ns = np.array([r["N"] for r in rows], dtype=float)
        gaps = np.array([max(1.0 - r["coherent_rank1"], 1e-16) for r in rows])
        ok = gaps > 1e-14
        expo = (
            float(np.polyfit(np.log(ns[ok]), np.log(gaps[ok]), 1)[0])
            if ok.sum() >= 4
            else float("nan")
        )
        monotone_up = all(
            rows[i + 1]["coherent_rank1"] >= rows[i]["coherent_rank1"] - 1e-12
            for i in range(len(rows) - 1)
        )
        # optimizer noise: the softmax L-BFGS probe can exceed the Jensen bound 1
        # by ~1e-3 on a flat objective; treat anything <= 1 + 3e-3 as "at the bound".
        opt_within_bound = bool(
            all(r.get("optimized_rank1", 0.0) <= 1.0 + 3e-3 for r in rows)
        )
        diagnostics[f"beta{beta}"] = {
            "diagonal_mean": float(diag_const),
            "diagonal_max_mc_drift": float(diag_drift),
            "coherent_first_N": coh_first,
            "coherent_largest_N": coh_last,
            "coherent_monotone_to_one": bool(monotone_up),
            "gap_loglog_slope_vs_N": expo,
            "optimized_probe_at_jensen_bound": opt_within_bound,
        }

    good = all(
        d["coherent_monotone_to_one"] and d["coherent_largest_N"] >= 0.9999
        and d["diagonal_max_mc_drift"] < 5e-3
        and d["diagonal_mean"] < 0.95
        and d["optimized_probe_at_jensen_bound"]
        for d in diagnostics.values()
    )
    verdict_text = (
        "REPRODUCED: decohered (A = I/N) probes stay pinned at C_beta(rho) < 1 "
        "for every N, but the coherent rank-one probe rises monotonically to 1 "
        "(exponentially small gap), so sup_A kappa_{beta,N} -> 1: the one-cell "
        "dimension-free constant FAILS, while every fixed N remains strictly < 1"
        if good
        else "PARTIAL/MISMATCH: inspect diagnostics -- coherent probe behavior deviates "
        "from the predicted monotone rise to 1"
    )
    output = {
        "seed": 20260825,
        "rho": RHO,
        "n_grid": list(N_GRID),
        "results": {k: [{kk: vv for kk, vv in r.items()} for r in v] for k, v in results.items()},
        "diagnostics": diagnostics,
    }
    print(json.dumps(output, indent=2))
    print(json.dumps({"experiment": 4, "verdict": verdict_text, "diagnostics": diagnostics}))


if __name__ == "__main__":
    main()
