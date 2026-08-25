# COUNTEREXAMPLE SEARCH — Can a legal play stall the program?

Source refs `L<n>` in `output/latex/operator_valued_riesz_singularity_note.tex`.
Question: does hazard divergence hold ALONG THE GENERATED TRAJECTORY
(Q of the brief), or can an explicit admissible adversary stall it?

---

## 1. Adversary A1 — the frequency ratchet (new construction)

**Idea.** Force the placement frequencies to blow up so fast that the
finite-spectral-model windows shrink geometrically, making `sum h_j < inf`
for every *greedy* schedule, while keeping all propositions' hypotheses true.

**Construction.** At stage `j`, after the group is fixed, the bundle
`(H_j(k), x_{p,j}(k))` contains collar modulations at all previously used
frequencies; its Lipschitz constant satisfies the feedback law
`Lambda_{j+1} >= c Lambda_j / eps_{j+1}` (Fourier tails of `C^1` data decay
like `L/n`; proof technique of `lem:one-step-placement`, L664–673). If the
FSM neighbourhood width is read modulus-limited, `h_j ~ delta_j / Lambda_j`
with `delta_j ~ eps_j / C_{rho,M_j}` (L1983–1985), then choosing the
placement epsilons merely summable (`eps_j = 2^{-2j}`) gives

```
Lambda_{j+1} >= 4 Lambda_j  =>  h_j <= h_0 4^{-j}  =>  sum gamma_j h_j < inf.
```

Every individual stage is fully certified (`h_j > 0`), amplitudes bounded,
`X_3` costs `<= zeta_j`, protected lists preserved. This is an **admissible
play** in which the adaptive averaging proposition
(`prop:adaptive-centre-averaging`) never forces `I_N -> 0`: the hazard sum
stays finite and `prop:coverage-obstruction` (L1391–1418) supplies matching
densities with `inf_j int w_j^beta > 0`.

**Verdict on A1.** Valid *as an attack on Route A only*, and only under the
unfavorable reading of Gap G2 (modulus-limited widths). Two independent
reasons it fails to be a global obstruction:

(a) **The ratchet is self-inflicted.** The Contractor chooses the placement
frequencies; nothing in the source forbids re-planning each generation from
scratch (fresh smooth background per shell), after which the modulus history
is irrelevant to the new certificates. The ratchet constrains greedy reuse of
one evolving bundle, i.e., exactly the adaptive scheme.

(b) **Route C ignores widths entirely.** Against a one-generation synthesis
(Theorem 6 of MAIN_ATTEMPT.md) there is no sequence `(h_j)` to shrink: the
finite cover is planned once against one bundle. Compactness of `K`, not a
width lower bound, does the work.

## 2. Adversary A2 — root-Zeno lengths (source's own, sharpened)

`prop:grouped-root-zeno` (L1741–1817): certified widths
`h_j = eta/(C M_j m_j)` with `M_j >= log N_j / (2rho)`, `N_j = ceil e^{j^2}`,
sum finite. **Why it cannot be realized along generated trajectories:** the
lengths `M_j` are lower bounds valid for *adversarially chosen* singular
bundles; the actual stage-`j` bundle is not adversarial but produced by
finitely many previous groups. Under Lemma 1 (atomicity, G1) the effective
upper bound is `M_j <= C(1 + log n_j) = O(log j)` (Lemma 3), and the cost
ledger forces `m_j >= c' j`, so `M_j m_j = O(j log j)` and
`sum 1/(M_j m_j) = inf`: by Proposition 4 (Cauchy–Schwarz dichotomy) there
are legal schedules with divergent hazard and summable errors. Root-Zeno is
thereby confined to black-box certificates about unknown bundles — precisely
the moral drawn in the source itself ("must use additional structure of the
actually generated phase bundles", L1781–1783).

**Residual life of A2.** If G1 fails — i.e., the comparison frame
`Theta_W(k)` is genuinely infinite-dimensional per energy — then Lemma 1–3
collapse, Dini compactness gives no rate, and one *cannot* currently rule out
that the generated bundles approach the zoom-mixture pathology of
`prop:mobius-orbit-haar-obstruction` (infinitely atomic measures tracking
boosts into Haar, L1867–1938). That would resurrect Zeno-type length demands.
This is the strongest surviving adversary scenario; see Section 4.

## 3. Impossibility result (what no adversary can do)

**Proposition.** No admissible play can block Theorem 6's generation.

*Proof.* The hypotheses consumed by Theorem 6 are: (i) smooth real finite
partial potential; (ii) finitely many probes, moments, continuous tests;
(iii) prescribed inner radius availability — successive shells give fresh
regions forever (assembly design L7734); (iv) norm continuity of the planned
bundle on `K` — real-analytic factors imply it at every stage regardless of
frequency content (bounded denominators `>= e^{-rho}`); (v) compactness of
`K`. None of these is stage-dependent; in particular no adversary choice of
past phases, frequencies, or cell placements can invalidate them for the next
generation, because the generation re-certifies everything from the current
bundle via the one-window proposition applied finitely many times. Off-window
behavior of earlier groups is harmless by exact phase-mean nonexpansion
(`lem:physical-hardy`, L1070–1084). Hence any play that keeps the dovetail
bookkeeping also admits the synthesis step; a stalling play would have to
violate a hypothesis of `prop:physical-grouped-one-window` itself, i.e.,
cease to be admissible. `square`

**Consequence.** Within the source's rule set, the adversary's winning
condition reduces to falsifying one of Gaps G1–G3 below; absent that, the
global problem is closed constructively and no stall exists.

## 4. Honest assessment of the remaining adversary space

If **G2 is unfavorable** (FSM width modulus-limited): Route A (adaptive
hazard) dies by A1 — this should be recorded as a genuine negative finding:
the hazard condition `eq:hazard-divergence` need NOT hold along greedily
generated trajectories, answering the brief's headline question as
"FALSE for the adaptive mechanism, UNDETERMINED-to-IRRELEVANT globally".
But note the problem statement itself offers the alternative "or a finite
broadband scalar synthesis which covers K in one generation" (L2080–2082);
A1 does not touch that route.

If **G1 fails** (infinite-dimensional comparison frame): Lemma 3 lapses; the
effective-length shield disappears. An explicit adversary would then try to
schedule groups whose composed fibers emulate the atomic-zoom mixture
construction (L1895–1927) at each stage. We could not exclude this without
G1, but neither can it be exhibited: the mixture needs infinitely many atoms
per stage while each group contributes finitely many cells (each cell acts by
a single normalized pushforward `mathcal T_g`). The atomic count grows by at
most `n_j` per stage even in the worst resolution of `Theta_W(k)`; whether
`n_j` is bounded along trajectories is exactly G1.

**Bottom line.** No admissible stalling trajectory was found. The two source
obstructions (Zeno, Möbius–Haar) attach to black-box/uniform-over-history
certifications and to the sequential adaptive scheme; the simultaneous
disjoint-shell synthesis circumvents both, subject to three verification
gaps (G1 atomicity/finite resolved block; G2 width provenance; G3 group-level
chromatic law), none of which is an obstruction-in-principle.
