# SETTLEMENT DOSSIER — Simon's Multidimensional L^2 Conjecture
**Workspace:** QM Problems · **Date:** 25 August 2026 · **Prepared by:** ox-alpha campaign

---

## 0. THE TARGET (user's Q2.png, verbatim)

> Suppose that $V(x)$ is a function on $\mathbb{R}^\nu$ such that
> $\int |x|^{-\nu+1}|V(x)|^2\,d^\nu x < \infty$, where $\nu \geq 2$.
> Prove that $-\Delta + V$ has absolutely continuous spectrum of infinite
> multiplicity on $[0,\infty)$.

This is Simon's Conjecture 20.2 (Kato tribute, R62.pdf). In polar coordinates
the weight cancels the Jacobian: the hypothesis is exactly
$V \in L^2(\mathbb R_+ \times S^{\nu-1})$ — the "multidimensional L^2" class.
The workspace program ($X_3$ = this class at $\nu=3$; paper-1 line ~98)
constructs, conditionally, bounded $V \in X_3$ whose AC spectrum dies on a
nonempty compact $K$ — refuting the conclusion at $\nu=3$.

## 1. STARTING STATE (what the user had built)

Two papers + one technical note (output/latex/operator_valued_riesz_singularity_note.tex,
23 July 2026). Verified proved-here ledger includes:
- One-cell dimension-free reciprocal contraction FALSE (root-of-unity).
- Fixed-height GROUPED singular-bundle contraction TRUE.
- One-window physical grouped contraction with h > 0 but NO uniform width bound.
- Adaptive averaging reduces coverage to hazard divergence sum gamma_j h_j = inf.
- Root-Zeno certificate: black-box certified widths can have summable hazard.
- Mobius-Haar orbit obstruction; dipole route closed negatively; slab/log-shell
  audits; outward angular-time budget 1/R.
Open gates: Problem prob:physical-grouped-global; Problem prob:short-time-radial-compiler.
Conditional counterexample (prop line 7712): global grouped Lemma B per stage
=> exists V in X_3 bounded with P_ac(H)1_K(H)=0 => conjecture FALSE.

Literature recon (settlement/literature/LITERATURE_RECON.md): conjecture OPEN
for every d >= 2 worldwide as of today; no scooping; "d>=4/5 settled" folklore
is a misattribution of Killip-Visan NLS work; no published control theorem
supplies the missing small-time step; all known counterexamples sit outside
the weighted-L^2 class.

## 2. WHAT THIS CAMPAIGN FOUND

### Route 1 — hazard bypass (NEW, pending audit)
attack-hazard/MAIN_ATTEMPT.md **Theorem 6**: prob:physical-grouped-global is
solvable WITHOUT hazard divergence: ONE generation of finitely many one-window
groups on pairwise disjoint fresh shells; finite cover by compactness of K
(each window needs only individual positivity, not uniform bounds); sequential
placement with globally locked protected lists; off-window behavior exact
phase-mean nonexpansion; factor <= 3/4 + zeta on total targeted beta-moment,
full ledger. Supporting new results with proofs:
- Lemma 2 quantitative Poisson barrier: Q_r(nu) <= C_beta A^{1-beta}(1-r)^{1-beta}
  uniformly over A-atomic measures.
- Lemma 3 effective group lengths M_j = O(log n_j) along trajectories
  (neutralizes root-Zeno).
- Prop 4 / Thm 5 Cauchy-Schwarz hazard dichotomy + explicit divergent schedule.

Orchestrator trace: thm:scalar-dovetail needs only PER-STAGE assemblies;
counterexample proof (L7725) assumes exactly this input; radialization belongs
to the alternative lens route and becomes unnecessary if Theorem 6 stands.

### Route 2 — short-time radialization likely constructible (pending G1)
attack-radialization/MAIN_RESULT.md + MAGNUS_FEASIBILITY.md: in the free-flow
interaction picture Omega(T) = -iT(A_3 + q_bar) + O(T^2||q||^2): higher Magnus
orders die as T = sum t_j -> 0 with FIXED amplitude. Lens drift renormalization
is a HEIGHT condition (h >= |tau-1| max|spec A_3|_E| / 2), not a time condition;
cos-carrier numerics achieve any prescribed tau with amplitude ~ sqrt|tau-1|.
Orchestrator spread bound (independent): s-continuum tracking forces
tau <= 1 + dim(E)*Qmax — consistent; unbounded tau impossible, fixed tau fine.
Evades twist/wrapping cost floors (those price integrated profile varphi/tau).

### Numerics (settlement/numerical/SUMMARY.md)
- VALIDATED: n=1 constants to 4 decimals; Zeno law M >= log N/(2 rho) to 0.6%;
  coherent-vs-decohered probe dichotomy; literal-trace n-independence (4e-16).
- SCOPE ERROR FOUND in source thm:finite-contraction: sup over ALL A>0 EXCEEDS 1
  for beta >= 0.75 (up to ~1.6, robust quadrature). Repair: program only needs
  scalar/coherent probes (dovetail is scalar) and/or beta <= 1/2; nothing
  load-bearing uses the blanket form. Corrected statement required in writeup.
- Hazard game sign-sensitivity confirmed => do not rely on adaptive certificates
  (Route 1 doesn't).
- Toy transfer tasks show positive floors under s-uniformity; diagonal
  renormalization (the lens need) remains feasible per Magnus analysis.
  Entrance/exit frames = residual open piece (G1 check).

## 3. VERDICT LOGIC

prop:conditional-counterexample-final activates iff EITHER
(a) Theorem 6 survives audit [audit-theorem6/AUDIT_REPORT.md], OR
(b) radialization G1 freeze-check passes [attack-radialization/G1_FREEZE_CHECK.md]
    and the entrance/exit frame question closes positively.

Either outcome => exists bounded real V in X_3 (hence satisfying the Q2.png
integral condition at nu=3) with AC spectrum killed on K => Q2.png statement FALSE.

If BOTH fail with located obstructions => the lens route closes structurally;
conjecture SURVIVES this attack line; dossier documents why precisely.

## 4. FINAL VERDICT

[PENDING — filled when audit + freeze check return]

## 5. DELIVERABLE MAP

settlement/
  literature/LITERATURE_RECON.md          — world status, no scooping, frontier map
  attack-hazard/GAME_FORMALIZATION.md     — chromatic game from source, line refs
  attack-hazard/MAIN_ATTEMPT.md           — Lemmas 2-3, Props 4, Theorems 5-6
  attack-hazard/COUNTEREXAMPLE_SEARCH.md  — adversary impossibility for Thm 6
  attack-hazard/VERDICT.txt               — hazard-route summary
  attack-radialization/SCALING_NOTES.md   — ledger conventions
  attack-radialization/MAGNUS_FEASIBILITY.md — orders 1-3, class constraint, QSL
  attack-radialization/MAIN_RESULT.md (+ADDENDUM) — construction sketch + gaps
  attack-radialization/num/*              — carrier scans, parity split, leakage
  attack-radialization/G1_FREEZE_CHECK.md — [pending] freezing-criterion audit
  audit-theorem6/AUDIT_REPORT.md          — [pending] red-team verdict on Thm 6
  numerical/SUMMARY.md                    — four-experiment falsification report
  synthesis/STATE_OF_PLAY.md              — full working log (this dossier's source)

## 6. HONESTY LEDGER

- Every claim above traces to files on disk; nothing is asserted from memory.
- Two items remain open at time of writing (Section 4 logic decides them).
- Known scope repair needed regardless of verdict: blanket contraction constant
  must be restated for coherent probes or beta away from 1 (numerics 1b).
- This is AI-generated mathematics: independent human verification is REQUIRED
  before any public claim touching the open conjecture. The author's own
  truth-in-claims standard (note lines 194-262) is adopted wholesale.
