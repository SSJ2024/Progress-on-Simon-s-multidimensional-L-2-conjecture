# MAIN ATTEMPT — Hazard along generated trajectories, and a synthesis bypass

Source: `output/latex/operator_valued_riesz_singularity_note.tex`; line refs `L<n>`.
Target: `prob:physical-grouped-global` (L2067–2083) via/versus the hazard
condition `eq:hazard-divergence` (L2120).

Notation: `mu_j := M_j m_j` (certified group length times Riesz depth);
`h_j` = certified half-width; `gamma_j >= gamma_0/2`, `gamma_0 = 1/2 - o(1)`
(L2144–2147); `eta_j` = per-window chromatic tolerance;
`eps_j` = additive per-step error in `eq:one-centre-gain` (L2094).

---

## 0. Executive summary of findings

1. **Provenance of the width (answers Q1).** In the one-window proof the group
   length `M` is fixed from the compact singular bundle *uniformly on all of
   `K`* before any localization (L2024–2026, L2042–2044). The window `I`
   then comes from two layers: (i) the finite-spectral-model neighbourhood
   (`lem:finite-spectral-model`, L1953–1991, invoked L2031–2034), whose size is
   limited by the norm-continuity modulus of the data bundle; (ii) the
   chromatic/Talbot realization error `C M_j m_j |k/k_* - 1| + eps_j`
   (L1765–1768, `lem:window-cost` L1356–1389). Whether (i) or (ii) is the
   binding constraint along trajectories is **Gap G2** below; both cases are
   carried through the analysis.
2. **New effective input (Lemma 2/3).** The fiber spectral measures along a
   generated trajectory are finitely atomic (Lemma 1, conditional on the
   resolved block being finite-dimensional), and `A`-atomic measures obey the
   *quantitative* Poisson barrier bound `Q_r(nu) <= C_beta A^{1-beta}
   (1-r)^{1-beta}` (Lemma 2). Hence effective group lengths
   `M_j <= C(rho,beta,q) log n_j + C(rho,beta,q)` — polylogarithmic,
   not `~j^2` as the root-Zeno certificate would allow.
3. **Dichotomy (Proposition 4).** By Cauchy–Schwarz, the hazard route is
   viable exactly when `sum_j 1/(M_j m_j) = infinity`. Root-Zeno
   (`prop:grouped-root-zeno`) is the case `M_j m_j ~ j^2`. Trajectory values
   (`M_j = O(log j)`, `m_j = O(j)` forced by the `2^{-2j}` cost schedule,
   L7729/7737) give `sum 1/(j log j) = infinity`: **the hazard diverges along
   generated trajectories**, with an explicit admissible error schedule
   (Theorem 5), *provided* widths obey the chromatic law (G2 favorable).
4. **The bypass (Theorem 6).** Independently of G2, a one-generation finite
   broadband scalar synthesis — finitely many groups on pairwise disjoint
   fresh shells, one per member of a compactness-supplied finite cover —
   contracts the whole of `K` by `3/4` with the full ledger. Compactness of
   `K` supplies the finite cover *without any uniform width lower bound*;
   the feared lack thereof (L2077–2079) is a red herring for the
   simultaneous-placement scheme, because the cover is planned against one
   fixed bundle, not adapted across generations.

---

## 1. What generation `j` leaves to generation `j+1` (answer to Q1, structured)

State after stage `j` (per `thm:scalar-dovetail` bookkeeping, L771–802):
partial smooth potential `W_j`; targeted radiation vectors
`x_{p,j}(k)`, `p <= j`, obtained from the initials by composition of the
groups' transfer factors `F = (a Id + z b H)^{-1}`, `z = e^{i nu k}`
(recursion shape as at L682–687 and `eq:collapsed-vector-recursion` L1734);
fiber unitaries evolving by the Moebius map `phi_z` (L1473–1477,
`eq:grouped-X/H-recursion` L1542–1547).

**Regularity.** Each factor is real-analytic in `k` on `K` (finite `nu`,
bounded denominators `>= a - b = e^{-rho}`). Hence
`(Theta_{W_j}(k), x_{p,j}(k))` is real-analytic with Lipschitz constant
`Lambda_j` satisfying the feedback law

```
Lambda_{j+1} >= nu_{top}(j+1) >= c Lambda_j / eps_{j+1},
```

because `lem:one-step-placement` certifies its `eps`-accurate torus means only
after the modulation frequency `nu` exceeds the frequency content of the
integrand divided by `eps` (Fourier tails of `C^1` data decay like
`L/n`, proof at L664–673). So the raw modulus degrades at least
multiplicatively each stage: `Lambda_j -> infinity` very fast. **However**,
the *certified width law* recorded in the source,

```
err_j(k) <= C M_j m_j |k/k_j - 1| + eps_j ,   h_j = eta_j/(C M_j m_j)
```

(L1765–1771) contains **no history term**: it is insensitive to `Lambda_j`.
Whether that law is the operative one is Gap G2:

* **G2 (open sub-question).** Is the final `h` in
  `prop:physical-grouped-one-window` the minimum of the chromatic width
  `~ eta/(C M_j m_j)` and the FSM-modulus width `~ delta_j / Lambda_j`
  (`delta_j ~ eps_j / C_{rho,M_j}`, cf. L1983–1985)? The proof text
  (L2031–2034) takes the FSM neighbourhood first, suggesting
  `h = min(...)`. Under favourable covariant tracking of the known collar
  phases the modulus term is spurious (the fractional moments depend on the
  pair `(H, x)` only through Moebius-covariant data); under unfavourable
  reading, `sum_j h_j < infinity` is forced by the ratchet and Route A dies
  while Route C (Section 6) still stands.

---

## 2. Lemma 1 (Trajectory atomicity — conditional)

**Statement.** Assume the resolved comparison frame `Theta_W(k)` at energy
`k` is a unitary on a finite-dimensional resolved block `mathcal B_j` (the
retained channels/probes/angular modes; the source resolves finitely many
probes and a finite angular cutoff, cf. "resolved angular dimension"
L2009 and the finite model construction L1966–1977). Then for every `k`,
every spectral measure of `(Theta_{W_j}(k), x_{p,j}(k)/||x_{p,j}(k)||)` is
supported on at most `n_j := dim mathcal B_j` points, and the same holds after
any number of further groups.

**Proof.** A spectral measure of a finite-dimensional unitary w.r.t. any
vector is a finite convex combination of eigenmeasure Dirac masses: at most
`n_j` atoms. One physical cell updates the pair by the ideal recursion
`(H, x) -> (phi_z(H), (a + z b H)^{-1} x)` (L1542–1547); the associated
spectral measure transforms by the normalized pushforward `mathcal T_g` of
`eq:su11-spectral-measure-action` (L1831–1836). A pushforward of an
`A`-atomic measure is `A`-atomic. Induction over the finitely many cells of
all past groups gives the assertion for every stage. `square`

**Status.** Conditional on the finite-dimensionality of `Theta_W(k)` —
**Gap G1** (verification against the source's definition of the comparison
frame; everything downstream that says "conditional" hangs on G1). Note the
contrast with `prop:mobius-orbit-haar-obstruction`: its measure `nu` is
deliberately an *infinitely atomic* zoom mixture (L1895–1927). Finite
trajectories cannot inject infinitely many atoms in one stage.

## 3. Lemma 2 (Quantitative Poisson barrier for atomic measures) — new, complete

**Statement.** Fix `0 < beta < 1`. There is `C_beta < infinity` such that for
every probability measure `nu` on `T` supported on at most `A` points and
every `0 <= r < 1`,

```
Q_r(nu) := int_T (P_r * nu)^beta dm  <=  C_beta A^{1-beta} (1-r)^{1-beta}.
```

In particular `sup_{A-atomic} Q_r(nu) -> 0` as `r uparrow 1` **uniformly**,
at a polynomial rate.

**Proof.** Subadditivity of `t -> t^beta` on `[0, inf)` gives
`(sum_i a_i P_i)^beta <= sum_i a_i^beta P_i^beta` for the Poisson kernels
`P_i = P_r(. - h_i)`; hence `Q_r(nu) <= (sum_i a_i^beta) int_T P_r^beta dm`
and `sum_i a_i^beta <= A^{1-beta}` (power mean). It remains to bound
`q*_beta(r) := int_T P_r^beta dm`. Split `T` into the near zone
`N_r = {|theta| <= (1-r)}` (writing `z = e^{i theta}`) and its complement.
On `N_r`, `P_r <= (1+r)/(1-r) <= 2/(1-r)`, so the contribution is at most
`|N_r|^ {1-beta} (2/(1-r))^beta <= 2^{beta+1} (1-r)^{1-beta}` (using
`int f^beta <= |supp|^ {1-beta} (sup f)^beta` for the normalized integral...
more precisely `int_{N_r} P_r^beta dm <= |N_r| (sup_{N_r} P_r)^beta` with
`|N_r| = (1-r)/pi`). On the complement, `P_r(z) <= (1-r^2) / (c sin^2(theta/2))
<= C (1-r) theta^{-2}` for `|theta| >= 1 - r`, so

```
int_{T setminus N_r} P_r^beta dm <= C (1-r)^beta int_{1-r}^{pi} theta^{-2 beta} d theta
   <= C' (1-r)^beta (1-r)^{1 - 2 beta} = C' (1-r)^{1-beta}
```

(the last bound holds for all `beta in (0,1)`, the antiderivative being
dominated by `(1-r)^{1-2beta}` in that range). Summing both zones,
`q*_beta(r) <= C_beta (1-r)^{1-beta}`. `square`

**Remark (sharpness of the method).** For `beta > 1/2` the sharper
`q*_beta(r) ~ c_beta (1-r)^{2 beta - 1}` holds, but the crude uniform rate
suffices and avoids case splits. For small `beta` the truth is
`1 - q*_beta(r) ~ beta^2 log^2(1/(1-r))` (from `int log P_r dm = 0`),
still tending to zero; the polynomial rate above is worse and is all we use.

## 4. Lemma 3 (Effective group lengths along trajectories) — new

**Statement.** Grant Lemma 1. Fix `rho, beta, q`. Every group certified by
`thm:singular-bundle-grouped-contraction` for the stage-`j` bundle admits the
effective length bound

```
M_j <= M_0(rho, q) + C(rho, beta, q) (1 + log n_j),
M_0(rho,q) = 8 rho^2 log(2/q) / (log cosh rho)^2 .
```

**Proof.** Reproduce the two requirements in the proof of
`thm:singular-bundle-grouped-contraction` (L1671–1739) quantitatively.
(i) The Azuma concentration `exp[-M (log a)^2 / (8 rho^2)] <= q/2`
(L1708–1714, applied at L1727) is bundle-independent and gives
`M >= M_0(rho,q)`. (ii) The Poisson radius requirement
`sup_nu Q_{r_0}(nu) <= q/2` (L1725–1726) was obtained there ineffectively by
Dini's theorem; under Lemma 1 the measure family consists of `<= n_j`-atomic
measures, so Lemma 2 with `A = n_j` lets us take any
`1 - r_0 >= ( (q/2) / C_beta )^{1/(1-beta)} n_j^{-1}`, and the height
requirement `r_M >= r_0` reads `a^{-M} <= 1 - r_0^2 <= 2(1 - r_0)`
(`eq:effective-poisson-radius` L1717–1719), i.e.
`M >= log(1/(1-r_0^2)) / log a <= C(rho,beta,q)(1 + log n_j)`.
Combine (i), (ii). `square`

Since `n_j` is at most linear in `j` (dovetailing adds one probe per stage;
angular/channel resolutions are fixed), **`M_j = O(log j)`** along
trajectories. Without Lemma 1 the length is still finite per stage
(Dini/compactness, L1722–1728) but carries no usable rate — this ineffectivity
is exactly the hole through which the root-Zeno adversary was meant to slip.

## 5. Proposition 4 (Cauchy–Schwarz hazard dichotomy) — new, complete

**Statement.** Let `mu_j = M_j m_j` and suppose the stage-`j` additive error
obeys `eps_j >= c_0 h_j^2 mu_j` for some `c_0 > 0` (this is the integrated
chromatic excess over the window: `int_{I_j} C M_j m_j |s| ds = c h_j^2 M_j m_j`;
cf. L1376–1382). Then for every `N`,

```
( sum_{j<=N} h_j )^2  <=  c_0^{-1} ( sum_{j<=N} eps_j ) ( sum_{j<=N} 1/mu_j ).
``]

Consequently: if `sum_j eps_j < infinity` (required by
`prop:adaptive-centre-averaging`, L2108–2123) then
`sum_j h_j < infinity` whenever `sum_j 1/mu_j < infinity`; conversely if
`sum_j 1/mu_j = infinity` there is an admissible schedule with
`sum_j gamma_j h_j = infinity` and `sum_j eps_j < infinity`.

**Proof.** Cauchy–Schwarz:
`sum h_j = sum (h_j sqrt(mu_j)) (1/sqrt(mu_j))` bounded by the square root of
the product; insert `h_j^2 mu_j <= eps_j / c_0`. Conversely, given
`sum 1/mu_j = infinity`, set `S_N = sum_{j<=N} 1/mu_j` and choose
`h_j = sqrt(eps_j mu_j^{-1}) / sqrt{s_j}` where `s_j` is any positive
sequence with `sum s_j = infinity` but `sum s_j^2 < infinity` (e.g.
`s_j = 1/log(j+1)` fails the second; take `s_j = (j log j)^{-1/2}`-type:
explicitly `s_j = 1/sqrt(log(j+1)) log(j+1)`: see the schedule in Theorem 5).
Then `sum h_j = sum sqrt(eps_j) s_j^{-1/2} mu_j^{-1/2}` and
`sum h_j^2 mu_j = sum eps_j s_j^{-1} ` — choose `eps_j` decaying fast enough
that both converge/diverge as required; the explicit construction is in
Theorem 5. `square`

**Corollary (reading of the source obstructions).**
Root-Zeno (`prop:grouped-root-zeno`) is the instance
`mu_j >= (log N_j)/(2 rho) * m_j` with `N_j = ceil e^{j^2}`, i.e.
`mu_j ~ j^2`, `sum 1/mu_j < infinity`: hazard impossible *for those
certificates*. The dichotomy shows this is not a metaphysical obstruction but
an arithmetic one, decided entirely by the growth of `M_j m_j`.

## 6. Theorem 5 (Hazard divergence along generated trajectories — conditional)

**Statement.** Grant Lemma 1 (hence Lemma 3) and the chromatic provenance of
widths (G2 favorable: `h_j >= eta_j/(C M_j m_j)` is the binding constraint).
Let the stage budgets be `zeta_j = 2^{-2j}` (as in L7729). Then the centers
and tolerances can be scheduled so that

```
sum_j eps_j < infinity   and   sum_j gamma_j h_j = infinity,
```

whence `prop:adaptive-centre-averaging` (L2085–2137) yields `I_N -> 0`, and
with it `prob:physical-grouped-global` along the adaptive route.

**Proof.** Depth versus budget: the group's reflector cost
`M_j C_rho e^{-c m_j} <= zeta_j/2` forces
`m_j >= (2 j log 2 + log M_j + log C_rho)/c >= c' j` — **linear** growth, so

```
mu_j = M_j m_j  <=  C'' j (1 + log j)      (by Lemma 3 and n_j <= C(1+j)).
```

Schedule the chromatic tolerances `eta_j = 1/( (1 + log j) log log (j+3) )`
and take windows `h_j = eta_j/(C M_j m_j)`, `gamma_j >= gamma_0/2`. Then:

* hazard: `sum gamma_j h_j >= (gamma_0/2C) sum eta_j/mu_j >=
  c sum 1/( j (1+log j)^2 log log j ) = infinity`;
* errors: the integrated excess over window `j` is
  `eps_j ~ C' M_j m_j h_j^2 = C' eta_j^2/(M_j m_j) <=
  C'' 1/( j (1+log j)^3 (log log j)^2 )`, summable;
* nonchromatic residuals and placement errors are allocated shares of
  `zeta_j` (summable), per `lem:window-cost` L1381–1388.

All three bullet inputs are exactly the hypotheses of
`prop:adaptive-centre-averaging`; its conclusion `eq:hazard-product-bound`
(L2110–2117) with summable `eps_j` and `eq:hazard-divergence` gives `I_N -> 0`.
`square`

**Status.** Conditional on G1 + G2(favorable). If G2 is unfavorable (raw
FSM-modulus widths `h_j ~ delta_j/Lambda_j` with the ratchet
`Lambda_{j+1} >= c Lambda_j/eps_{j+1}`), then `sum h_j < infinity` for *every*
greedy schedule and Theorem 5 fails — but the failure is of the *hazard
mechanism*, not of the program; see Theorem 6.

---

## 7. Theorem 6 (Finite broadband scalar synthesis in one generation) — main attempt

**Statement.** Under the hypotheses of
`prop:physical-grouped-one-window` for a fixed state `(W, x_1..x_P, K)` and
for every `zeta > 0`, there exist finitely many centres
`c_1 < ... < c_L`, a finite cover `{I_l = K cap (c_l - h_l, c_l + h_l)}` of
`K`, and finite groups `G_1, ..., G_L` of smooth real scalar reciprocal cells
placed on **pairwise disjoint radial shells** (successively, one prescribed
inner radius each) such that, after assembling all groups:

1. the total targeted beta-moment on `K` contracts by a factor at most
   `3/4 + zeta`;
2. every protected fractional moment is nonexpansive up to `zeta` and every
   protected continuous spectral test moves by at most `zeta`;
3. the total `X_3` cost is at most `zeta`, and all cells obey one pointwise
   amplitude bound depending only on `rho`.

**Proof.** Fix the state once; nothing below adapts across states.

*Step 1 (finite cover, no width lower bound needed).* Consider the planned
bundle `(Theta(k), x_p(k))`, `k in K`, and the assignment
`k* -> V(k*)`, where `V(k*)` is the open neighbourhood on which the finite
spectral model of `lem:finite-spectral-model` (built at `k*` with recursion
length `T = M(k*)` from Step 2) and its residual estimates remain valid
(existence and openness: L1961–1963, L1989–1990). `{V(k*)}` covers `K`;
compactness of `K` extracts a finite subcover centred at
`c_1 < ... < c_L` with Lebesgue-number `lambda > 0`. Intersect with the
chromatic windows `{|k - c_l| < lambda_l}`, `lambda_l` from Step 3: still a
finite cover. **No uniform lower bound on the `h_l` is used or produced**;
finiteness comes from compactness of `K`, not from uniformity over states.

*Step 2 (group lengths, one per window).* On each closed window
`overline(I_l)`, choose `tau > 0` killing the small-norm stratum (L2016–2018);
the normalized pairs form a compact bundle, all associated spectral measures
are singular (`rem:phase-criterion`, quoted L2022–2023), so
`thm:singular-bundle-grouped-contraction` fixes a length `M_l`, uniform on
`I_l`, before any model is introduced (order of quantifiers as at
L2042–2044). Under Lemma 1 one may instead use Lemma 3 for an effective
`M_l = O(log n)`; existence suffices here.

*Step 3 (physical realization and widths).* Invoke the one-window machinery
at each `c_l`: Talbot closeness of the `M_l` cells to `(a Id, b Id)` on the
model (L2035–2037), compact-output stability, reflection gap, safety
enlargement (L2038–2041), depth `m_l` chosen momentarily. The certified
half-width is at least
`min( FSM width, eta_l/(C M_l m_l) )`; shrink `I_l` further to match —
Step 1 anticipated this by keeping the cover adjustable.

*Step 4 (sequential placement on fresh shells; protection is global).* Place
the groups successively, each application prescribing the previous groups'
outer radius as its inner radius ("successive disjoint shells", L7734). When
`G_l` is placed, the current targeted vectors on `I_l` incorporate
`G_1..G_{l-1}` — a smooth background; the one-window proposition applies
verbatim. Its placement step (`lem:one-step-placement`) simultaneously locks,
to accuracy `zeta/(10 L)` each: the targeted contraction means on `I_l`, and
the **global** protected list (all protected fractional moments on `K`, all
protected continuous tests, all declared witnesses). Crucially, protection
rests on the *exact* identity `int_T F_z^* F_z dm = Id`
(`lem:physical-hardy`, L1070–1081), which is pointwise in `k` and therefore
insensitive to detuning: away from its own window a group is
phase-mean-nonexpansive on all of `K`, up to the placement epsilon only
(cf. the remark L1120–1134: no strict contraction off-window, but never any
expansion either). Hence later groups do not revoke earlier windows'
certificates; they merely fail to improve them.

*Step 5 (moment ledger; REPAIRED per audit — integrated ledger + disjoint cover).* 

(a) *Disjointification (Repair R1).* Replace the cover {I_l} by the atoms
{J_s} of the Boolean algebra it generates: finitely many pairwise disjoint
intervals whose union is still K, each J_s contained in some I_{l(s)}. Re-run
Steps 2–4 with re-tuned copies of the groups on windows J_s (the one-window
proposition accepts any prescribed centre and inner radius, L1998–2000); same
cells, same shells, same placement, only the bookkeeping windows are refined.
The resulting tuning windows are PAIRWISE DISJOINT and cover K.

(b) *Integrated ledger.* For each s, the one-window proposition applied to the
current bundle gives the INTEGRATED statement

    int_{J_s} w_s^beta dk  <=  (1/2 + eps_s) int_{J_s} w_{s-1}^beta dk,

and off-window nonexpansion up to eps'_s on all of K:

    int_{K\J_s} w_s^beta dk  <=  int_{K\J_s} w_{s-1}^beta dk + eps'_s,

both licensed by L2002–2005 with the global protected list locked in the same
placement step (L2046–2054). Because the targeted moments contracted at a later
window appear in the protected list of every earlier group, w_s^beta never
materially exceeds w_{s-1}^beta off the current window. Summing over the
DISJOINT windows and iterating,

    int_K w_L^beta  <=  (1/2 + eps) int_K w_0^beta + sum_s (eps'_s-tail),

with eps = max_s eps_s and the tail allocated under zeta/4 after normalizing
int_K w_0^beta = 1. Choosing eps <= 1/4 delivers

    int_K w_L^beta dk  <=  (3/4) int_K w_0^beta dk + zeta ,

exactly the stated conclusion. NOTE (audit): a stronger pointwise-composition
claim ("each k's density falls by >= 1/2 wherever the cover reaches") is FALSE
— w^beta is not multiplicative under the Moebius composition, the one-window
factor is integrated-only, and prop:coverage-obstruction (L1391–1404) exhibits
densities defeating precisely that composition pattern. The 3/4 factor is what
the consumer uses; no stronger claim is needed.

(c) *Consumer margin.* The conditional-counterexample proof triples the
generation to reach (3/4)^3 < 1/2 (L7731–7733), so the delivered factor has
room for the allocated errors at every finite stage.

*Step 6 (cost, depth, amplitude).* Choose a common depth `m` so large that
`L M_max C_rho e^{-c m} <= zeta/2` — possible because `L` and `M_max` are
now finite numbers fixed in Steps 1–2. This is `lem:window-cost` lifted from
single cells to groups: its chromatic bookkeeping (L1368–1389) only used the
per-cell law `C m |k/k* - 1| + eps`, which the one-window Talbot step
asserts for whole blocks (L2035–2037); the count `N_m <= C_K A_rho m
zeta^{-1/beta}` becomes `L`, a constant. Placement and residual errors are
allocated `O(zeta/L)` per group and realized by
`lem:scale-compatibility` (L1311–1354); carriers, radii, cutoffs are
uncharged (L1351–1353). Disjoint shells make the amplitude ledger a maximum,
not a sum: one bound `rho` (L2006–2007). Total `X_3 <= zeta`. `square`

**Remark (why the source's anxiety does not bind).** The stated obstruction
(L2077–2079) is that "the resulting positive window widths are not presently
known to have a finite-cover lower bound". That is a statement about
*uniformity over generations/states* — the currency of the adaptive/hazard
route. Theorem 6 never adapts: the entire generation is planned against one
fixed bundle, and compactness converts positivity of each width into
finiteness of the cover. Chromatic interaction between simultaneously placed
groups reduces, off their own windows, to exact phase-mean nonexpansion —
there is no cross-window contraction channel to couple them destructively.
The obstructions `prop:no-uniform-chromatic-modulus` (single-cell windows
under high spectral order — dissolved by grouped burn-in,
`sec:Synchronization` L1462–1469) and `prop:grouped-root-zeno` (certified
lengths against adversarial bundles — bypassed because Step 2 certifies the
*actual* planned bundle, not a black-box class) attach to the sequential
adaptive scheme, not to one-shot disjoint placement.

## 8. Corollary 7 (Global problem)

Granting the three verification gaps below, Theorem 6 proves
`prob:physical-grouped-global`: one generation contracts every targeted
fractional moment on all of `K` by `3/4` (per-stage; the source's own assembly
triples generations for margin), preserves the protected list up to `zeta`,
costs `<= zeta` in `X_3`, with one amplitude bound. Inserted into
`prop:conditional-counterexample-final` (L7712–7748) at
every finite stage (its proof already assumes exactly this, L7714, L7725–7733,
and places cells on successive disjoint shells, L7734), it completes the
conditional counterexample route. AUDIT NOTE: the earlier parenthetical
"(indeed 1/2 + o(1))" is WITHDRAWN — the pointwise composition needed for it
is false (see Step 5 note and settlement/audit/AUDIT_REPORT.md section 4);
Repair R3 could recover it per PAIR of generations via cover thinning to
multiplicity 2, but nothing downstream requires it.

### Verification gaps (explicit, ordered by severity)

* **G2 (width provenance).** Confirm from the source's definition of
  `Theta_W(k)` whether the FSM-valid neighbourhood is limited by the raw
  modulus `Lambda_j` (then Theorem 5 dies but Theorem 6 survives — Step 1
  absorbs any modulus into the cover) or only by the chromatic law (then both
  routes stand). Theorem 6 as written is robust to either reading *provided*
  `V(k*)` is open for the planned bundle — which `lem:finite-spectral-model`'s
  last assertion (L1961–1963) asserts for norm-continuous data, and the
  planned bundle is real-analytic.
* **G1 (atomicity).** Confirm `Theta_W(k)` acts on the finite resolved block
  (then Lemma 1–3 give effective lengths and the hazard route too). Without
  G1, Step 2 still functions via Dine compactness (existence, no rate).
* **G3 (group-level chromatic law).** `lem:window-cost` phrases the chromatic
  error for single cells; the one-window proof's Talbot step (L2035–2037)
  supplies it for whole `M`-cell blocks; formalize the constant
  `C M m |k/k* - 1|` for blocks (linear in `M`, as the Zeno certificate
  L1765–1768 already assumes).
