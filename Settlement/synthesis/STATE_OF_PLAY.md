# Settlement dossier — state of play (working log)

Started: 25 Aug 2026. Goal: reach a definite verdict on the remaining gap of the
Simon multidimensional L^2 program contained in this workspace.

## What the existing material establishes (verified by direct reading)

Source of record: `output/latex/operator_valued_riesz_singularity_note.tex`
(23 July 2026), plus `siam-siraji-simon-l2-research/papers/*/main.tex`.

Proved in the note:

- One-cell, dimension-free reciprocal contraction is FALSE
  (`prop:no-dim-free`, root-of-unity obstruction).
- Fixed-height GROUPED singular-bundle contraction is TRUE
  (`thm:singular-bundle-grouped-contraction`): a finite product of scalar
  SU(1,1) cells collapses to one effective Poisson barrier; contracts every
  compact family of singular spectral measures.
- One-window physical grouped contraction holds with NO uniform lower bound on
  the window half-width h (`prop:physical-grouped-one-window`, line ~1993).
- Adaptive-centre averaging reduces global coverage to hazard divergence
  sum_j gamma_j h_j = infinity (`prop:adaptive-centre-averaging`, line ~2085;
  gamma_0 = 1/2 - o(1) per `cor:exact-hazard-bottleneck`).
- Root-Zeno certificate (`prop:grouped-root-zeno`, line ~1741): if group length
  M_j >= (log N_j)/(2 rho) - C and certified widths are h_j = eta/(C M_j m_j),
  then N_j = ceil(e^{j^2}) makes sum h_j < infinity. So singularity alone does
  NOT give hazard divergence; extra structure of generated bundles is needed.
- Pure-point Moeobius history orbit can accumulate on Haar measure; no fixed
  grouped length is uniform over all prior ideal scalar histories.
- The dipole/multiband carrier route is CLOSED NEGATIVELY
  (Zakharov-Shabat energy floors). Free-flight recurrence cannot supply the
  broadband inverse (`prop:positive-flight-no-recurrence`). Slab/log-shell
  architectures audited: bounded-depth cascades freeze densities
  (`prop:direct-scaled-slab-density-no-go`, `prop:bounded-depth-density-no-go`);
  logarithmic shells need angular degree comparable to R
  (`prop:log-shell-ballistic-degree`) and isolated Born carriers have a cost
  floor (`prop:log-shell-ballistic-born-cost`).
- Conditional counterexample (`prop:conditional-counterexample-final`,
  line ~7712): IF Problem prob:physical-grouped-global holds at every finite
  stage THEN there is bounded real V in X_3 and compact nonempty K with
  P_ac(-Delta+V) 1_K(-Delta+V) = 0. I.e., Simon's conjecture FALSE.
  Under the same hypothesis as stated there.

Open problems that decide the verdict:

1. prob:physical-grouped-global (line ~2067): finite chromatic coverage /
   hazard divergence / one-generation broadband synthesis.
2. prob:short-time-radial-compiler (line ~7036): eta-short-angular-time
   radialization of the finite-frame compiler. A positive answer activates
   prob:physical-grouped-global "by global phase placement"; a lower bound
   excluding eq:short-angular-time-target closes the lens implementation
   structurally.

## Decision tree

- Hazard diverges along generated trajectories OR short-time radialization
  proved => counterexample route reopens => attempt full assembly =>
  verdict DISPROVE (conditional on audit).
- Short-time radialization impossible + hazard can stall => lens route closed
  => conjecture survives THIS attack line; verdict remains OPEN globally but
  the workspace's own conditional disproof is dead unless another route exists.

## Running units

1. Q2 transcription (2nd/Q2.png) — pending.
2. Literature recon 2026 — pending.
3. Numerical lab (4 experiments) — pending.
4. Hazard attack (prove/disprove sum gamma_j h_j = inf) — pending.
5. Radialization attack (Magnus/speed-limit analysis) — pending.

## AUDIT VERDICT IN (21:03) — Theorem 6 UNPROVEN, NOT UNSOUND; repair dispatched

[Red-team audit] full report: settlement\audit-theorem6\AUDIT_REPORT.md.
A PASS (protection genuinely global, pointwise Hardy identity + simultaneous
placement + zero-cost collar frequencies). B PASS (off-window nonexpansion,
per-functional errors independent of counts). C PASS (h>0 with any zeta; no
live proved width-shrinkage theorem — chromatic law is hypothesis-only or in
\iffuse block L7411-7481). D PASS (re-certification via trace-class/
Kato-Rosenblum). F PASS (NO circular dependence on lens/radialization).
G PASS (assembly proof sound). E GAP moderate (sum-level vs per-probe
dovetail arithmetic). H GAP MAJOR (Theorem 6 gives sum-level 3/4;
prob:physical-grouped-global needs PER-PROBE contraction; Corollary 7
overclaims). G3 minor (block chromatic law = hypothesis, promote to lemma).

REPAIR DISPATCHED [repair unit]: Theorem 6' per-probe synthesis (generations
aimed at one probe at a time, tripled factor (3/4)^3 < 1/2 per probe,
protected lists carry the rest), block-chromatic-law lemma with proof,
final corollary + load-bearing dependence list. If it closes =>
prob:physical-grouped-global holds => prop:conditional-counterexample-final
activates => conjecture FALSE relative to the program's proved ledger.

## G1 FREEZE CHECK IN (20:55) — Route 2 downgraded

[G1 checker] verdict: NO — the fixed-degree temporal-carrier compiler FAILS
the radial audit. Key discovery: the density-freezing no-gos apply to ANGULAR
PHASE GATES too, not just spatial drifts: multiplication flows preserve
position densities pointwise, but the lens gate e^{is tau A_3}|span{e0,el}
MOVES <M_el> by O(1); so any freezing architecture excludes the lens qua phase
gate. The carrier's omega->infty is TEMPORAL and invisible to every quantity
in the freezing proofs (kinetic time, degree D_R, trajectory energies,
semiclassical scales) — those integrate exact commutator identities valid for
any temporal profile; fast alternation purchases nothing.
Per criterion: slab density-no-go APPLIES-AND-VIOLATED; multiscale condition
APPLIES-AND-VIOLATED (violating the product criterion needs ballistic
E_j ~ N_j^2/R_j — a spectral scale the carrier lacks); log-shell ballistic
degree APPLIES-AND-VIOLATED (fixed degree is o(R), upgrade cost-floored);
outward budget APPLIES-AND-SATISFIED. Word-level corollary: sum t_j >=
c/(1+G^2) > 0 at bounded trajectory gradient G — eta-short compilation needs
UNBOUNDED interacting scale diversity, which fixed-degree carriers deny by
design.

ROUTE 2 STATUS: word-level Magnus feasibility STANDS as mathematics, but the
mechanism cannot be radialized within any audited architecture. The residual
hope for Route 2 would need ballistic harmonic-degree excursions refocused in
vanishing flight — precisely what prop:log-shell-ballistic-born-cost floors.
Route 2 therefore does NOT currently activate the counterexample.

VERDICT NOW RESTS ON ROUTE 1: Theorem 6 audit (still running).

## NUMERICAL LAB VERDICTS IN (20:45)

[NUM lab v2] completed all experiments. Referee digest + my reconciliations:

1. EXP1/1B — CONTRACTION CONSTANTS, WITH A CATCH. Coherent/rank-one probes:
   kappa_{beta,n} < 1 at ALL tested beta, gap ~ c(beta,rho)/n (generic phases)
   or ~ |tanh rho|^{2n} (equally spaced phases) — exact n=1 anchors reproduced
   to 4 decimals. BUT sup over ALL A>0 EXCEEDS 1 for beta >= 0.75
   (optimized diagonal A: 1.45 at n=4 beta=0.75; 1.63 at beta=0.9;
   robust deterministic quadrature). IMPLICATION (referee flag): the note's
   blanket Theorem thm:finite-contraction (kappa_{beta,n}<1 for EVERY A>=0,
   0<beta<1) is NUMERICALLY FALSE near beta -> 1 for spread A. My theoretical
   sanity check supports plausibility: for diagonal H the ratio is exactly
   C_beta(rho) < 1 regardless of A, so violations require noncommuting H, A —
   consistent with the observed Haar-generic excess. REPAIR: the program only
   ever applies the contraction to SCALAR/coherent probes (dovetail theorem is
   scalar; grouped functional Q_prob verified correct in exp4b) and may FIX
   beta <= 1/2 throughout; nothing load-bearing seems to need the blanket
   form. ACTION ITEM: final dossier must state the corrected scope
   (rank-one/coherent inputs or beta bounded away from 1).

2. EXP2 — HAZARD GAME IS SIGN-SENSITIVE. Formula-as-written: extinction
   always (mass -> 1e-6). Oscillation-deficit adversary: stalls in 3/36
   configs (mass plateau 0.38-0.69). Confirms Route 1 should NOT rely on
   black-box adaptive certificates — consistent with Theorem 6 bypassing
   adaptation entirely (planned cover, no history-uniform widths).

3. EXP3 — TOY RADIALIZATION BLOCKED FOR TRANSFER TASKS. On truncated S^2
   (L=24), NO family (static/resonant/optimized) reached eps=0.05 for the
   POPULATION TRANSFER |1,1> -> |2,1>; errors GREW with Qmax via
   s-uniformity dephasing (fast segments amplify detuning sensitivity).
   APPARENT CONFLICT with radialization-v2 verdict (likely TRUE): RESOLVED —
   different tasks. Exp3 tests an OFF-DIAGONAL transfer (displacement-bound
   regime, genuine floors). The LENS INSTANCE needs only the DIAGONAL
   renormalization chi(s)e^{is tau A_3}|_E (phase gates), where Magnus
   order-1 compression applies and higher orders die as (T Qmax)^2 -> 0 with
   FIXED Qmax and T->0. Both results coexist: eta-short DIAGONAL compilation
   plausible; eta-short TRANSFER compilation floor-blocked. Whether the
   finite-frame compiler's required gates reduce to diagonal ones for the
   lens insertion (they do for the drift itself; entrance/exit frames are the
   open part — G1 freeze check running) decides which side binds.

4. EXP4 — ROOT-ZENO REPRODUCED TWICE. Decohered probes pinned at C_beta(rho);
   coherent probes rise to 1; grouped functional gap ~ exp(2n log tanh rho),
   measured/predicted slope ratio 1.006 => M >= log N/(2 rho) law confirmed.
   Literal trace is n-independent to 4.4e-16 (no contraction from grouping
   alone) — the structural distinction the program emphasizes is real.

NET: numerics VALIDATE the program's quantitative machinery where closed
forms exist, REFUTE its naive universal-constant form (needs beta/scope
restriction), and locate the true battlefield: diagonal-vs-transfer gates
under the s-uniform ledger.

## RADIALIZATION VERDICT IN (20:10)

[Radialization attack v2] completed. Verdict: prob:short-time-radial-compiler
LIKELY TRUE for the lens instance. Mechanism: interaction picture gives
Omega(T) = -iT(A_3 + q_bar) + O(T^2||q||^2): higher Magnus orders vanish as
sum t_j -> 0 WITHOUT amplitude growth; order-1 compression identity
P_E M_qbar P_E = tau A_3|_E + c Id + rho handles the drift. Renormalization
is a HEIGHT condition (h >= |tau-1| max|spec A_3|_E|/2, amplitude ~ sqrt|tau-1|
via cos-carrier, numerics to 1e-15), NOT a time condition — consistent with my
instantaneous-spread bound above (both say: fixed tau needs bounded height;
unbounded tau impossible). Evades twist/wrapping cost floors because those
price integrated profile varphi/tau with degree ~ 1/tau, whereas this uses
fixed-degree masks. Numerics: leakage kappa^2 ~ R*/C independent of carrier
frequency. New exact structural fact: renormalization strength = complementary-
channel coupling identically (max split = 4h/(3sqrt3), sharpening
prop:no-exact-scalar-galerkin-mixer).

Remaining flip risk: G1 — reciprocal-radius criterion eq:multiscale-density-
no-go-condition unverified for the temporal-carrier family vs slab freezing
(focused checker dispatched). Secondary: G7 ledger-convention reconciliation
(QSL floor under strict charging vs kicks-free convention at L7040).

ROUTE MAP TO VERDICT:
- Route 1 (hazard): Theorem 6 one-generation synthesis => global grouped Lemma B
  per stage => conditional counterexample. UNDER RED-TEAM AUDIT.
- Route 2 (radialization): short-time compiler likely TRUE (G1 pending)
  => activates global phase-placement route independently.
Either route alone activates prop:conditional-counterexample-final.

## MAJOR DEVELOPMENT — Theorem 6 (hazard attack, 19:30)

The [hazard attack v2] returned a candidate solution of prob:physical-grouped-global:
ONE-GENERATION FINITE BROADBAND SYNTHESIS (MAIN_ATTEMPT.md Theorem 6):
finitely many one-window groups on pairwise disjoint fresh shells covering K
by compactness; sequential placement with globally locked protected lists;
factor 3/4 + zeta on the total targeted beta-moment; full ledger. Claim: no
uniform width lower bound is needed (each h_l > 0 individually; finiteness
from compactness), off-window behavior is exact phase-mean nonexpansion, and
the Zeno/Mobius obstructions bind only history-uniform certificates.

New supporting results (complete proofs in MAIN_ATTEMPT.md):
- Lemma 2: quantitative Poisson barrier Q_r(nu) <= C_beta A^{1-beta}(1-r)^{1-beta}
  uniformly over A-atomic measures.
- Lemma 3: effective group lengths M_j = O(log n_j) along trajectories
  (conditional on atomicity G1) — neutralizes root-Zeno.
- Proposition 4 + Theorem 5: Cauchy-Schwarz hazard dichotomy; explicit
  admissible schedule with sum gamma_j h_j = infinity, sum eps_j < infinity
  (conditional on chromatic width provenance G2).

My own referee trace (orchestrator): thm:scalar-dovetail (L771) needs only
PER-STAGE assemblies (no cross-stage uniformity); the counterexample proof at
L7725 already assumes exactly "global physical grouped Lemma B per stage";
one-window ingredients are all in the proved-here ledger; radialization
belongs to the ALTERNATIVE lens route (L7775 wording: "only remaining PHYSICAL
input") and becomes unnecessary if Theorem 6 stands. If correct =>
prop:conditional-counterexample-final activates => Simon's conjecture DISPROVED.

STATUS: pending independent red-team audit (audit unit dispatched, scope A-H:
protection quantifiers, off-window mechanism, width/cost simultaneity,
sequential composition re-certification, dovetail arithmetic fit, hidden
circularity vs radialization, assembly proof, quantifier match). Verdict
withheld until audit returns.

## Orchestrator analysis update (18:20)

New observation (mine) — INSTANTANEOUS SPREAD BOUND, a candidate obstruction
for prob:short-time-radial-compiler:

The requirement sup_{s in [s0,s1]} ||W_s - chi(s)e^{is tau A_3}|_E|| < eps
with W_s = T-exp(-is int_0^T (A_3 + u(r))dr) forces, at every s in the
INTERVAL (not just near s=0), the gauge-transformed instantaneous Hamiltonian
P(s)^{-1}(A_3 + u(sT))P(s) to match tau*A_3 + c on E up to o(1). Spectra are
conjugation-invariant, so the E-block of the instantaneous Hamiltonian must
have spectral spread >= 2*tau - o(1) at every s (take E containing eigenspaces
l=0 and l=1, spread of A_3|_E = 2). But the E-block is
A_3|_E + u * (matrix of <Y_i|q|Y_j>) with |<Y_i|q|Y_j>| <= ||q||_inf = Qmax,
so its spread is <= 2 + 2*dim(E)*Qmax. Hence:

    tau <= 1 + dim(E)*Qmax   (necessary, up to constants).

Consequence: with ONE pointwise height bound held fixed (as the problem
requires), arbitrarily large renormalization tau is IMPOSSIBLE. If the radial
ledger demands tau growing with R (which is why compression is wanted at all),
the lens implementation is structurally blocked and the conjecture SURVIVES
this attack line. Conversely if the required tau is a fixed finite constant,
a bounded-amplitude duty-cycle + Stark-shift synthesis plausibly reaches it
and eta-compression follows; the whole verdict then hinges on WHAT tau the
radial insertion actually needs. Both attack units have the context; this
spread bound is the sharpest necessary condition found so far.

Mirror observation for the hazard side: the Zeno-shrinkage worry reduces to
whether phase placement must inject k-oscillation at scale h_j into the
bundle (forcing h_{j+1} = O(h_j), geometric decay, summable hazard) or can
concentrate winding outside active windows. That tension is now the formalized
game in settlement/attack-hazard/.

## Problem statement confirmed (Q2.png)

User transcription (25 Aug 2026):

> Suppose that V(x) is a function on R^nu such that
> int |x|^{-nu+1} |V(x)|^2 d^nu x < infinity, where nu >= 2.
> Prove that -Delta + V has absolutely continuous spectrum of infinite
> multiplicity on [0, infinity).

This is Simon's Conjecture 20.2 verbatim (Kato tribute, R62.pdf). Alignment
check PASSED: X_3 in paper-1 main.tex line ~98 is defined as real functions
square integrable against the radial weight |x|^{1-d}, i.e. exactly the
hypothesis above at nu = d = 3 (Jacobian r^{d-1} cancels the weight). The
conditional counterexample prop:conditional-counterexample-final constructs
bounded V in X_3 with P_ac(-Delta+V) 1_K(-Delta+V) = 0 on nonempty compact K,
which would refute the conclusion for nu = 3. The two open problems gate it:
prob:physical-grouped-global (line 2067) and prob:short-time-radial-compiler
(line 7036). Note the conjecture asks for AC spectrum of INFINITE multiplicity
on ALL of [0, infinity); killing it on one interval K already refutes it.

## Q2.png status

Image is 415x191 RGBA, ~6% ink coverage, several lines of text+math spanning
the full frame. Multiple enhancement passes (4x/8x/12x Lanczos+Nearest,
autocontrast, binarization, quadrant tiling) did not yield a reliable glyph-
level transcription by the orchestrator; dedicated transcription unit was
stopped by the user and will not be re-dispatched. The problem statement in
Q2.png is treated as SUPPLEMENTARY: the decisive content of the open problems
is fully specified in output/latex/operator_valued_riesz_singularity_note.tex
(Problem prob:physical-grouped-global line 2067; Problem
prob:short-time-radial-compiler line 7036; conditional counterexample line
7712). If the user wants the image transcribed later, a higher-resolution
photo would settle it instantly.

Enhanced derivatives kept for the record under settlement/synthesis/
(q2_upscaled.png, q2_bw.png, q2_left/right.png, q2_q1..q4.png,
q2_content_nearest.png, t1..t4.png).

## Literature verdict (recon unit, 25 Aug 2026)

Full report: settlement/literature/LITERATURE_RECON.md

- Simon's multidimensional L^2 conjecture is OPEN for EVERY d >= 2 as of
  2026-08-25. No proof, no disproof, no credible resolution claim anywhere
  (arXiv math.SP checked through today).
- Correction to common folklore: "Killip-Visan settled d >= 4/5" is a
  MISATTRIBUTION — their celebrated papers concern critical nonlinear NLS,
  not this conjecture. No dimension d >= 2 has a positive result of Deift-
  Killip strength. Best partial: Laptev-Naboko-Safronov (CMP 2005) AC support
  for oscillatory potentials, d >= 3 only, d = 2 explicitly left open even
  with oscillation.
- No construction anywhere puts V inside the weighted L^2 class while killing
  AC spectrum. All known negative results sit strictly outside the class:
  Wigner-von Neumann, Frank-Simon 2017 (L^q vanishing embedded eigenvalues,
  q > (d+1)/2), Bogli-Cuenin CMP 2023 (complex potentials only; Fermi golden
  rule blocks real V), Taimanov-Tsarev / Naboko-Simonov 2D Moutard examples
  (decay ~1/|x|).
- Control-theory side: NO published theorem provides one parameter-blind
  input realizing a prescribed unitary on a finite eigenspace family,
  uniformly over a dilation continuum, in small time. Liang-Boscain-Sigalotti
  (2501.12357): state-to-state chirped ensemble inversion, total time
  diverges. Chambrion-Pozzoli 2023: target-dependent controls, no unitary
  synthesis. Beauchard-Pozzoli (2410.02383): torus/Euclidean diffeomorphism
  control, not S^2, not ensemble-uniform. All assume simple spectra;
  degenerate eigenspaces (unavoidable on S^2) are untreated in the literature.
- Implication: the workspace's two open problems are genuinely open; nothing
  published closes or refutes them. A completed counterexample here would be
  the FIRST disproof-type result inside the weighted L^2 class.

## Referee synthesis #1 (orchestrator, 25 Aug 2026 ~7:25 PM)

### Radialization front (files under settlement/attack-radialization/)

Internal tension identified and RESOLVED analytically:

- MAIN_RESULT.md initially claims "likely FALSE" via a quantum-speed-limit
  floor T_Sigma >= c*tau/B.
- MAGNUS_FEASIBILITY.md (written later, section N3) shows that floor FAILS
  for phase-type tracking: the relative-phase rate demanded by the lens
  target is |tau-1)*s*|Delta_lambda|, INDEPENDENT of T, while bounded-height
  masks supply rate <= 2B for however long the mask acts. The T cancels:
  requirement becomes a HEIGHT condition h >= |tau-1)|*|Delta_lambda|/2,
  not a TIME condition. Order 1-3 Magnus leaves error O(sT rho_min) +
  O(s^2 T^2 ...) -> 0 as T->0 with NO amplitude growth. So for DIAGONAL
  (phase renormalization) targets there is NO time floor.
- Orchestrator adjudication: both are partially right. The correct split:
  (a) Phase-tracking part of the lens target (chi(s)e^{is tau A_3}|_E):
      NO Magnus/speed-limit obstruction up to order 3; only height and
      residue conditions. N3 is correct.
  (b) Population-swap part (needed by prop:broadband-transposition-criterion,
      drift-decorated transpositions): genuine per-swap floor
      T >= pi/(2 B mu) at bounded height B and matrix element mu — UNLESS
      the saturated degree-J profile basis boosts mu to O(1)-with-large-
      effective-gap via the carrier mechanism (thm:shrinking-window-carrier-lift),
      which is exactly what the note claims locally on shrinking windows.
  (c) Therefore the TRUE battlefield is: (i) can finitely many carrier blocks
      tile the FIXED interval S (partition of unity over s) — obligations
      OB1-OB3 of MAIN_RESULT; (ii) does the full-sphere leakage refocus
      uniformly across blocks given prop:dipole-unavoidable-one-over-nu-tail
      (sharp nonzero 1/nu Stark tail per pulse — signed collective
      cancellation across the block family required); (iii) does the
      multiscale-density criterion (eq:multiscale-density-no-go-condition)
      tolerate carrier-frequency->infinity excursions.
- Consequence for verdict: prob:short-time-radial-compiler is GENUINELY OPEN,
  leaning constructible for the lens instance if OB1-OB3 go through;
  the all-eta version (arbitrary gates G(s)) likely FALSE by the swap floor,
  but the program only NEEDS the lens instance + transposition currency,
  for which the carrier mechanism was built. This is sharper than either
  agent's initial read.

### Hazard front

GAME_FORMALIZATION.md confirms the orchestrator's reading: everything hinges
on the k-modulus (frequency content Lambda_j) of GENERATED bundles; source
asserts norm continuity with NO modulus (line 1961-1963); root-Zeno and
Möbius-Haar adversaries exploit arbitrary histories, not generated ones.
Ledger feedback laws previewed. MAIN_ATTEMPT/COUNTEREXAMPLE_SEARCH pending
(agent resumed with explicit proof targets).

### Numerics so far

exp1 run log: coherent-family estimates stay < 1 for all n (theory OK);
adversarial 'dir' estimator overshoots > 1 at small n (known Monte-Carlo
sup-bias, not a theory violation) and falls below 1 by n=64; gap shrinks as
n grows at fixed rho — consistent with root-of-unity collapse (kappa ->
1).
exp2/exp4 artifacts exist; SUMMARY.md pending.

### Updated decision tree

- If OB1-OB3 + signed Stark-tail cancellation close => lens inverse holds =>
  counterexample assembles => DISPROVED (nu = 3 first).
- If hazard divergence provable along generated trajectories (Lambda_j
  polynomial growth argument) => prob:physical-grouped-global solvable
  directly, WITHOUT radialization => DISPROVED.
- Both failing => the workspace's conditional disproof dies; conjecture
  survives this attack line; document sharp phase boundary instead
  (MAIN_RESULT Theorem S shape: eta-short iff eta > c(E,S) tau/B).

## Referee notes (mine, to check agent claims)

- The Haar-orbit / root-Zeno adversaries use ARBITRARY singular histories.
  Along the CONSTRUCTED trajectory each generation adds smooth cells with
  X_3 cost 2^{-j} and amplitude bounded by fixed height rho. Whether the
  radiation-vector bundles k -> x_p(k) stay uniformly continuous with a
  generation-independent modulus (giving h_j >= h_0 > 0) is THE question for
  the hazard side.
- For radialization: word is s-linear, so W_s solves i psi' = s(A_3+u(t))psi
  over T = sum t_j; requirement sup_{s in S} ||U_{A_3+u}(sT) - chi(s) U_{A_3}(s tau)|| < eps
  is tracking of free flow under time-warp r -> tau r. Magnus order-1 forces
  time-average of (A_3 + u) to equal tau A_3 mod scalars. Bounded amplitude
  Qmax gives quantum-speed-limit floor T >= pi/(2 Qmax |matrix element|) per
  swap UNLESS concurrent disjoint-cap swaps or resonant high-gaps bypass it.
  Whether the ledger sums or maximizes concurrent segments must be checked
  against the source definition of the word product and ledgers.
