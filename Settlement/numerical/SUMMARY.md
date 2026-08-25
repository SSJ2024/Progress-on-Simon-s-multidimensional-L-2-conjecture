# Numerical Laboratory — Settlement Summary (4 experiments)

Date: 25 Aug 2026. Workspace: `settlement/numerical/`.
Scripts: `exp1_grouped_contraction_constants.py`, `exp2_hazard_game.py`,
`exp3_radialization.py`, `exp4_root_zeno_reproduction.py` (all `py -3`-run;
logs `exp*_run.log`, machine verdicts `exp*_verdict.json` or last JSON line of
the log, figures `exp*.png`). Seed 20260825 everywhere.

Bugs found and fixed during this session (details in script docstrings):
`dir_gains` summed over the wrong axis (directions instead of components);
`wishart_ratios` fed a non-Hermitian matrix to `eigvalsh` (silent
lower-triangle readback produced impossible ratios > 1); a dead code block
double-drew Haar unitaries per configuration; the window search was replaced by
an exact cumsum box filter; experiment 4 was redesigned around the exact
spectral reduction described below after matrix-path Monte Carlo proved
needless.

---

## Experiment 1 — grouped contraction constants kappa_{beta,n}(rho)

**Question.** For the Szego kernel `F_z = (aI + z b H)^{-1}` on the circle,
is `kappa_{beta,n}(rho) = sup_H sup_A E_z[tr((F_z^* A F_z)^beta)]/tr(A^beta)`
strictly below 1 for every tested `(beta in {.25,.5,.75}, n in {1..64},
rho in {.5,1,2})`, degrading gracefully in n?

**Method.** Batched deterministic z-grid (1536 points), 8 Haar H per config,
three probe families: random Wishart A, random rank-one directions, and the
coherent rank-one probe `u = V 1/sqrt(n)` in the eigenbasis of H. The n=1
case has an analytic anchor `C_beta(rho) = E[|a+b e^{it}|^{-2 beta}]`, which
the estimator must reproduce.

**Result: PASS.**

- All 63 configurations give `kappa_estimate < 1`; worst value 0.99994.
- n=1 estimates match the analytic anchors to 5 decimals
  (e.g. beta=.25: rho=.5 -> 0.95547 vs 0.95548; rho=2 -> 0.57614 vs 0.57614),
  validating the whole pipeline.
- Decay law: the gap closes like **1/n**, not faster. Fitting
  `gap * n` gives coefficients 0.012 / 0.121 / 1.126 at
  (beta,rho) = (.25,.5), (.5,1), (.75,2), i.e. 24–46% of the first-order
  prediction `beta(1-beta) sinh^2(rho)` from the variance of the coherent
  probe's Poisson average. Representative values (beta=.75, rho=2):
  kappa = 0.576 (n=1) -> 0.757 (n=4) -> 0.905 (n=16) -> 0.977 (n=64).

**Reading.** Exactly what the theory requires: every probe respects the
Jensen cap, no probe family ever reaches 1, and the loss of contraction is
polynomial in n — graceful, not catastrophic. Grouping cells of growing
dimension remains a contraction, just an increasingly weak one.

## Experiment 2 — adaptive hazard game vs a phase adversary

**Question.** With the player choosing greedy windows `h * mass(window)` and
the adversary realizing `gamma_eff = gamma(1 - s*D)` (`D = |m|` "coherence"
rule or `D = 1 - |m|` "moment" rule), does total mass always reach ~0 with
diverging hazard, or can the adversary stall it at positive mass?

**Setup.** Cantor middle-thirds product measure and a 24-spike random Fourier
proxy on a 2^14 grid; gamma in {.25,.5,1}; strength s in {0,.5,1}; 2500 rounds.

**Result: ADVERSARY-CAN-STALL — but only at full strength.**

- 33/36 configurations go extinct (final mass < 2e-6); cumulative hazard at
  extinction is O(0.1–1.6) and grows without bound relative to residual mass.
- The three exceptions are all `(moment rule, s = 1.0, fourier_spikes)`:
  final mass **0.694 / 0.571 / 0.382** (gamma = .25/.5/1) with cumulative
  hazard frozen at 0.02–0.06. Wide windows over many spikes have near-vanishing
  first moment `|m|`, so `gamma_eff = gamma*|m| ~ 0`: the realized removal
  rate collapses and mass plateaus far from 0.
- At s <= 0.5 even the moment rule cannot prevent extinction (slower, but the
  hazard still accumulates).

**Reading.** Hazard divergence is NOT automatic. Under the oscillation-deficit
adversary at full strength, greedy adaptive play stalls at O(1) mass. This is
a concrete toy realization of the source's own warning
(prop:grouped-root-zeno): singularity plus naive window play does not force
`sum gamma_j h_j = infinity`; additional structure of the generated bundles is
needed, as prob:physical-grouped-global anticipates.

## Experiment 3 — radialization toy model: time vs amplitude cap

**Question.** In the truncated S^2 Galerkin model (l = 1..24, m = 1 sector,
exact Gaunt nearest-neighbour mask, exact segment propagation — no Trotter
error), how does the minimal total time to reach transfer error eps = 0.05
for the task |1,1> -> |2,1> scale with the amplitude cap Qmax in
{10, 100, 1000}? Does some protocol family show eta-compressibility
(time -> 0 achievable), or a positive time floor?

**Result: POSITIVE-FLOOR-BLOCKED.**

- No family (static pulse, sinusoidal carrier with swept omega, or 6-segment
  Nelder-Mead-optimized control) reaches eps = 0.05 at ANY Qmax:
  best errors are 0.234 (Qmax=10, carrier), 0.501 (Qmax=100), 0.902
  (Qmax=1000). Larger amplitude makes things WORSE: strong masks drive
  population into intermediate l-levels (leakage), so the two-level picture
  degrades exactly when the displacement heuristic T ~ N_gap/Qmax predicts
  success.
- Consequently there is no meaningful T(Qmax) power law above Qmax ~ N_gap =
  4: the required time does not fall with amplitude; the obstruction is
  structural (off-resonant coupling / spread into the ladder), not
  amplitude-limited.

**Reading.** The toy compiler is **not** eta-compressible: brute amplitude
does not buy short-time radialization, and the data indicate a positive time
floor (here effectively infinity within the searched families). This is
consistent with the orchestrator's instantaneous-spread-bound analysis: the
uniform-in-s requirement forces the instantaneous Hamiltonian to match
tau*A_3 on the working subspace at ALL s, which bounded-amplitude masks
cannot deliver while simultaneously rotating the target pair. As a lower
bound it is model-limited (L = 24, one sector, three control families), but
every honest attempt hit the same wall.

## Experiment 4 — root-of-unity Zeno reproduction (prop line 1741)

**Question.** For `H = diag(1, omega, ..., omega^{n-1})`, omega = e^{2pi i/n},
`F_z = (aI + z b H)^{-1}`, verify (i) the gap of the grouped functional tends
to 0 as n grows (n up to 256), and (ii) that at FIXED n the Haar average over
random unitaries stays strictly below 1 with a visible margin.

**Method (exact, not Monte Carlo).** `aI + z b H` is normal-diagonal, so the
spectrum of `F_z^*F_z` is `{w(t + 2 pi j/n)}_j` with
`w(x) = |a + b e^{ix}|^{-2}`. Two functionals, both reduced to circle
quadrature:

- literal `Q_lit(n) = E_t[(1/n) sum_j w^beta]`;
- source-faithful `Q_prob(n) = E_t[((1/n) sum_j w)^beta]`
  (eq:grouped-root-moment puts the nu_N-average INSIDE the beta power).

The n-grid average of the Poisson kernel keeps only Fourier harmonics
divisible by n, leaving remainder ~ `|tanh(rho)|^{2n} = e^{-2 rho n}`;
Haar-random phases are evaluated by the same quadrature over 32 random phase
sets (the functional depends on H only through its eigenvalue phases, since
tr W_z = ||F_z||_F^2 = sum_i w(t + theta_i); cross-checked against the full
matrix/z-grid computation with agreement to machine precision).

**Result: REPRODUCED.**

- `gap_decays_with_n = true`. Gaps at (beta=.5, rho=.5):
  5.9e-2, 1.2e-2, 5.2e-4, 1.1e-6, 4.7e-12 for n = 1,2,4,8,16 and identically
  0 (< 1e-18) beyond; measured log-gap slope vs n equals the predicted
  `2 log tanh(rho)` with median ratio **1.006** across all nine (beta, rho)
  pairs. This is exactly the `M >= log N / (2 rho) - C` mechanism of
  eq:grouped-root-length-lower-bound: certified widths `h_j = eta/(C M_j m_j)`
  with `N_j = ceil(e^{j^2})` therefore sum to less than infinity — the Zeno
  certificate stands.
- The literal trace is n-INDEPENDENT to 4.4e-16 (it equals `C_beta(rho)` for
  every n): grouping alone contracts nothing. The proposition's point —
  singularity alone gives no nonsummable lower bound — is reproduced
  quantitatively.
- `fixed_n_gap_positive = true`. At fixed n the Haar-random functional stays
  strictly below 1 with visible margin: median margins 1.4e-2 / 3.1e-3 /
  8.3e-4 at n = 4/16/64 (worst-case-over-draws margins 3.0e-2 / 1.0e-2 /
  4.5e-3), shrinking like c/n rather than exponentially — generic phase
  spectra never achieve the root-of-unity coherence, but never close the gap
  either.

---

## Implications for the conjecture

**The numerics support the SURVIVAL of Simon's L^2 conjecture (the "prove"
side) against this workspace's attack program; they actively undermine both
halves of the conditional disproof.**

1. The contraction calculus checks out everywhere it can be tested. Exp1
   confirms kappa_{beta,n}(rho) < 1 with polynomial (1/n) degradation and
   reproduces analytic anchors to 5 decimals; exp4 confirms the root-Zeno
   mechanism with log-gap slope matching theory to 0.6%. There is no
   numerical counterexample signal to the note's proved estimates — the
   tools the survival argument relies on are sound.

2. The hazard-divergence route fails in adversarial models. Exp2 exhibits
   concrete configurations (full-strength oscillation-deficit adversary,
   multi-spike measures) where greedy adaptive window play stalls at O(1)
   mass with bounded cumulative hazard. Combined with exp4's demonstration
   that grouping contributes nothing without coherence (literal trace
   n-independent), the burden of proof that
   `sum gamma_j h_j = infinity` along generated trajectories lies entirely
   with special structure of the bundles — which is precisely the unresolved
   prob:physical-grouped-global.

3. The radialization route looks structurally blocked. Exp3 finds no control
   family reaching even eps = 0.05 at amplitudes up to 250x the spectral gap,
   with error INCREASING in Qmax through off-resonant leakage — the
   signature of a positive time floor, not of an eta-compressible compiler.
   If the short-time angular-time target of prob:short-time-radial-compiler
   is impossible, "global phase placement" cannot activate the broadband
   synthesis either.

Per the dossier's own decision tree: hazard can stall AND short-time
radialization shows a floor => the lens route is closed => the workspace's
conditional counterexample dies unless a genuinely new route appears. The
conjecture itself is of course not decided by simulation; but every place
where the disproof program needed nature to cooperate — universal hazard
divergence, amplitude-bought speedups, super-polynomial coherence in generic
spectra — the numerics say no. Recommended next theoretical effort: characterize the
generated bundle structure needed for hazard divergence (prob:physical-grouped-global),
or prove the radialization lower bound suggested by exp3's leakage mechanism.

---

## Addendum: sup_A cross-check (`exp1b_supA_check.py`, corrected)

An intermediate revision of the sup-over-A probe computed
`Y_z = F_z^* diag(w) F_z` by scaling the wrong axis of `F_z`, i.e. it formed
`diag(w) (F_z^* F_z)` — non-Hermitian — which `eigvalsh` silently read from a
single triangle, producing spurious ratios up to 1.74 and a false
"SUP-A-EXCEEDS-ONE" alarm for beta >= 0.75.

The corrected script uses an algebraically identical, bug-proof route:
`svd(sqrt(D) F_z)` has singular values `s_i` with
`tr[(F_z^* D F_z)^beta] = sum_i s_i^(2 beta)`. Seeded rerun (deterministic
z-quadrature, 150 random Wishart draws + 7-restart Nelder-Mead per cell,
nine `(n, beta)` cells at rho = 1):

- worst probe over all cells: **0.98882 < 1**; zero of 1350 random draws
  exceeded 1; optimizer never exceeded 0.982.
- coherent rank-one reference stayed <= 0.973 throughout.

VERDICT: `"ALL-BELOW-ONE (corrected): worst probe 0.98882 < 1 across all 9
cells; the earlier sup-A>1 alarm is retracted as a non-Hermitian-axis bug in
the previous revision"`.

Consequence for the reading above: the Jensen cap holds for ALL A at every
tested beta <= 0.75 (and beta = 0.9), so Experiment 1's PASS is unconditional
over the tested grid; no "spread-out states exceed 1" caveat is needed. The
conjecture-relevant conclusions are unchanged — they rest on exp2 (stalling),
exp3 (positive floor) and exp4 (root-Zeno gap law), all of which are
unaffected by this estimator bug.
