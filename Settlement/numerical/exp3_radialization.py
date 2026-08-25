"""Short-time radialization feasibility on a truncated S^2 model.

Galerkin space: spherical harmonics with l = 1..L (L = 24) in the m = 1
sector; A_3 = diag(l(l+1)), masks are real symmetric nearest-neighbour
couplings with the exact cos(phi)-type Gaunt matrix elements between l and
l+1, normalized to unit operator norm.

Control model: H(t) = A_3 + u(t) G with piecewise-constant amplitude
|u_j| <= Qmax on segments of duration delta_j.  Words are

    W_s = prod_j exp(-i s delta_j (A_3 + u_j G)),

propagated EXACTLY per segment (eigendecomposition of A_3 + u G cached per
unique amplitude; no Trotter error).  Total time T = sum delta_j.

Task: population transfer |1,1> -> |2,1> uniformly for s in [0.975, 1.025];
error = sup_s (1 - |<2,1|W_s|1,1>|^2), a phase-insensitive surrogate for
sup_s ||W_s - chi(s) U||; target eps = 0.05.

Protocol families compared against the displacement-bound heuristic
T ~ N_gap / Qmax:
  static   : u_j = +Qmax constantly (no carrier);
  carrier  : u_j = Qmax cos(omega t_j), omega swept near the gap -- the
             stroboscopic-resonance ansatz;
  optimized: six-segment sign/level pattern tuned by Nelder-Mead.

Diagnostic only: truncation to L = 24 confines what this says about the full
S^2 compiler.
"""

from __future__ import annotations

import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

SEED = 20260825
L_MAX = 24
M_SECTOR = 1
EPS_TARGET = 0.05
S_SAMPLES = np.linspace(0.975, 1.025, 5)
N_SEGMENTS = 320
QMAX_GRID = (10.0, 100.0, 1000.0)

ROOT = "C:/Users/a3188798/OneDrive - Adelaide University/Desktop/QM Problems/settlement/numerical"


def gaunt_template(ls: np.ndarray, m: int) -> np.ndarray:
    size = ls.size
    g = np.zeros((size, size))
    for r in range(size - 1):
        l = ls[r]
        c = np.sqrt(((l + 1.0) ** 2 - m * m) / ((2.0 * l + 1.0) * (2.0 * l + 3.0)))
        g[r, r + 1] = g[r + 1, r] = c
    return g / np.linalg.norm(g, 2)


class Propagator:
    def __init__(self, eigs: np.ndarray, g: np.ndarray):
        self.eigs = eigs
        self.g = g
        self.cache: dict[float, tuple[np.ndarray, np.ndarray]] = {}
        self.psi0 = np.zeros((S_SAMPLES.size, eigs.size), dtype=np.complex128)
        self.psi0[:, 0] = 1.0

    def _segment(self, u: float):
        key = round(u, 9)
        hit = self.cache.get(key)
        if hit is None:
            lam, q = np.linalg.eigh(np.diag(self.eigs) + u * self.g)
            self.cache[key] = hit = (lam, q)
        return hit

    def leakage(self, us: np.ndarray, deltas: np.ndarray) -> float:
        psi = self.psi0.copy()
        sv = S_SAMPLES[None, :]
        for u_j, d_j in zip(us, deltas):
            lam, q = self._segment(float(u_j))
            phi = q.conj().T @ psi.T
            phi *= np.exp(-1j * d_j * sv * lam[:, None])
            psi = (q @ phi).T
        p_out = np.abs(psi[:, 1]) ** 2
        return float(1.0 - p_out.min())


def static_family(prop: Propagator, qmax: float, totals: np.ndarray):
    best = (np.inf, None)
    us = np.full(N_SEGMENTS, qmax)
    for t in totals:
        err = prop.leakage(us, np.full(N_SEGMENTS, t / N_SEGMENTS))
        if err < best[0]:
            best = (err, float(t))
    return best


def carrier_family(
    prop: Propagator, qmax: float, totals: np.ndarray, omegas: np.ndarray
):
    best = (np.inf, None, None)
    tg = (np.arange(N_SEGMENTS) + 0.5) / N_SEGMENTS
    for omega in omegas:
        for t in totals:
            us = qmax * np.cos(omega * t * tg)
            err = prop.leakage(us, np.full(N_SEGMENTS, t / N_SEGMENTS))
            if err < best[0]:
                best = (err, float(t), float(omega))
    return best


def optimized_family(prop: Propagator, qmax: float, rng: np.random.Generator):
    n_piece = 6

    def objective(x: np.ndarray) -> float:
        us = qmax * np.clip(x[:n_piece], -1.0, 1.0)
        durs = np.abs(x[n_piece:])
        reps = np.maximum(np.round(durs / durs.sum() * N_SEGMENTS).astype(int), 1)
        scale = N_SEGMENTS / reps.sum()
        us_full = np.repeat(us, reps)
        durs_full = np.repeat(durs * scale / N_SEGMENTS, reps)
        return prop.leakage(us_full, durs_full)

    best = (np.inf, None)
    for _ in range(3):
        x0 = np.concatenate(
            [
                rng.choice([-1.0, 1.0], size=n_piece) * rng.random(n_piece),
                rng.uniform(0.02, 1.0, size=n_piece),
            ]
        )
        res = minimize(objective, x0, method="Nelder-Mead",
                       options={"maxiter": 500, "fatol": 1e-8})
        if res.fun < best[0]:
            best = (float(res.fun), res.x)
    err, x = best
    us = qmax * np.clip(x[:n_piece], -1.0, 1.0)
    total_t = float(np.abs(x[n_piece:]).sum())
    return err, total_t


def main() -> None:
    print("Experiment 3: short-time radialization on truncated S^2 model")
    ls = np.arange(max(M_SECTOR, 1), L_MAX + 1).astype(float)
    eigs = ls * (ls + 1.0)
    n_gap = float(eigs[1] - eigs[0])
    g = gaunt_template(ls, M_SECTOR)
    prop = Propagator(eigs, g)
    rng = np.random.default_rng(SEED)
    print(f"sector dim={ls.size}, N_gap={n_gap}, eps_target={EPS_TARGET}", flush=True)

    table: dict[str, dict] = {
        "free_only": {"total_time": 0.0, "error": 1.0,
                      "note": "free evolution preserves populations"}
    }
    totals = np.geomspace(0.02, 60.0, 120)
    omegas = np.linspace(0.4, 1.8, 29) * n_gap

    for qmax in QMAX_GRID:
        err_s, t_s = static_family(prop, qmax, totals)
        err_c, t_c, w_c = carrier_family(prop, qmax, totals, omegas)
        err_o, t_o = optimized_family(prop, qmax, rng)
        table[f"static_Qmax{qmax:.0f}"] = {"total_time": t_s, "error": err_s}
        table[f"carrier_Qmax{qmax:.0f}"] = {
            "total_time": t_c, "error": err_c,
            "omega_over_gap": None if w_c is None else w_c / n_gap,
        }
        table[f"optimized_Qmax{qmax:.0f}"] = {"total_time": t_o, "error": err_o}
        print(
            f"Qmax={qmax:>7}: static err={err_s:.4f} @T={t_s}   "
            f"carrier err={err_c:.4f} @T={t_c} (w/gap={None if w_c is None else round(w_c / n_gap, 3)})   "
            f"optimized err={err_o:.4f} @T={t_o:.3f}",
            flush=True,
        )

    # ---- regime analysis ----------------------------------------------------
    fam = {}
    for family in ("static", "optimized", "carrier"):
        pts = []
        for qmax in QMAX_GRID:
            row = table[f"{family}_Qmax{qmax:.0f}"]
            pts.append({"Qmax": qmax, "time": row["total_time"], "error": row["error"]})
        slopes = []
        for i in range(len(pts) - 1):
            t0, t1 = pts[i]["time"], pts[i + 1]["time"]
            met = pts[i]["error"] <= EPS_TARGET and pts[i + 1]["error"] <= EPS_TARGET
            if met and t0 and t1 and t0 > 0 and t1 > 0:
                slopes.append(np.log(t1 / t0) / np.log(pts[i + 1]["Qmax"] / pts[i]["Qmax"]))
        fam[family] = {
            "points": pts,
            "eps05_met_all": bool(all(p["error"] <= EPS_TARGET for p in pts)),
            "loglog_slope_if_met": float(np.mean(slopes)) if slopes else None,
        }

    cpts = fam["carrier"]["points"]
    ok_small = cpts[0]["error"] <= EPS_TARGET and cpts[1]["error"] <= EPS_TARGET
    ok_large = cpts[2]["error"] <= EPS_TARGET
    slope_low = (
        np.log(cpts[1]["time"] / cpts[0]["time"]) / np.log(cpts[1]["Qmax"] / cpts[0]["Qmax"])
        if ok_small else None
    )
    slope_high = (
        np.log(cpts[2]["time"] / cpts[1]["time"]) / np.log(cpts[2]["Qmax"] / cpts[1]["Qmax"])
        if ok_large and ok_small else None
    )

    if not fam["carrier"]["eps05_met_all"] and not any(f["eps05_met_all"] for f in fam.values()):
        verdict_text = (
            f"POSITIVE-FLOOR-BLOCKED: no family reaches eps={EPS_TARGET} at any Qmax "
            "(static transfer suppressed for Qmax << N_gap; carrier too slow within budget)"
        )
    elif slope_high is not None and abs(slope_high) < 0.35:
        verdict_text = (
            f"BOTH-REGIMES-THEN-FLOOR: carrier amplitude-limited at small Qmax "
            f"(slope {slope_low:+.2f}) then saturates near T = "
            f"{cpts[2]['time']:.3f}; positive eta-compression floor visible"
        )
    elif slope_low is not None and slope_low < -0.7:
        verdict_text = (
            f"AMPLITUDE-LIMITED: carrier time ~ 1/Qmax (slope {slope_low:+.2f}) "
            "across the caps tested; eta-compressibility plausible in the toy model"
        )
    else:
        verdict_text = (
            "INCONCLUSIVE: carrier errors "
            f"{['%.3f' % p['error'] for p in cpts]} do not separate regimes cleanly"
        )

    # ---- plots ---------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.8))
    ax = axes[0]
    styles = {"static": ("o", "-"), "optimized": ("s", "--"), "carrier": ("^", ":")}
    for family, (marker, lsty) in styles.items():
        qs = [p["Qmax"] for p in fam[family]["points"]]
        errs = [p["error"] for p in fam[family]["points"]]
        ts = [p["time"] if p["time"] else np.nan for p in fam[family]["points"]]
        ts_ok = [t if e <= EPS_TARGET else np.nan for t, e in zip(ts, errs)]
        ax.loglog(qs, ts_ok, marker=marker, ls=lsty, label=family)
        ax.loglog(qs, ts, marker=marker, ls="none", mfc="none", alpha=0.35)
    ax.axhline(np.pi / n_gap, color="k", lw=0.8, ls=":", label=r"$\pi/N_{gap}$")
    ref = [40.0 * (10.0 / q) for q in QMAX_GRID]
    ax.loglog(QMAX_GRID, ref, color="gray", lw=0.8, label=r"$\propto 1/Q$")
    ax.set_xlabel(r"amplitude cap $Q_{\max}$")
    ax.set_ylabel("minimal total time reaching eps")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    ax2 = axes[1]
    names = [k for k in table if k != "free_only"]
    vals = [table[k]["error"] for k in names]
    colors = ["tab:green" if v <= EPS_TARGET else "tab:red" for v in vals]
    ax2.bar(range(len(names)), vals, color=colors)
    ax2.axhline(EPS_TARGET, color="red", lw=0.8, ls="--")
    ax2.set_xticks(range(len(names)))
    ax2.set_xticklabels(names, rotation=60, ha="right", fontsize=7)
    ax2.set_ylabel("worst-case error")
    ax2.grid(alpha=0.3, axis="y")
    fig.suptitle("Radialization feasibility vs amplitude cap (hollow markers: eps not met)")
    fig.tight_layout()
    fig.savefig(ROOT + "/exp3_radialization.png", dpi=150)
    plt.close(fig)

    output = {
        "seed": SEED,
        "l_max": L_MAX,
        "m_sector": M_SECTOR,
        "task": "|l=1,m=1> -> |l=2,m=1>, sup_s leakage",
        "eps_target": EPS_TARGET,
        "n_gap": n_gap,
        "results": table,
        "families": fam,
        "regime": {
            "carrier_slope_Q10_to_100": slope_low,
            "carrier_slope_Q100_to_1000": slope_high,
        },
    }
    print(json.dumps(output, indent=2))
    print(json.dumps({"experiment": 3, "verdict": verdict_text}))


if __name__ == "__main__":
    main()
