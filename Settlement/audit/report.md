# ADVERSARIAL AUDIT — Theorem 6 (`settlement/attack-hazard/MAIN_ATTEMPT.md` §7, L279–417) and Corollary 7 (L389–398)

Referee role: adversarial. Every citation re-checked against
`output/latex/operator_valued_riesz_singularity_note.tex` (refs `L<n>` below refer to that file;
`MA<n>` refers to `MAIN_ATTEMPT.md`). All six assigned attack vectors were worked through,
plus five extra checks (E1–E5) that the vectors forced.

---

## 0. Verdict table

| # | Attack vector | Verdict |
|---|---------------|---------|
| 1 | Citation audit (does each cited source line say what Thm 6 needs?) | **SURVIVES** (2 cosmetic errata, no logical damage) |
| 2 | Placement-lemma frequency ratchet across sequentially placed groups | **SURVIVES** |
| 3 | Singularity persistence of the growing potential `W + (cells)` | **SURVIVES** |
| 4 | Step-5 ledger: integrated vs pointwise contraction (the orchestrator's "pointwise rescue") | **NEEDS REPAIR** — the rescue argument is *false*; the theorem's `3/4` conclusion survives under a corrected *integrated* ledger; the advertised `1/2+o(1)` strengthening does not survive as stated |
| 5 | X_3 cost additivity across disjoint shells; amplitude max-vs-sum | **SURVIVES** (with rate-level caveat G3) |
| 6 | Extra checks: quantifier order/Dini fallback, protected-test locking, small-norm stratum, Corollary-7 insertion, G1/G2/G3 dependency | **SURVIVES** |

**OVERALL VERDICT: Theorem 6 is CORRECT WITH REPAIRS.**
The assembly scheme (compactness cover -> per-window group lengths -> sequential disjoint-shell
placement -> integrated moment ledger -> cost ledger) is sound and every load-bearing citation
checks out. What does **not** survive is the *proof written in Step 5* (MA344–359): it silently
assumes a pointwise composition property that the one-window theorem does not provide, and its
error allocation `int_{I_l} err_l <= zeta/(10L)` under-counts overlapping windows by the cover
multiplicity. Both defects are repairable inside the same architecture (Repairs R1/R2 below);
after repair the delivered stage factor is exactly `3/4 + o(1)`, which is precisely what the
consumer `prop:conditional-counterexample-final` (L7712–7748) assumes at L7729–7732. The route
to `prop:conditional-counterexample-final` therefore stays fully activatable. The parenthetical
strengthening "(indeed 1/2 + o(1))" in Corollary 7 (MA393) must be withdrawn or re-derived via
Repair R3; it was never needed by the source (the source triples `3/4`-generations,
L7730–7732).

Scope disclosure: this audit verifies that Theorem 6's assembly logic correctly composes the
source's cited statements *as those statements are written*, and that the internal arithmetic is
consistent. It is not a from-scratch re-proof of the source's own lemmas
(`lem:physical-hardy`, `thm:singular-bundle-grouped-contraction`, `lem:one-step-placement`,
`rem:phase-criterion`, `prop:full-block-talbot`, …); their proofs were read and found coherent
at the level checked here (see E6 for the one soft spot, gap G3).

---

## 1. Vector 1 — Citation audit: **SURVIVES**

Checked every citation in the Theorem 6 proof (MA296–371) against the source text:

| MA cite | Claim | Source lines | Status |
|---|---|---|---|
| MA303: FSM neighbourhood open/existence | `V(k*)` open, model valid on neighbourhood | L1953–1963 (statement), L1989–1990 (proof: "Norm continuity of the data and the same resolvent estimate give the last assertion") | OK. Openness is genuinely asserted; residual `C_{rho,T} delta` uniform in phase history at L1982–1985 supports the neighbourhood mechanism |
| MA311: small-norm stratum kill | choose tau so `||x_p||<tau` mass < allocated error | L2016–2018 | OK, verbatim |
| MA312–314: spectral measures singular, compact bundle | `rem:phase-criterion` + `thm:singular-bundle-grouped-contraction` | L2022–2026 | OK, verbatim chain in the source's own proof |
| MA315: length `M_l` fixed before any model | order of quantifiers | L2042–2044 ("There is no dimension–length fixed point: M was selected ... before the finite model was introduced") | OK |
| MA320–321: Talbot closeness of M-cell blocks to `(a Id, b Id)` | `prop:full-block-talbot` applied on the model | L2035–2037 | OK |
| MA321–322: compact-output stability, reflection gap, safety enlargement | transfer of eq:singular-vector-bundle-contraction to physical outputs | L2038–2041 | OK |
| MA333–336: placement locks window means AND the global protected list | `lem:one-step-placement`, "In the same placement step include every protected fractional moment on K and every protected continuous test" | L2046–2050 | OK — this is the crucial license for Theorem 6's simultaneous locking, and it is the source's own sentence, not the agent's invention |
| MA336–338: exact phase-mean identity, pointwise in k | `int_T F_z^* F_z dm = Id` | L1066–1073 (statement), L1102–1114 (Neumann-series proof, no k-dependence used) | OK — identity holds for each fixed k; see Vector 2/E2 for why this kills the ratchet worry |
| MA340: off-window nonexpansion, never expansion | remark | L1120–1134 ("it does not supply a strict contraction away from the cell's tuning window" L1131–1133) | OK, accurately characterized |
| MA330: successive disjoint shells | prescribed inner radius | L1998 ("a prescribed inner radius"), L2000, L7734 | OK |
| MA363–365: `lem:window-cost` lifted from cells to groups | chromatic law for blocks | L1356–1389 states the law for a *depth-m cell* (L1360–1361); the block version is *asserted* by the one-window Talbot step (L2035–2037) and *assumed* by the Zeno certificate (L1765–1768) | OK as an inference, but the block-level constant `C M m |k/k* − 1|` is not literally proven anywhere — this is the document's own declared gap G3 (MA413–417). Flagged, rate-level only; see E6 |
| MA369: carriers/radii/cutoffs uncharged | `lem:scale-compatibility` | L1311–1354, esp. L1332–1334 ("None of these choices changes the reflector cost C_rho e^{-cm}") and L1351–1353 | OK |
| MA371: one amplitude bound rho | pointwise amplitude bound depending only on rho | L2006–2007; independently L7436–7438 ("pointwise amplitude is bounded by the fixed constant ..., independently of m and of its radial location") | OK |
| MA396–397: consumer places cells on successive disjoint shells | `prop:conditional-counterexample-final` | L7714 hypothesis, L7725–7733 procedure, L7733–7735 shells | OK |

Errata (cosmetic):

* **ERRATUM-1 (label).** MA302–303 cites "existence and openness: L1961–1963, L1989–1990".
  Correct content, but the openness clause is the *last assertion* of
  `lem:finite-spectral-model` whose formal statement sits at L1961–1963; fine. However MA87
  cites "L1983–1985" for `delta_j ~ eps_j/C_{rho,M}` — L1982–1985 gives the bound
  `C_{rho,T} delta` with `T = M`; the constant's `T`-dependence is exactly the `C_{rho,M}`;
  acceptable shorthand, worth a footnote.
* **ERRATUM-2 (arithmetic display).** MA356: "`1/2 + 1/10 <= 3/4 - 1/8` slack" is numerically
  true (0.6 <= 0.625) but compares the wrong objects: the `1/10` is used both as a *relative*
  per-window factor increment and as an *absolute* off-window mass term (dimension mismatch).
  Symptom of the Step-5 confusion diagnosed in Vector 4. Harmless after Repair R1.

No citation is load-bearing-false. Theorem 6 invokes only mechanisms the source itself either
proves or explicitly offers ("or a finite broadband scalar synthesis which covers K in one
generation", L2081–2082 — the source *invites* Theorem 6).

---

## 2. Vector 2 — Placement-lemma frequency ratchet: **SURVIVES**

**Attack.** `lem:one-step-placement` (L640–674) certifies eps-accurate torus means only after
the collar frequency `nu` exceeds the frequency content of the integrand divided by eps
(proof L664–674: integrands lie in `L^1(K; C(T))`, Fourier tails of `C^1` data decay like
`L/n`, Riemann–Lebesgue kills nonzero coefficients at `z = e^{i nu k}`). When group `G_l` is
placed, the current bundle incorporates `G_1..G_{l-1}`, each factor
`F = (a Id + z b H)^{-1}`, `z = e^{i nu k}`, adding modulation frequencies of size `nu`. So
Lambda grows multiplicatively, later collars explode, and — the sharpest form of the attack —
the *chromatic law* `C m |k/k* − 1| + eps` (L1765–1768) was derived for data of bounded
modulation; maybe with huge Lambda the realized width collapses and Step 3's shrinking loop
never closes.

**Why it fails to break Theorem 6.**

(a) *Existence, not bounds.* `lem:one-step-placement` guarantees **arbitrarily large**
frequencies (L650: "there are arbitrarily large real frequencies nu"). There is no upper
obstruction: whatever Lambda_l the current bundle has, a finite `nu_l > Lambda_l · (10L)/zeta`
exists. Finiteness of L makes the sequential choice possible. Nothing in the placement lemma's
hypotheses caps the modulation of the input data — measurability and denominator lower bound
`a − b > 0` suffice (L642–648, L665).

(b) *The chromatic law is insensitive to Lambda — and this is the source's own position.*
The certified half-width law `err(k) <= C M m |k/k* − 1| + eps` (L1765–1771) contains no
history term; the MAIN ATTEMPT itself isolates this as Gap G2 (MA84–93). Crucially, Theorem 6
is robust to *both* readings of G2:
   - If the chromatic law is operative, widths are `h_l = eta_l/(C M_l m_l)` as planned.
   - If the raw FSM-modulus reading were operative (`h ~ delta/Lambda`), the modulus enters
     **only through the size of the FSM neighbourhood `V(k*)`** (L1961–1963, proof L1989–1990),
     i.e. through how much Step 1/Step 3 must shrink each `I_l` *before* the group is placed.
     Since Theorem 6 plans the entire generation against one fixed bundle and needs **no uniform
     positive lower bound** on the `h_l` (compactness of K converts positivity into finiteness;
     MA307–308; the source explicitly disclaims uniformity, L2009–2010), any finite per-centre
     width still yields a finite cover. The ratchet degrades *widths*, never *existence*.
(c) *The source's own sequential construction faces the identical issue and accepts it.*
    `prop:conditional-counterexample-final` (proof L7724–7739) applies the global generation at
    stage j to a bundle already carrying stages 1..j−1 of placed cells, each with its own collar
    phases, allocating `2^{-2j}` combined placement/residual/error (L7728–7729). If the
    frequency ratchet invalidated sequential placement, the *source's* conditional proposition
    would fail first — and Theorem 6 would merely inherit the same hypothesis it is meant to
    discharge. Since Theorem 6's per-stage placement is *strictly easier* than the source's
    cross-stage iteration (one fixed bundle, finitely many groups, all planned in advance),
    validity transfers: Theorem 6 inherits legitimacy rather than debt.
(d) *Where the ratchet WOULD bite:* only in Theorem 5's effective-rate schedule (MA233–275),
    which needs summable `eps_j` against diverging `sum gamma_j h_j` — there uncontrolled width
    degradation kills the schedule, exactly as MA271–275 concedes. That is the hazard route,
    not Theorem 6.

Verdict: the ratchet attacks Route A (Theorem 5), is absorbed by compactness in Route C
(Theorem 6), and is pre-accepted by the source's own consumer. **Survives.**

---

## 3. Vector 3 — Singularity persistence: **SURVIVES**

**Claim to verify.** After placing groups on new shells, the new potential
`V' = W + (cells)` is still smooth, real, compactly supported; hence
`rem:phase-criterion` (L528–546) applies verbatim to `Theta_{V'}(k)`: trace-class difference
from `Theta_0(k)` (L537–540), no absolutely continuous subspace (L541–542, Kato–Rosenblum at
L563–566), every vector spectral measure singular (L542–543), norm continuity in k on compact
intervals (L544–545, L567). Therefore at every later window the Step-2 hypothesis ("all
associated spectral measures are singular", L2022–2023) re-arms automatically.

Checks:

* Cell smoothness/realness/support: the one-window output is "a finite group of smooth real
  scalar reciprocal cells outside that radius" (L1999), placed on prescribed disjoint shells
  (L7734); finite sums of such are smooth, real, compactly supported. No hypothesis of
  L528–546 is disturbed.
* The criterion is *per fixed V*: nothing in its proof (L548–567) uses boundedness of the
  number of shells or of prior stages; it is re-applied fresh to each `V'`.
* Atomicity (Lemma 1 of MAIN_ATTEMPT, MA97–122) is indeed **not needed** for Theorem 6's
  existence claims — confirmed: Step 2 (MA310–317) runs on
  `thm:singular-bundle-grouped-contraction`, whose hypothesis is weak compactness +
  singularity of the measure family (L1634–1637), supplied by `rem:phase-criterion` +
  norm continuity + compactness of K; the length `M_l` then exists by Dini/monotonicity
  (L1722–1728). Lemma 1/2/3 (MA97–194) enter only through MA316–317's optional "effective
  `M_l = O(log n)`" remark. Existence of the cover, the contraction factors, and all three
  conclusions of Theorem 6 are independent of G1. Confirmed as the agent claims.

One caution recorded: singularity of the *ideal* bundle is used before the finite model is
introduced (L2031–2034); the model approximation preserves the contraction estimate up to
`C_{rho,T} delta` (L1982–1985) but the *singularity* itself is only a device to obtain `M`;
nothing downstream needs the approximating model's measures to be singular. Consistent.

Verdict: **Survives.**

---

## 4. Vector 4 — Integrated vs pointwise ledger (Step 5): **NEEDS REPAIR** (theorem survives, proof does not)

### 4.1 The orchestrator's rescue argument, stated precisely

MA344–356 reasons: "on each `I_l`, the realized contraction is `<= 1/2 + err_l` ...; on K off
the windows, each group contributes only nonexpansion ... Summing, `int_K w_1^beta <=
(1/2 + zeta/(10L)) sum_l int_{I_l} w_0^beta + int_{K \setminus cup I_l} w_0^beta + zeta/10`."
The prompt's proposed rescue sharpens this to a pointwise claim: for each k,
`w_final^beta(k) <= prod_l factor_l(k) · w_0^beta(k)` with `factor_l(k) <= 1/2 + err_l` if
`k in I_l` and `<= 1 + err_l` otherwise.

### 4.2 The rescue is FALSE. Three independent obstructions.

**(O1) `w^beta` is not multiplicative under composition.** The density transforms by
composition of linear-fractional (Moebius) factors on the *amplitudes*; even in the ideal
scalar case `x -> (A_M H + conj(A_M) Id)^{-1} x` (collapsed recursion, L1732–1738), the new
density is `(new amplitude)^2`, and `(fg)^2 != f^2 g^2`. There is no product formula for
`w^beta` along a deterministic path — the `1/2` is produced by *averaging over the phase torus*
(`Q_r(nu)` Poisson contraction, L1683–1694), not by a pointwise multiplier. Any "pointwise
factor" statement confuses the averaged object with a sample.

**(O2) The one-window contraction is integrated, and only on its own window, and only for the
current bundle.** The deliverable (L2002–2003) is:
`sum of targeted beta-moments on I contracted by <= 1/2 up to zeta` — an inequality between two
numbers `int_I w_after^beta` and `int_I w_before^beta`. The proof path
(singularity -> group length -> torus average, L2022–2044) passes through torus means and
placement; **no pointwise-in-k statement is ever produced**, and `rem:physical-hardy-meaning`
explicitly warns the off-window behaviour is mere nonexpansion *of torus means* (L1123–1133),
not a pointwise bound. A pointwise factor `<= 1/2` on `I_l` is simply not an output of the
machinery.

**(O3) The source contains a counterexample to exactly the needed composition.**
`prop:local-contraction-without-coverage-is-insufficient` (L1391–1404, cited region
L1397–1403): a sequence of cells, each *exactly* nonexpansive off its own window `I_j` and
contractive on it, with arbitrarily small cost, yet `inf_j int_K w_j^beta dk > 0`. Whatever the
fine print, this proposition is the source's own certification that **one-window contractions
do not compose pointwise into a global contraction** without a coverage argument. Theorem 6's
cover *is* the missing coverage argument — but then the ledger must be an integrated,
cover-aware ledger, not a pointwise product.

### 4.3 What IS true: the corrected integrated ledger (Repair R1)

Grant for each l, from the one-window proposition applied to the *current* bundle on `I_l`:

$$ \int_{I_l} w_l^\beta \le (\tfrac12 + \epsilon_l)\,\mu(I_l), \qquad \mu(I_l) := \int_{I_l} w_{l-1}^\beta ,$$

and off-window nonexpansion up to epsilon:
$$ \int_{K\setminus I_l} w_l^\beta \le \int_{K\setminus I_l} w_{l-1}^\beta + \epsilon'_l .$$

Both follow from L2002–2005 applied with the *global* protected list included in the same
placement step (licensed by L2046–2054: the placement locks the window means and every
protected quantity on all of K simultaneously). Key structural facts:

1. **Monotonicity of the targeted list:** the targeted moments contracted at stage l+1 on
   `I_{l+1}` are among the protected (nonexpansive) items of stage l — they are declared
   witnesses on K. Hence `w_l^\beta` dominates `w_{l-1}^\beta` only up to `epsilon'`, never
   expands materially, and stage l+1 contracts the *current* mass on its own window.
2. **Overlap handling by superadditivity (upper side):** since `t^beta` is subadditive and the
   windows may overlap, the only safe upper bound for the initial mass seen by the cover is
   $$ \sum_l \mu(I_l) \le \bar R \int_K w_0^\beta, \qquad \bar R := \sup_k \#\{l : k \in I_l\} $$
   (cover multiplicity). Overlaps therefore **over-count initial mass**, never contractions.
3. **Corrected ledger.** Iterating fact 1 window by window and summing:

$$ \int_K w_L^\beta \;\le\; \Big(\tfrac12 + \epsilon\Big)\sum_l \mu(I_l) \;+\; \sum_{l,L\text{-terms}} \epsilon'_l \;\le\; \Big(\tfrac12+\epsilon\Big)\,\bar R \int_K w_0^\beta \;+\; \epsilon_{\rm tot} .$$

With a **multiplicity-1 cover** this yields factor `1/2 + o(1)`; for general covers it yields
`(1/2+o(1)) \bar R`.

### 4.4 Why the THEOREM still stands at `3/4` (two repairs)

**Repair R1 (partition-of-unity / disjointification — preferred).** Replace the cover
`{I_l}` by a disjointized refinement: let `{J_s}` be the connected components of the atoms of
the Boolean algebra generated by `{I_l}` (finitely many intervals, pairwise disjoint), assign
each `J_s` to one `l(s)` with `J_s ⊆ I_{l(s)}`, and declare `J_s` the tuning window of a
*re-tuned* copy of `G_{l(s)}`. Re-running Step 2–4 with centres/lengths adapted to the `J_s`
(the one-window proposition allows any prescribed window centre and inner radius; L1998–2000)
gives a **pairwise-disjoint** cover with `\bar R = 1`, hence

$$ \int_K w_L^\beta \le \big(\tfrac12 + \epsilon\big) \int_K w_0^\beta + \epsilon_{\rm tot}. $$

Choosing `\epsilon \le 1/4` and `\epsilon_{\rm tot} \le \zeta/4` (normalize
`\int_K w_0^\beta = 1`; the inequalities are homogeneous apart from additive errors, which are
allocated after normalization) delivers **exactly the stated `3/4 + zeta`**. All other steps
of the proof are untouched: the same groups, the same shells, the same placement, only the
bookkeeping windows are refined. Cost unchanged (same cells).

**Repair R2 (accept overlap accounting, keep the original cover).** Keep `{I_l}` as chosen and
pay the multiplicity: allocate `\epsilon_l = \zeta/(10 L^2)` per window (not
`\zeta/(10L)`) so that `\sum_l \sum_{j \ge l} \epsilon`-type accumulated placement errors stay
`O(\zeta/L)`; then the delivered factor is `(1/2 + o(1)) \bar R`. This satisfies the theorem's
`3/4` conclusion whenever `\bar R \le 1` — i.e. it reduces to R1's hypothesis — and otherwise
must be paired with:

**Repair R3 (thinning + repetition — salvages the `1/2`-per-two-generations claim).** Any
finite interval cover of `K ⊂ ℝ` admits a subcover of multiplicity `\bar R \le 2` (greedy
left-to-right thinning). Two successive generations then give
`(1/2+o(1))^2 · 2 = 1/2 + o(1) \le 3/4`, and three (as the source already schedules,
L7730–7732) give margin to spare. Under R3 the literal Corollary-7 parenthetical
"(indeed 1/2 + o(1))" (MA393) is recovered *per pair of generations*, not per single
generation.

### 4.5 Consequences for the downstream chain

* The consumer `prop:conditional-counterexample-final` assumes at L7729–7730: "The stage
  contracts each of the first j fractional moments by `3/4 + o(1)`", and triples generations
  to beat 1/2 (L7730–7732). The repaired Theorem 6 delivers **exactly** `3/4 + o(1)`. The
  chain is not merely salvageable; it is unchanged.
* What dies is only MA353's displayed `<= (3/4) int_K w_0^beta` *derivation* and the
  MA393 "indeed 1/2+o(1)" gloss. The theorem statement (MA289–290: factor at most
  `3/4 + zeta`) survives intact under R1.

Verdict: **NEEDS REPAIR** (proof-level), theorem **survives** at its stated `3/4 + zeta`.

---

## 5. Vector 5 — Cost and amplitude across disjoint shells: **SURVIVES**

* **Amplitude: max, not sum — verified.** Each cell carries a pointwise amplitude bound
  depending only on rho (L2006–2007; L7436–7438: independent of m *and of radial location*).
  Cells on pairwise disjoint shells coexist; the pointwise supremum of finitely many functions
  each bounded by `A(rho)` is bounded by `A(rho)`. One bound (MA293–294, MA371). Correct.
* **X_3 additivity: verified, with the right mechanism.** The cost functional is quadratic in
  the mask profile with per-cell contributions `\|w\|_2^2/T`-type (cf. L7398–7402) plus the
  weak-mask part, which `lem:scale-compatibility` makes `< epsilon` *without touching the
  reflector cost* (L1332–1334). Disjoint radial supports make cross terms vanish by support
  orthogonality (`\int (sum_l w_l)^2 = sum_l \|w_l\|^2` when supports are disjoint), so the
  total cost is the **sum** of per-cell costs — additive across shells, exactly as
  MA361–363 exploits: choose common depth m with `L M_max C_rho e^{-cm} <= zeta/2`, possible
  because `L, M_max` became fixed finite numbers in Steps 1–2. The count `N_m <= C_K A_rho m
  zeta^{-1/beta}` of `lem:window-cost` (L1374–1375) is replaced by the constant `L` — the
  entire point of the compactness cover. No cross-term exists in any of the source's cost
  floors (L7258–7273 are per-cell lower bounds on disjointly supported profiles).
* **Consistency with the consumer's schedule.** The `2^{-2j}` geometric schedule lives in the
  *consumer's* proof (L7728–7737: allocate `2^{-2j}` at stage j, sum `\sum_j 2^{-2j} < inf`),
  not in Theorem 6; Theorem 6 only owes `<= zeta` per generation, which Step 6 delivers. The
  inheritance is clean: stage-j budget `zeta_j = 2^{-2j}` feeds Theorem 6 with `zeta =
  2^{-2j}`, and disjointness of shells *across* stages (L7734) keeps the amplitude bound a
  running maximum and the total cost the convergent series (eq:counterexample-X3-cost,
  L7736–7739).
* **Residual caveat (rate-level, = G3).** The per-*group* chromatic error constant
  `C M_l m_l |k/k* − 1|` used to size the windows (and hence how much of K each window eats,
  hence indirectly the required depths) is asserted by the one-window Talbot step (L2035–2037)
  and by the Zeno certificate's working assumption (L1765–1768), but `lem:window-cost`
  literally proves only the single-cell law (L1360–1361). Since Theorem 6 shrinks windows
  *after* fixing `M_l, m_l` (MA324–326), any finite constant closes the existence argument;
  only quantitative widths depend on it. Flagged as the document's own gap G3 (MA413–417);
  does not affect verdicts here.

Verdict: **Survives** (G3 noted).

---

## 6. Additional checks forced by the above (E1–E5)

* **E1 (quantifier order / no hidden circularity).** Step 2 fixes `M_l` from the infinite-
  dimensional singular bundle *before* the FSM model exists; the source certifies this exact
  ordering (L2042–2044). The FSM model is then taken with recursion length `T = M_l`
  (L2031–2034). Depth `m` is chosen last (L2056–2064) following the already-fixed M — no
  dimension–length fixed point. Matches MA310–326. OK. Moreover, if G1 (atomicity) fails, Step
  2 falls back to Dini compactness (L1722–1728) — existence without rates; Theorem 6 needs no
  rate. G1 is genuinely optional for this theorem (contra its prominence in the executive
  summary, MA29–32, MA116–122).
* **E2 (protected continuous tests).** A protected test changes by `<= zeta` requires more than
  the Hardy nonexpansion (which covers fractional moments): it needs the *oscillatory* part
  `psi(W_z − W) -> 0` in integral, i.e. `lem:one-step-placement`'s second output
  (L656–661, proof L666–673). That lemma requires the test integrands to be bounded measurable
  and the entries of `W_z − W` in `L^1` — satisfied because the composed bundle stays smooth on
  K (real-analytic factors with denominators `>= a − b = e^{-rho}`, cf. MA61–63) and psi is
  continuous on compact K. The locking happens in the same placement step as the window mean
  (source's own instruction, L2046–2050), so **no second frequency is needed** and no conflict
  arises between the window-lock nu and the test-lock nu. OK.
* **E3 (small-norm stratum across groups).** Each window kills its own `||x_p|| < tau_l`
  stratum by allocated error (L2016–2018); after earlier groups the norms have changed, but
  the *current* bundle's small-norm set is handled afresh at each l with its own tau_l and its
  share of `zeta/(10 L^2)` (post-R1/R2 allocation). Summing L such strata keeps the total
  within budget. OK.
* **E4 (Corollary 7 insertion).** Hypothesis of the consumer: Problem
  `prob:physical-grouped-global` "holds at every finite stage" (L7714). Theorem 6 (repaired)
  *is* that problem solved for one fixed state (compare conclusions MA289–294 with
  L2070–2073). Stage-j application to the first j probes/witnesses/tests with budget
  `2^{-2j}`: the protected list is finite at each stage, the placement locks all of it
  (L2046–2054), the dovetail bookkeeping (`eq:dovetail-nonexpand` L782,
  `eq:dovetail-contract` L783) receives exactly the `3/4 + o(1)` factor it consumes after
  tripling (L7730–7732). Shell assignment and amplitude/cost ledgers as in Vector 5. The
  final transfer to the whole-space operator (L7741–7747) is the source's own machinery,
  untouched by Theorem 6. Insertion valid.
* **E5 (the source's own obstruction does not preempt the bypass).** The anxiety at
  L2077–2079 ("positive window widths not presently known to have a finite-cover lower bound")
  targets *uniformity across states/generations*. Theorem 6 requests no such uniformity —
  compactness of the single fixed K converts pointwise-positive widths into a finite cover
  (MA373–381), and the source explicitly lists "a finite broadband scalar synthesis which
  covers K in one generation" as an acceptable equivalent (L2080–2082). The bypass is
  licensed by the source, not smuggled past it.
* **E6 (soft spot retained).** Gap G3 (block-level chromatic constant) and the fine print of
  `prop:full-block-talbot` on the model are the only places where a determined skeptic could
  still demand quantitative upgrades. Neither affects the existence-level truth of Theorem 6;
  both affect only how small the windows (hence how many) must be.

---

## 7. Overall verdict and required repairs

**Theorem 6 (MAIN_ATTEMPT.md §7): CORRECT WITH REPAIRS.**

* Broken component: **Step 5's proof only** (MA344–359). Its pointwise-composition rescue is
  refuted by (O1)–(O3) above, and its error allocation ignores cover multiplicity. The
  displayed inequality MA351–354 is not established by the argument given.
* Required repairs:
  * **R1 (mandatory, minimal):** replace Step 5 by the integrated ledger of §4.3 and
    disjointify the cover (partition-of-unity refinement, re-tuned copies on the atoms
    `J_s`). Delivers `3/4 + zeta` exactly as stated; no other step changes.
  * **R2 (mandatory if R1's re-tuning is not performed):** allocate
    `epsilon_l = zeta/(10 L^2)` per window and carry the multiplicity factor `\bar R` honestly.
  * **R3 (optional, restores the `1/2` rhetoric):** thin the cover to multiplicity `<= 2` and
    run two generations; or drop the parenthetical "(indeed 1/2 + o(1))" from Corollary 7
    (recommended — nothing downstream uses it).
  * **Editorial:** fix ERRATUM-2's slack arithmetic line (MA356); annotate G3 in Step 6.
* **Salvageability of the breakthrough route:** fully preserved. The repaired theorem
  activates `prop:conditional-counterexample-final` (L7712–7748) verbatim, because that
  proposition consumes a per-stage factor `3/4 + o(1)` (L7729–7732) — precisely the repaired
  output — together with per-stage budget `2^{-2j}`, successive disjoint shells, one amplitude
  bound, and summable X_3 (L7733–7739), all of which survive audit. Whether Simon's
  multidimensional L^2 conjecture is thereby disproved remains conditional on exactly what the
  source declares conditional (L7714, and the abstract's framing L260–262): the condition is
  now discharged *locally* (one generation, one state) by the repaired Theorem 6, and the
  remaining content is the iteration/dovetail machinery of the source itself, which this audit
  did not put in doubt.

— Adversarial referee report ends.
