# AUDIT REPORT — Theorem 6 of `settlement/attack-hazard/MAIN_ATTEMPT.md`

**Referee:** adversarial red-team audit.
**Date:** 2026-08-25.
**Sources audited (live line numbers):**
- `output/latex/operator_valued_riesz_singularity_note.tex` (the Note),
- `output/latex/fixed_potential_riesz_counterexample.tex` (external zonal Talbot layer),
- `output/latex/simon_fcen_new_attack_program.tex` (companion programme: definitions of $X_d$, Simon's conjecture),
- `settlement/attack-hazard/MAIN_ATTEMPT.md` (Theorem 6 and its proof).

**Claim under audit:** Theorem 6 (MAIN_ATTEMPT §7) assembles finitely many applications of
`prop:physical-grouped-one-window` (Note L1993–2065) on a compactness-supplied finite cover of $K$,
groups placed on pairwise disjoint radial shells, to prove `prob:physical-grouped-global`
(Note L2067–2083), thereby activating `prop:conditional-counterexample-final` (Note L7712–7748)
and disproving Simon's multidimensional $L^2$ conjecture *conditionally on the Note's proved layer*.

---

## A. SCOPE OF PROTECTION — **PASS** (one minor note)

**Question.** Does item 2 of the one-window proposition protect *arbitrary* finitely many other
probes' $\beta$-moments on **all of $K$** *simultaneously* with item 1's contraction on $I$, or is
protection elsewhere merely heuristic?

**Findings.**

1. The protection ingredient is `lem:physical-hardy` (Note L1058–1118). Its proof
   (L1088–1118) uses **only** the flux identity $A^*A-B^*B=\mathrm{Id}$ (L1062), the factorization
   $F_z=A^{-1}(\mathrm{Id}-zT)^{-1}$ (L1100), termwise integration of the Neumann series
   (L1108–1113), and operator concavity (L1115–1117). **No energy localization is used anywhere.**
   The identity $\int_\T F_z^*F_z\,\dd m=\mathrm{Id}$ (L1071) therefore holds **pointwise in $k$**
   for the *actual* scattering pair $(A(k),B(k))$ of the realized potential, at every $k$, because
   the flux identity is a structural consequence of unitarity/current conservation of the reciprocal
   shell pair (cf. the exact radial composition `eq:exact-jost-shell-update-final`, L7693–7698), not
   a consequence of the window tuning. Detuning away from $I$ degrades the pair's distance to the
   boost $(a\,\mathrm{Id},b\,\mathrm{Id})$ — i.e., the *contraction strength* — but **not** the validity
   of the Hardy nonexpansion. This is exactly the reading announced in
   `rem:physical-hardy-meaning` (L1120–1134): "an outer physical cell may behave arbitrarily away
   from its tuning window: after a rapid scalar collar phase is averaged, every protected quadratic
   density is preserved and every protected fractional moment is nonexpansive … by itself it does not
   supply a strict contraction away from the cell's tuning window."
2. Deterministic realization of the torus means is `lem:one-step-placement` (Note L641–674):
   for **finitely many** test functionals and one $\epsilon>0$ there are arbitrarily large
   frequencies $\nu$ realizing **all** the inequalities simultaneously (L649–661); the proof
   approximates the integrands in $L^1(K;C(\T))$ by trigonometric polynomials and takes the **finite
   maximum of the frequency thresholds** (L672–673). Growing the locked list enlarges the threshold
   but costs nothing else, and $\nu$ may be taken arbitrarily large. The successive-list version with
   undisturbed earlier inequalities is `lem:uniform-torus-placement`
   (`fixed_potential_riesz_counterexample.tex` L228–255, esp. L239–242).
3. **Collar-frequency crowding: none.** Free collars realize $z=e^{i\vartheta(k)}$ with
   $\inf_K|\vartheta'|$ arbitrarily large at no charged cost and no amplitude cost; the carrier is
   rechosen afterwards and the induced error absorbed (`fixed_potential…tex` L129–132, L212–216;
   `lem:scale-compatibility` Note L1312–1354 orders the scales so the carrier is chosen after the
   masks). Hence arbitrarily growing frequency lists across stages are admissible at no $X_3$ or
   amplitude cost. (The associated Lipschitz ratchet $\Lambda_{j+1}\ge c\Lambda_j/\eps_{j+1}$,
   MAIN_ATTEMPT §1, degrades *smoothness*, not feasibility.)
4. **Simultaneity with item 1:** in the one-window proof the placement step explicitly includes
   "every protected fractional moment on $K$ and every protected continuous test" **in the same
   placement step** as the targeted integrals on $I$ (Note L2046–2054). Because one $\nu$ locks all
   finitely many functionals (point 2), there is no competition between the window-$I$ accuracy and
   the global protection accuracy beyond the pre-allocated split of $\zeta$.
5. Error bookkeeping per protected functional: placement error (pre-allocated share of $\zeta$),
   plus outgoing-buffer/Galerkin residuals, which are **uniform on $K$**
   (`prop:explicit-buffer-stability` L1191–1209, the bound `eq:explicit-buffer-resolvent` is a sup
   over $k\in K$, and the spectral-density version is scaled by $\|f\|^2$, L1208–1209). Both error
   classes are budgeted per group ($O(\zeta/L)$) and per stage ($2^{-2j}$ in the assembly), so the
   per-functional error is independent of the numbers of groups and stages given the finite lists.

**Minor note (recorded, non-blocking).** The exactness of the flux identity for the *realized*
(smooth, compactly supported) cell pair at every $k$ is used as a structural fact of the reciprocal
Jost formalism; the Note proves it for the model pair and uses the stability lemmas to transfer.
A referee of record should cite the radial-composition identity (L7691–7698) and the construction of
the cells as the locus where exactness is inherited. This is a provenance note, not a gap.

## B. OFF-WINDOW BEHAVIOR OF PHYSICAL CELLS — **PASS**

**Mechanism located precisely.** Protection on all of $K$ does **not** proceed through the
$(a,b)$-closeness (which is certified only on the finite spectral model / window $I$;
`prop:full-block-talbot` L1254–1266 and its invocation at L2034–2037). It proceeds through:

- the **exact** Hardy identity $\int_\T F_z^*F_z\,dm=\mathrm{Id}$, valid at every $k$ for the true
  pair (see A);
- deterministic placement matching the $e^{i\nu k}$-weighted integrals to torus means on **all of
  $K$** (`lem:one-step-placement`; invoked globally at L2046–2050);
- truncation residuals uniform in $k\in K$ (`prop:explicit-buffer-stability`).

**Error terms.** Off its window a group contributes (i) placement error $\to$ pre-allocated
$\eps$; (ii) buffer/Schur/Galerkin residuals $\to$ uniform-on-$K$ bounds, budgeted in the stage
ledger; (iii) **no** chromatically growing term — the chromatic law
$C_{K,\mathfrak C,\rho}m|k/k_\star-1|$ bounds the *distance to the boost*, i.e. the loss of
contraction strength, not a violation of nonexpansion (consistent with the commented cell statement,
`eq:one-window-residual` L7422–7428, and its derivation by differentiating the finite product,
L7471–7473).

**Independence of group/stage counts.** Yes: each functional enters each group's finite lock list
with a pre-allocated share; thresholds are finite maxima; residual bounds do not multiply with list
size (normalized probes; L1208–1209). Cross-talk between groups is only through the placement
errors already allocated ($\sum_{l'}\eps_{l'}\le\zeta/10$ type allocations in MAIN_ATTEMPT Step 4–5).

## C. WIDTH POSITIVITY vs COST — **PASS**

From the live statement: item 3 asserts "$X_3$ cost at most $\zeta$" **for the given $\zeta$**, and
$h>0$ is asserted in the same breath as item 1's error $\zeta$ (L1998–2008); the closing paragraph
chooses depth $m$ *after* $M$ is fixed, with reflector cost $MC_\rho e^{-cm}\to0$ (L2056–2059), and
`lem:scale-compatibility` meets the finite requests without touching the reflector cost
(L1332–1334). Nothing in the live proof forces $\zeta$ to shrink with $h$: the depth $m$ is chosen
against the *fixed* $M$ and the requested $\zeta$; shrinking $h$ only shrinks the window (Step 1 of
Theorem 6 anticipates this by keeping the cover adjustable). **Crucially, there is no live proved
chromatic-certificate theorem at all**: the only occurrences of the chromatic law in live text are
(i) a *hypothesis* inside `lem:window-cost` ("Suppose a depth-$m$ cell **has** chromatic error…",
L1360–1362) and (ii) the commented-out `\iffalse` block (`prop:one-window-cell`,
L7411–7481, in particular L7425–7427). See G3 under E/F below for the consequences.

**Thread C (follow-up as instructed): no proved result forces widths to shrink across generations.**
- `prop:no-uniform-chromatic-modulus` (L1420–1460) — **proved**; obstructs *dimension-free/uniform*
  width bounds over adversarial phase families; does not bind one fixed planned bundle.
- `prop:grouped-root-zeno` (L1741–1817) — **proved**; its summable-hazard conclusion
  (L1774–1778) is *conditional on certification through the black-box chromatic law*
  (L1764–1771) **and** on adversarial bundles ($N_j=e^{j^2}$ roots of unity). For the *fixed*
  bundle of the one-shot cover, `thm:singular-bundle-grouped-contraction` yields a **finite** $M$
  per closed window (Dini compactness, L1722–1728), so root-Zeno never engages.
- `prop:mobius-orbit-haar-obstruction` (L1819–1951) — **proved**; kills uniformity of $M$ over
  *prior ideal scalar histories*; the sequential scheme re-certifies each updated state from
  scratch (see D), so it does not bind.
- `prop:coverage-obstruction` (L1391–1418) — **proved**; shows summable total widths kill the
  *adaptive/hazard* route; the one-shot cover covers $K$ completely and does not iterate widths.
- All remaining width-anxiety language (`prob:physical-grouped-global` L2077–2079;
  `cor:exact-hazard-bottleneck` L2148–2158; abstract L74–81, L109–110) is diagnostic, not proved
  obstruction. **Conclusion: Theorem 6's compactness move is not contradicted by any proved
  result in the Note.**

## D. SEQUENTIAL COMPOSITION — **PASS** (with effectivity note)

**(i) Re-certification of singularity.** After placing $G_1,\dots,G_{l-1}$ the state is a new
smooth, compactly supported, real partial potential $W'$ (finite sum). `rem:phase-criterion`
(L528–568) applies verbatim: stationary representation with smooth on-shell kernel
(L555–561) $\Rightarrow$ $\Theta_{W'}-\Theta_0\in\mathfrak S_1$ (L536–540); free phase pure-point
(L563–564); Kato–Rosenblum (L564–566) $\Rightarrow$ every vector spectral measure singular;
norm-continuity in $k$ on compacts (L566–567). This is the abstract claim of Note lines 64–67,
proved at L548–568. **Re-certification holds at every stage.**

**(ii) Compact bundle / $\tau$-stratum.** The updated pairs
$(\Theta_{W'}(k),x_p(k)/\|x_p(k)\|)$ are norm-continuous in $k$ (both factors are), hence form a
compact bundle on each closed stratum $\{\|x_p(k)\|\ge\tau\}$; the small-stratum is disposed of by
exact Hardy nonexpansion (L2016–2018, L2027–2029). `thm:singular-bundle-grouped-contraction`
(L1632–1739) then fixes a **finite** $M_l$ per closed window before any model is introduced
(L2022–2026, order of quantifiers L2042–2044). Re-applies at every stage.

**(iii) Non-revocation.** Later groups affect an earlier window's realized contraction only through
their placement errors and uniform residuals (see A/B): they are phase-mean-nonexpansive on $K$ up
to $\eps$, hence "do not revoke earlier certificates; they merely fail to improve them"
(MAIN_ATTEMPT Step 4). The ledger in Step 5 charges exactly these shares.

**Effectivity note.** The $M_l$ come from Dini's theorem: finite but with no rate (unless one adds
MAIN_ATTEMPT Lemmas 1–3, which need Gap G1). Existence suffices for Theorem 6 and for the assembly
(each stage's depth $m$ is chosen after the finite $M_{\max}$, L361–364 of MAIN_ATTEMPT); only the
*hazard route* (Theorems 4–5 of MAIN_ATTEMPT) needs rates. Not a gap for Theorem 6.

## E. DOVETAIL FIT — **GAP (moderate; repairable)**

**Arithmetic.** $(3/4)^3=27/64=0.421875<1/2$. ✓ (Note L7731–7732.) Three generations' errors are
allocated into the stage budget $2^{-2j}$ (L7728–7729), which is summable, and Theorem 6 accepts any
prescribed $\zeta>0$, so the per-generation error shares close. ✓

**Delivery of `eq:dovetail-contract`.** Here there is a genuine mismatch, which is the substance
of item H below: `thm:scalar-dovetail` (L771–837) requires, at each stage,
$I_{\tau(j),j}\le\tfrac12 I_{\tau(j),j-1}+\eps_j$ **for the single scheduled probe**
(`eq:dovetail-contract`, L783) *and* $I_{p,j}\le I_{p,j-1}+\eps_j$ for all $p\le j$
(`eq:dovetail-nonexpand`, L782). Theorem 6 as proved delivers a **sum-level** contraction
("the total targeted beta-moment on $K$ contracts by $3/4+\zeta$", MAIN_ATTEMPT item 1; likewise
the one-window proposition contracts "*the sum* of the targeted $\beta$-fractional moments",
L2002–2003). Sum-level contraction does **not** imply the scheduled probe's factor $1/2$: e.g.
$(I_\tau,I_{\text{rest}})=(10,90)\to(9,33)$ satisfies total $99\le(27/64)\cdot100$ while
$I_\tau$ shrinks only by factor $0.9$.

**Repair (concrete, no new inputs).** Either (a) run the entire finite generation once per probe
(finitely many extra groups on fresh disjoint shells; per-generation budget subdivided; the
protection mechanism of A/B keeps earlier probes' certificates within their shares), yielding
literal per-probe $3/4$; or (b) replace the dovetail by a *total-moment* variant: every stage
triples a generation contracting $\sum_{p\le j}I_p$ by $27/64$, whence every $I_{p,N}\le
(27/64)^{N-p}I_{p,p}+\sum\eps\to0$, which suffices verbatim for the witness/singularity part of
`thm:scalar-dovetail` (its proof, L804–836, only needs each $I_{p,j(p,q)}$ small and the moments
Cauchy). Both repairs stay entirely within already-proved components.

`eq:dovetail-nonexpand` **is** delivered by the protected lists (item 2 up to $\eps_j$; the
assembly includes the first $j$ probes in the preservation list, L7726–7728).

## F. HIDDEN RADIALIZATION DEPENDENCE — **PASS** (one presentational caveat)

Complete ingredient list of `prop:physical-grouped-one-window` and its transitive closure:

| Ingredient | Location | Content | Lens/radialization dependence |
|---|---|---|---|
| `rem:phase-criterion` | L528–568 | stationary repn, smooth kernel, trace class, Kato–Rosenblum | none |
| `thm:strong-barrier` / `cor:strong-bundle` | L466–526 | Poisson boundary, Dini | none |
| `thm:singular-bundle-grouped-contraction` | L1632–1739 | SU(1,1) products, Jensen drift, Azuma, Dini | none |
| `lem:physical-hardy` (+ meaning remark) | L1058–1134 | Neumann series identity | none |
| `lem:finite-spectral-model` | L1953–1991 | spectral partition, resolvent identities | none |
| `prop:full-block-talbot` | L1254–1278 | product-Laplacian identity `eq:product-laplacian` (L1234–1237) + "same Duhamel comparison as in the zonal proof"; external zonal Talbot = `prop:zonal-talbot-factor` (`fixed_potential…tex` L546–591: Duhamel vs flat circle Laplacian, $\cot\theta\,L^2$ estimate) and `prop:talbot-riesz-concentration` (ibid. L593–647: Riemann–Lebesgue + Chernoff) | none |
| `lem:compact-output-stability` | L866–917 | algebra of the residual bound | none |
| `lem:reflection-gap` | L919–934 | factorization $(\mathrm{Id}+zHC)A$ | none |
| `lem:schur-stability`, `prop:explicit-buffer-stability` | L1156–1224 | Schur complement, elliptic/Fredholm | none |
| `lem:bounded-reflector` | L1281–1309 | 1D transfer-matrix Cartan decomposition | none |
| `lem:scale-compatibility`, `lem:window-cost` | L1312–1389 | scale ordering, bookkeeping | none |
| `lem:one-step-placement` | L641–674 | Fourier/Riemann–Lebesgue | none |

String search over the Note confirms that "lens", the outward time budget
(`prop:outward-angular-time-budget`, L6249–6270), the angular/frame compilers
(`thm:sphere-finite-frame-compiler` L6190ff, `prop:uniform-adiabatic-lens-compilation` L5728ff),
and `prob:short-time-radial-compiler` (L7036–7121) occur **only** in the swap/lens/carrier/slab
sections and the decision section; **none is cited by the one-window chain**. Consistently, the
truth ledger (L194–262) marks exactly these one-window ingredients \proved and isolates the
radialization problem as \conditional (L257–262). The outward budget is not merely unused but
*harmless* here: the Talbot flights consume angular kinetic time $O(\sum_t L_t^{-2})=o(1)$ and the
collars sit at radii contributing $\le 1/R_-\to0$, well inside $\int_R^\infty r^{-2}\dd r=1/R$.

**Presentational caveat (not circularity).** The full-block *cell assembly* (weak-slab realization
of arbitrary finite-dimensional masks, collar phases, reflection gap for the assembled cell) is
carried in live text only implicitly: `prop:one-window-cell` and `prop:local-adapted-squeeze`, which
contain the explicit assembly, sit inside the `\iffalse … \fi` block (L7411–7687). The live
ingredients (`prop:full-block-talbot` + stability lemmas + `lem:bounded-reflector`) suffice and the
zonal prototype is published in `fixed_potential_riesz_counterexample.tex`
(`prop:scalar-reciprocal-riesz-cell`, L111–220, with its own scale separation
`eq:riesz-cell-scale-separation` L182–186), but the non-zonal cell statement should be reinstated
as live text. Recorded under G3 below as part of the formalization debt.

## G. THE ASSEMBLY PROOF (L7712–7748) — **PASS** (inherits item H's gap in its hypothesis)

Checked componentwise:
- **Dense-probe selection:** countable dense set of smooth compact probes exists; triangular
  schedule $\tau(j)$ from L764–769 visits each probe infinitely often. ✓
- **Strong-resolvent/wave-operator transfer:** the dovetail produces exterior measures;
  strong resolvent identification of the summed-potential measures (standard monotone/strong
  convergence of the staged potentials — the shells are disjoint with summable $X_3$ norms, so
  $V_n\to V$ in $X_3\cap L^\infty_{\rm loc}$ and the truncated operators converge in strong
  resolvent, cf. the companion's audited truncation lemma, `simon_fcen…tex` L346–387);
  changing the operator inside a fixed ball and recoupling the exterior Dirichlet boundary are
  compactly supported short-range perturbations, so completeness of the local wave operators
  transfers the vanishing of $P_{\rm ac}\mathbf 1_K$ from the exterior Dirichlet operator to the
  whole-space operator (L7741–7748). Wave operators intertwise functional calculus, so
  $P_{\rm ac}(H)\mathbf 1_K(H)=0$ passes through. ✓
- **`cor:dense-probes` logic (L839–853):** kernel of $P_{\rm ac}(H)\mathbf 1_K(H)$ is a closed
  subspace containing a dense set. ✓
- **$X_3$ summability:** `eq:counterexample-X3-cost` (L7736–7739) $\sum_j 2^{-2j}<\infty$, valid
  since Theorem 6 meets any prescribed per-stage budget. Amplitudes: one uniform bound
  (`lem:bounded-reflector` L1290–1293: no copy exceeds the fixed bump height; weak-slab amplitudes
  $T^{-1}\|w\|_\infty\to0$), disjoint shells make the pointwise supremum a maximum. ✓
- **Contradiction with Simon's conjecture:** the companion programme fixes the statement:
  $m_{\rm ac}(E;H)=\infty$ for a.e. $E>0$ (`simon_fcen…tex` `eq:simon` L248–253; abstract L96–100;
  Simon~2019, Conjecture 20.2). $P_{\rm ac}(H)\mathbf 1_K(H)=0$ on a nonempty compact $K$
  gives $m_{\rm ac}=0$ a.e. on $K$ — contradicting the conjecture for $d\ge2$ (here $d=3$). The
  Note's phrasing "Simon's multidimensional $L^2$ conjecture is false" (L7721) is thus correct
  *under its own hypothesis*. ✓
- **Caveat:** the hypothesis consumed at L7729–7732 is the **per-probe** reading
  ("contracts each of the first $j$ fractional moments by $3/4+o(1)$"); Theorem 6 currently
  supplies only the sum-level statement. See H. The conditional structure itself is sound.

## H. QUANTIFIER AUDIT — **GAP (MAJOR; repairable)**

- `prob:physical-grouped-global` (L2069–2073) demands: one generation "**contracts every targeted
  fractional moment on all of $K$** by a factor at most $3/4$" — a **per-probe** quantifier.
- Theorem 6 (MAIN_ATTEMPT item 1) delivers: "the **total** targeted beta-moment on $K$ contracts by
  a factor at most $3/4+\zeta$" — a **sum-level** statement; its Step-5 ledger
  (MAIN_ATTEMPT lines around "Summing") aggregates over the cover and over probes.
- Likewise the underlying one-window proposition contracts "*the sum* of the targeted
  $\beta$-fractional moments on $I$" (L2002–2003), and its engine
  `eq:singular-vector-bundle-contraction` (L1662–1666) contracts the **sum**
  $\sum_p\|x_{p,M}\|^{2\beta}\le q\sum_p\|x_p\|^{2\beta}$ with one common group; no per-vector
  factor is asserted.
- The surrounding text confirms the intended quantifier is per-probe:
  `cor:exact-hazard-bottleneck` (L2140–2158) reduces the global problem to hazard divergence for
  `eq:one-centre-gain` (L2094–2098), whose density $f=w^\beta$ is **a single probe's** fractional
  density; and `prop:conditional-counterexample-final`'s proof (L7729–7730) reads "contracts
  **each** of the first $j$ fractional moments by $3/4+o(1)$".
- MAIN_ATTEMPT Corollary 7 therefore **overclaims** ("contracts every targeted fractional moment…
  by $3/4$") relative to Theorem 6's proven content.

**Exact fix (either suffices; both use only proved components):**
1. *Per-probe upgrade:* run the whole finite cover construction once per targeted probe
   ($P\times L$ groups, $P,L$ finite, fresh disjoint shells, per-group error shares
   $\zeta/(10PL)$, common depth chosen against $M_{\max}PL$). The protection mechanism (A/B)
   keeps previously certified probes within their allocated shares, so the last probe's
   certificate and all earlier ones hold simultaneously up to $\zeta$.
2. *Dovetail-side rewrite:* replace `eq:dovetail-contract` by total-moment contraction
   $\sum_{p\le j}I_{p,j}\le(27/64)\sum_{p\le j}I_{p,j-1}+\eps_j$ (triple generation); then every
   $I_{p,N}\to0$ geometrically and the witness-locking/singularity conclusion of
   `thm:scalar-dovetail` follows with the identical proof.

---

## ADDITIONAL FINDINGS (bookkeeping)

- **G3 (group-level chromatic law), severity minor–moderate.** The block-level law
  $\operatorname{err}\le CMm|k/k_\star-1|+\eps$, used by MAIN_ATTEMPT Steps 3/6 (via
  `lem:window-cost`, whose statement carries it as a *hypothesis*), is derivable by
  differentiating the finite Talbot product in $k/k_\star$ (derivation visible only in the
  commented block, L7471–7473; single-cell analogue proved in
  `fixed_potential…tex` `eq:physical-riesz-cell-chromatic-error` L124–128 and
  `eq:riesz-chromatic-error` L618–622). It should be promoted to a live lemma for blocks.
  Without it, Step 6's "cost does not see the window count" argument rests on a hypothesis
  rather than a proved law. Note this does **not** affect the width-positivity/existence core
  (Steps 1–5), which never invokes the chromatic law.
- **FSM open set / closed subcover, severity minor.** `lem:finite-spectral-model`'s last assertion
  (L1961–1963) grants a neighbourhood per center; the residual constant $C_{\rho,T}\delta$
  (L1983–1985) degenerates as the neighborhood grows, so openness of $V(k_\star)$ for the *fixed*
  $T=M$ is fine, but the report recommends stating Step 1 with closed balls
  $\overline{B}_{r(k_\star)}$ chosen before extraction.
- **Effectivity, severity informational.** All group lengths obtained via Dini are ineffective;
  sufficient for existence-based Theorem 6 and the assembly; required only for the hazard route
  (MAIN_ATTEMPT Theorems 4–5, which additionally need G1/G2).

---

## VERDICTS

| Item | Verdict |
|---|---|
| A. Scope of protection | **PASS** (minor provenance note on exact flux identity of realized pairs) |
| B. Off-window behavior | **PASS** (mechanism: pointwise-in-$k$ exact Hardy nonexpansion + placement + uniform residuals; per-functional error independent of group/stage counts) |
| C. Width positivity vs cost | **PASS** (no proved result forces width shrinkage; all shrinkage statements bind only uniformity-over-bundles or the adaptive route) |
| D. Sequential composition | **PASS** ((i)/(ii)/(iii) verified; effectivity note recorded) |
| E. Dovetail fit | **GAP** (moderate — arithmetic and error summability close, but `eq:dovetail-contract` needs per-probe contraction that is not delivered; repairs (E.1)/(E.2) specified) |
| F. Hidden radialization dependence | **PASS** (no circularity; full dependency table above; presentational caveat: full-block cell assembly lives in commented-out text) |
| G. Assembly proof | **PASS** (internally sound conditional argument; inherits item H's gap through its hypothesis) |
| H. Quantifier audit | **GAP** (**major** — sum-level delivered vs per-probe demanded by `prob:physical-grouped-global` and consumed at L7729–7732; exact two-line repair given) |

## OVERALL JUDGMENT: **UNPROVEN (gaps listed; program repairable)**

Theorem 6's architecture survives adversarial scrutiny: the protection mechanism is genuinely
global (exact pointwise-in-$k$ Hardy identity + deterministic simultaneous placement + uniform
truncation residuals), the finite-cover/compactness move is not blocked by any proved result in the
source, sequential recomposition re-certifies cleanly, and the ingredient chain contains **no
hidden dependence** on the open radialization problem, the lens machinery, or the outward time
budget — the truth-ledger's partition (one-window layer proved; radialization conditional) is
accurate. However, Theorem 6 **as written does not prove `prob:physical-grouped-global`**: it
establishes the sum-level contraction, while the problem statement, the hazard corollary, and the
counterexample assembly each require the per-probe quantifier (item H, major), and the block-level
chromatic cost law used in its Step 6 is currently a hypothesis, not a live lemma (G3, minor–moderate),
with the supporting cell assembly partially confined to commented-out text. Both gaps admit concrete
repairs using only components the Note already proves (per-probe repetition of the finite
generation, or a total-moment dovetail; promotion of the differentiated-product chromatic bound to
a live block lemma). Accordingly: **no disproof of Simon's conjecture is currently established**;
the conditional route remains open and, on this audit's evidence, repairable within the note's own
proved toolkit. The claim "If Theorem 6 is correct, then … Simon's conjecture is DISPROVED
(conditionally)" is **not yet activated**: Theorem 6 is not yet correct as stated.
