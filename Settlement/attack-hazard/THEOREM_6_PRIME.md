# THEOREM 6′ — Per-probe finite broadband synthesis, the block chromatic law, and activation of the conditional counterexample

**Purpose.** Post-audit repair of `settlement/attack-hazard/MAIN_ATTEMPT.md` §7–8, closing the two gaps
flagged by `settlement/audit-theorem6/AUDIT_REPORT.md`:

* **GAP H (major, quantifier mismatch).** Theorem 6 delivered a *sum-level* `3/4` contraction of the total
  targeted beta-moment, while `prob:physical-grouped-global` (Note L2067–2083) and the assembly proof
  (`prop:conditional-counterexample-final`, Note L7712–7748, esp. L7729–7732 "contracts **each** of the
  first `j` fractional moments") demand a **per-probe** contraction. Closed by Theorem 6′ below
  (per-probe synthesis by repeated one-probe-aimed generations).
* **GAP G3 (minor–moderate, hypothesis to promote).** The block-level chromatic law
  `err(k) <= C M m |k/k_* - 1| + eps` was used in MAIN_ATTEMPT Steps 3/6 but existed only as a
  *hypothesis* inside `lem:window-cost` (Note L1356–1389). Closed by Lemma A below (complete proof).

**Line-reference conventions.** `L<n>` = live line `<n>` of `output/latex/operator_valued_riesz_singularity_note.tex`
("the Note"); `F<n>` = `output/latex/fixed_potential_riesz_counterexample.tex`; `S<n>` =
`output/latex/simon_fcen_new_attack_program.tex`; `MA<n>` = `settlement/attack-hazard/MAIN_ATTEMPT.md`;
`AR<n>` = `settlement/audit-theorem6/AUDIT_REPORT.md`. All line numbers were re-verified against the live
files on 2026-08-25.

---

## 0. Executive summary

1. **Lemma A (Section 2) closes G3.** For a group of `M` reciprocal cells of common Riesz depth `m`
   tuned at `k_*`, the certified window contraction obeys the *block chromatic law*
   `factor(k) <= q + C_2 (C_1 M m |k/k_* - 1| + M eps_c)` with `q in (0,1)` the ideal engine factor
   (take `q = 1/2`, as at L2024), `C_1 = C_1(K, rho)` explicit from the single-cell ledgers, and
   `C_2 = C_2(rho, q)` **fully explicit** (`C_2 = (1 - q)/delta_*(rho)`,
   `delta_* = (1/2) min( cosh rho * log cosh rho , (4 e^{rho})^{-1} )` suffices), independent of
   `M`, `m`, the placed phases, and the shell radii. The proof composes the cells not by naive operator
   telescoping (which incurs an `e^{rho M}` amplification) but through the SU(1,1) drift engine
   (`eq:positive-radial-drift` L1704–1707, `eq:effective-height-concentration` L1709–1714,
   `eq:effective-poisson-radius` L1716–1719, `eq:random-product-poisson-identity` L1685–1692), whose
   constants are `M`-uniform inside an explicit headroom band and capped by the exact Hardy nonexpansion
   (`lem:physical-hardy` L1058–1118). `lem:window-cost`'s hypothesis is thereby discharged
   unconditionally (Corollary A).
2. **Theorem 6′ (Section 3) closes H.** Given finitely many targeted probes `x_1..x_P`, compact `K`,
   `zeta > 0`, the construction runs `3P` generations on pairwise disjoint fresh shells; generation `g`
   aims at **exactly one** probe (each probe receives three consecutive aimed generations). Because the
   one-window proposition `prop:physical-grouped-one-window` (L1993–2065) contracts *the sum over the
   targeted probes* and the targeted list has cardinality one, its item 1 **is** a per-probe statement —
   the sum-versus-per-probe mismatch of AR item H dissolves identically. Protection of everything else is
   global by the pointwise-in-`k` Hardy identity (audit items A/B), later generations do not revoke
   earlier certificates (audit item D(iii)), and singularity of each new aim is re-certified twice over
   (rem:phase-criterion applied to the current potential; normalized Mobius pushforward of the spectral
   measures, `eq:su11-spectral-measure-action` L1831–1836). Per probe the tripled aim yields
   `(3/4)^3 = 27/64 < 1/2`, matching `eq:dovetail-contract` (L783) verbatim with the summable stage
   budgets `eps_j = 2^{-2j}` (L7728–7729).
3. **Corollary 6″ (Section 4).** `prob:physical-grouped-global` holds in the per-probe form consumed at
   L7729–7732. Granting the Note's proved ledger (dependence list in Section 5),
   `prop:conditional-counterexample-final` applies at every finite stage: there exist a bounded real
   `V in X_3` and a nonempty compact `K Subset (0, infinity)` with
   `P_ac(-Delta + V) 1_K(-Delta + V) = 0`. Consequently Simon's multidimensional `L^2` conjecture
   (`eq:simon` S248–253, Conjecture 20.2) is **false** for `d = 3`: the implication
   "`int |x|^{-nu+1} |V|^2 < infinity => m_ac(E; H) = infinity a.e.`" fails at `nu = 3`.

---

## 1. Standing notation

Fix throughout: `0 < beta < 1`; `K Subset (0, infinity)` nonempty compact with `kappa_K := inf K > 0`;
hyperbolic height `rho > 0` with boost entries `a = cosh rho`, `b = sinh rho`, so that
`a - b = e^{-rho}` and `a + b = e^{rho}` (the denominator bound used at L665, L896, L1982);
`C_0` the fixed reflector transition constant of `lem:bounded-reflector` (L1280–1309, Cartan parameter
`<= rho + C_0`, a profile statement independent of `k`). A *state* is a triple
`(W, x_1..x_P, K)` with `W` a smooth real finite partial potential and `x_p(k)` the current targeted
radiation vectors (incorporating all previously placed groups). A *generation* is a finite family of
groups of smooth real scalar reciprocal cells placed on pairwise disjoint radial shells with one
prescribed inner radius each (L1998–1999; MA295–296, MA327–330).

The engine factors are `S(z)` as at `eq:su11-random-product` (L1640–1647); the grouped recursion is
`eq:grouped-X-recursion`/`eq:grouped-H-recursion` (L1542–1547), collapsing to
`x_{p,M} = (B_M H + conj(A_M) Id)^{-1} x_p` (`eq:collapsed-vector-recursion` L1732–1736). Spectral
measures transform along placed groups by the normalized Mobius pushforward
`mathcal T_g` of `eq:su11-boundary-action`/`eq:su11-spectral-measure-action` (L1827–1836).

---

## 2. Lemma A (Block chromatic law) — closes GAP G3

### 2.1 Statement

**Lemma A.** Fix `rho > 0`, `0 < beta < 1`, `q in (0, 1)`, `K Subset (0, infinity)`, and a compact
bundle class `mathfrak M` of probability measures on `T` (the associated spectral-measure family of the
current state; all members singular). Let `G` be a group of `M >= 1` reciprocal shell cells, each of
Riesz depth `m`, all tuned to the common centre `k_* in K`, with fixed collar phases
`z = (z_1, ..., z_M) in T^M`. Assume each cell `j` obeys, on the common finite safety/model space:

* **(C1) Flux exactness.** `A_j(k)^* A_j(k) - B_j(k)^* B_j(k) = Id` for every `k in K` (inherited from
  the exact radial composition `eq:exact-jost-shell-update-final`, L7691–7698; see AR A, minor note).
* **(C2) Tuned closeness.** `|A_j(k_*) - a| + |B_j(k_*) - b| <= eps_c` after the safety enlargement
  (`prop:full-block-talbot` L1254–1266 + `lem:compact-output-stability` L865–903 +
  `lem:reflection-gap` L919–934; the residual `C e^{-cm}` is folded into `eps_c` by the depth choice).
* **(C3) Single-cell chromatic law.**
  `sup_{k in K} ( |A_j(k) - A_j(k_*)| + |B_j(k) - B_j(k_*)| ) / |k/k_* - 1| <= C_1 m`,
  with `C_1 = C_1(K, rho, class) < infinity` — the differentiated single-cell product
  (`F` `eq:physical-riesz-cell-chromatic-error` F124–128, `eq:riesz-chromatic-error` F618–622;
  derivation locus in the Note at L7471–7473; ledger audit in Section 2.2).
* **(C4) Reflection gap, chromatic-free.** `|| B_j(k) A_j(k)^{-1} || <= tanh(rho + C_0)` for all
  `k in K` (`lem:bounded-reflector` L1296–1308: the Cartan bound is a property of the bump profile,
  not of `k`).

Then there are constants, depending only on `(rho, beta, q, mathfrak M, K)` and **not** on `M`, `m`,
the phases `z`, or the shell radii,

```
delta_* = delta_*(rho)  (> 0),      C_2 = C_2(rho, q)  (< infinity),
```

such that, defining the **block chromatic parameter**

```
delta(k) := C_1 M m |k/k_* - 1| + M eps_c ,
```

the realized group's fresh-collar torus mean of the targeted fractional density obeys, at **every**
`k in K`:

```
(+)   int_{T^M} sum_p || x_{p,M}^{real}(zeta, k) ||^{2 beta} dm^M(zeta)
         <= ( q + C_2 delta(k) ) * sum_p || x_p(k) ||^{2 beta} .
```

Moreover there is a **sharp band**: if `delta(k) <= delta_*` then the sharper bound
`factor(k) <= q` holds with **no** response term at all. Taking `q = 1/2` (the operating point L2024),
`(+)` is exactly the block law `err(k) <= C M m |k/k_* - 1| + M eps` with `C = C_2 C_1`: the shape
assumed by MAIN_ATTEMPT §1 (MA77–81), §7 Steps 3/6 (MA319–325, MA361–371), and by the Zeno-certificate
bookkeeping (L1764–1771), now proved.

### 2.2 What is imported, and where it is proved (smoothness audit)

**(a) Within-cell telescoping is already proved, linear in `m`.** The depth-`m` cell is
(forward Talbot train, localized reflector, reverse train, weak-slab realizations, collars). The
train-level chromatic law is `eq:riesz-chromatic-error` (F618–622):
`||W_{m,s} U_{m,s} - W_{m,1} U_{m,1}|| + ||U_{m,s} - U_{m,1}|| <= C_{K,a} m |s - 1|`, `s = k_*/k`,
proved by telescoping the two products and using the per-flight bound `eq:talbot-chromatic-bound`
(F566–568). The telescoping is linear in `m` because the surrounding factors have **operator norm one**
(free flights are unitary evolution groups `exp(- i pi s A_3 /(2 L^2))`, masks are bounded multipliers
on the finite block — equivalence of smooth norms on a fixed finite-dimensional space, used at L1270–1271).
The slab and collar remainders are `k`-independent constants (`eq:long-weak-mask-transmission/reflection`
F150–157: `O_K(T^{-1} + D^2 T/R^2 + T/R)` uniformly in `k in K`), hence contribute to `eps_c` and not to
the chromatic slope. This discharges **(C3)** with `C_1 = C_{K,a}` inflated by the finite-dimensional
norm-equivalence constants and by `ds/dk = k_*/k^2 <= kappa_K^{-2}`.

**(b) The reflector adds no chromatic term.** `lem:bounded-reflector` realizes the boost with
`k`-independent plateau coefficients and transitions whose Cartan parameter is bounded by `rho + C_0`
as a profile statement (L1304–1307). This discharges **(C4)** and identifies `C_0`.

**(c) Flux exactness at every `k`** is a structural consequence of unitarity/current conservation of the
reciprocal shell pair, transferred from the model by the stability lemmas; the compositional identity is
`eq:exact-jost-shell-update-final` (L7691–7698). This discharges **(C1)**. (AR A records this as a
provenance note, not a gap.)

**(d) Collar phases need no smoothness.** In the placed configuration the collar phase is
`z(k) = e^{i nu k}` (`lem:one-step-placement` L649–661). The ideal comparison at energy `k` uses the
**same** `z(k)`; the phase is a coordinate on the comparison torus, so the `k`-derivative `nu` — however
large — cancels identically in the matched-phase comparison. Large `inf_K |vartheta'|` is a
*placement-accuracy* requirement (Fourier decay of `L^1(K; C(T))` integrands, L664–673), met at
uncharged cost by the scale ordering of `lem:scale-compatibility` (L1311–1354: carrier chosen after the
masks; `F` L129–132, L212–216; AR A.3). No chromatic contribution and no smoothness beyond measurability
is required of the collars.

**(e) What the proof below newly does.** Compose the `M` cells. Naive composition of the *operators*
fails to be `M`-linear: each inverse factor has norm up to `e^{rho}` (indeed up to
`(1 - tanh(rho + C_0))^{-1}` by `lem:reflection-gap`, `eq:reflection-gap-inverse` L924–927), so
telescoping realized against ideal outputs incurs `e^{rho M}` — precisely the exponential that would
destroy the `C M m` law. (Within a cell this never happens because the train factors are norm-one; across
cells the inverse factors amplify.) The correct composition is through the drift engine of
`thm:singular-bundle-grouped-contraction`, whose constants are `M`-uniform, together with the exact Hardy
cap. That is executed next.

### 2.3 Proof of Lemma A

Write `delta_1(k) := C_1 m |k/k_* - 1| + eps_c` for the per-cell parameter, so `delta(k) = M delta_1(k)`
at the common tuning. All steps are pointwise in `k in K`; fix `k` and suppress it.

**Step 1 (the realized product is an honest group element).** By (C1) each realized factor
`S_j^{real}(zeta) = S^0_j(zeta) + Delta_j` with entry perturbation
`|Delta_j| <= C' (|A_j - a| + |B_j - b|) <= C' delta_1` (constants absorbed into `C_1`, `eps_c`) is an
element of the same `SU(1,1)`-type class as `eq:su11-random-product`: entrywise
`|A_j|^2 - |B_j|^2 = 1`. Induction over `j` (identical to the one-line argument at L1672–1676) gives

```
S_M^{real}(zeta_M) ... S_1^{real}(zeta_1) = [[A_M, conj(B_M)], [B_M, conj(A_M)]],
|A_M|^2 - |B_M|^2 = 1 ,
```

so the collapsed realized recursion `x_{p,M}^{real}(zeta) = (B_M(zeta) H + conj(A_M(zeta)) Id)^{-1} x_p`
(`eq:collapsed-vector-recursion` shape) is valid, and `|A_j| >= 1` for every partial product.

**Step 2 (drift and increment bounds under detuning).** Put
`tilde a_j := A_j`, `tilde b_j := B_j` (entries of the realized boost), `|tilde a_j - a| + |tilde b_j - b| <= delta_1`,
and `w_{j-1} := B_{j-1}/A_{j-1}`, `|w_{j-1}| < 1`. The increment of the height process is
`L_j - L_{j-1} = log| tilde a_j + conj(zeta_j) tilde b_j w_{j-1} |`.

*Drift.* Jensen's formula (as at L1703–1707) gives
`E_{zeta_j} log|tilde a + conj(zeta) tilde b w| = log|tilde a|`, since
`|tilde a|^2 - |tilde b|^2 >= 1 - 2 delta_1 (a + b) > 0` provided `delta_1 <= 1/(4(a+b))`. Hence

```
mu(k) := inf-cell conditional drift >= log a - c_a delta_1(k),
c_a := 2/a   (from |log|tilde a| - log a| <= |tilde a - a| / min(|tilde a|, a) and |tilde a| >= a - delta_1 >= a/2).
```

*Increment range.* Using `a + b = e^{rho}` and `a - b = e^{-rho}` (the denominator bound),
`|tilde a + conj(zeta) tilde b w| in [tilde a - tilde b, tilde a + tilde b]` with
`tilde a - tilde b >= e^{-rho} - 2 delta_1`, `tilde a + tilde b <= e^{rho} + 2 delta_1`, so for
`delta_1 <= e^{-rho}/4` (whence `tilde a - tilde b >= e^{-rho}/2`):

```
|L_j - L_{j-1}| <= log( 2(e^{rho} + 2 delta_1) / e^{-rho} )
                <= log( 4 e^{2 rho} ) = 2 rho + log 4 .
```

Define the fixed variance proxy `V_rho := max(rho, 2 rho + log 4) = 2 rho + log 4`; every increment lies
in `[-V_rho, V_rho]` **unconditionally**, and inside the headroom the drift is bounded below — exactly
the two inputs Azuma–Hoeffding needs.

**Step 3 (Azuma tail is `delta_1`-flat inside the headroom).** Impose the headroom condition

```
(HR)   delta_1(k) <= delta_* ,   delta_* := (1/2) min( a log a , 1/(4(a+b)) ) .
```

so that `mu(k) >= (1/2) log a` throughout. Every increment lies in `[-V_rho, V_rho]`; Azuma–Hoeffding
(the mechanism of `eq:effective-height-concentration` L1709–1714, with the fixed variance proxy
`V_rho`) gives, uniformly for all `k` with `delta_1(k) <= delta_*`,

```
P( L_M < (1/4) M log a ) <= exp[ - (M (log a)^2 / 4) / (8 V_rho^2) ]
                         = exp[ - M (log a)^2 / (32 V_rho^2) ] =: Tail(M) .
```

Note `Tail(M)` is **independent of `delta_1`**: the headroom absorbs the detuning, which is the source of
the flat band and, ultimately, of the `M`-independent constants.

**Step 4 (Poisson radius, `M`-uniform).** On the complementary (good) event, `|A_M| >= e^{M log a / 4}`,
so by `eq:effective-poisson-radius` (L1716–1719)

```
r_M >= sqrt( 1 - a^{-M/2} ) .
```

Let `r* in (0,1)` be the Dini threshold of the fixed compact singular family `mathfrak M`
(`sup_{nu in mathfrak M} Q_{r*}(nu) <= q/2`; existence exactly as at L1722–1726, via
`thm:strong-barrier` L466 ff. and `cor:strong-bundle` L510–521). Choose

```
M >= M_1(rho, q, mathfrak M) := ceil( 2 log( 1/(1 - r*^2) ) / log a ) ,
```

so that `sqrt(1 - a^{-M/2}) >= r*` — a condition **independent of `k` and `delta_1`** inside the
headroom. (Larger `M` buys *more* headroom: the radius lower bound improves with `M` at fixed
`delta_1 <= delta_*`.)

**Step 5 (Poisson identity and assembly in the flat band).** The identity
`eq:random-product-poisson-identity` (L1685–1692) holds verbatim for the realized product: its proof
used only (i) the `SU(1,1)` structure (Step 1), and (ii) Haar-invariance of the fresh collar phases under
the simultaneous rotation argument (L1677–1682) — and fresh collars are Haar by construction of the
placement average. Hence, with `nu_p` the normalized spectral measure of `(Theta_W(k), x_p/||x_p||)`,

```
int_{T^M} || x_{p,M}^{real}(zeta) ||^{2 beta} dm^M(zeta)
   = ||x_p||^{2 beta} * E_{zeta} [ ( int_T |B_M h + conj(A_M)|^{-2} d nu_p (h) )^beta ]
   = ||x_p||^{2 beta} * E[ Q_{r_M}(nu_p) ] .
```

On the good event `r_M >= r*`, so `Q_{r_M}(nu_p) <= Q_{r*}(nu_p) <= q/2` (monotonicity of `Q_r` in `r`);
on the bad event the integrand is at most `1` and the probability is at most `Tail(M)`. Choosing `M`
also so large that `Tail(M) <= q/2`, we obtain for **every** `k` with `delta_1(k) <= delta_*`:

```
int_{T^M} sum_p || x_{p,M}^{real}(zeta, k) ||^{2 beta} dm^M(zeta)
   <= ( q/2 + q/2 ) sum_p ||x_p(k)||^{2 beta} = q * sum_p ||x_p(k)||^{2 beta} .
```

This is the sharp flat band: no response term whatsoever.

**Step 6 (outside the band: explicit linear envelope under the Hardy cap).** For general `k in K`,
repeat Steps 3–5 with the *degraded, still explicit* quantities
`mu(k) = log a - c_a delta_1(k)` (nonnegative whenever `delta_1(k) < a log a`),
`Tail_k = exp[ - M mu(k)^2 / (8 V_rho^2) ]`, `r_M(k) >= sqrt(1 - e^{-M mu(k)})`:

```
factor(k) := ||x_p||^{-2 beta} int_{T^M} || x_{p,M}^{real}(zeta, k) ||^{2 beta} dm^M(zeta)
          <=  Tail_k + sup_nu Q_{r_M(k)}(nu).
```

Define the nondecreasing response

```
Psi(delta) := sup{ ( Tail_k + sup_{nu in mathfrak M} Q_{ sqrt(1 - e^{-M mu(k)}) }(nu) - q )^+ :
                   k in K with delta_1(k) <= delta } ,
```

then `Psi(delta_*) = 0`, `Psi` is nondecreasing and bounded by `1`, and
`factor(k) <= q + Psi(delta(k))` for every `k`. Finally, the **exact Hardy cap**: each realized cell
satisfies the flux identity (C1), so `lem:physical-hardy` (L1058–1118) applies at every `k` to every
factor; iterating over the `M` cells,

```
int_{T^M} sum_p ||x_{p,M}^{real}(zeta, k)||^{2 beta} dm^M(zeta) <= sum_p ||x_p(k)||^{2 beta}
```

**always** — the realized family is never expansive in fresh-collar phase mean, on all of `K`, at any
detuning (this is the pointwise-in-`k` protection mechanism of AR A/B). Therefore `factor(k) <= 1`
unconditionally, and the linear law `(+)` holds on all of `K` with the explicit constant

```
C_2 := (1 - q) / delta_* ,      delta_* = (1/2) min( a log a , 1/(4(a+b)) )
                               = (1/2) min( cosh(rho) log(cosh rho) , 1/(4 e^{rho}) ) :
```

for `delta(k) >= delta_*` the right side `q + C_2 delta >= q + (1 - q) = 1 >= factor(k)` holds by the
Hardy cap; for `delta(k) <= delta_*` Step 5 gives the sharper `<= q`; in between, `Psi` is dominated by
the secant slope because `Psi(t) = 0` for `t <= delta_*` and `Psi <= 1`, whence
`sup_{t > 0} Psi(t)/t = sup_{t >= delta_*} Psi(t)/t <= 1/delta_* = C_2`. (One may take this smaller
secant constant instead; the explicit value above suffices for every downstream use, since the ledger
only ever evaluates `C_2 delta` on windows where it is required to be small.)
`square`

**Remark A.1 (why the constant does not depend on `M`).** Three mechanisms conspire: (i) the Azuma tail
inside the headroom uses the *fixed* variance proxy `V_rho` and drift `(1/2) log a` — the detuning is
absorbed by the headroom, not propagated; (ii) the Poisson-radius floor `r_M >= sqrt(1 - a^{-M/2})`
*improves* with `M`, so the barrier threshold `r*` is met `M`-uniformly; (iii) outside every band the
Hardy cap `<= 1` truncates the response, and `C_2 = (1 - q)/delta_*` is a number depending on `rho`
alone. The exponential `e^{rho M}` of naive operator telescoping (Section 2.2(e)) never enters, because
the comparison is performed in the drift/barrier engine, not on raw products.

**Remark A.2 (beta-dependence).** `beta` enters (i) the reachability of `q` by the engine
(`M_1`, `r*` depend on `(beta, mathfrak M)` through the Dini step, exactly as in the Note), and (ii) the
integrated fractional bookkeeping, where coefficient errors of size `err` contribute `O(err^beta)` to the
density (`lem:compact-output-stability`, L885–887: "|difference in the beta-fractional density is bounded
by the beta-th power"; used identically in `lem:window-cost`'s proof, L1376–1382). The multiplicative
chromatic coefficient `C_2 C_1` itself is `beta`-independent.

**Remark A.3 (effectivity).** `r*` (hence `M_1`) is obtained by Dini's theorem on the fixed compact
family `mathfrak M`: finite but without rate — the same effectivity status as the group lengths `M_l`
of the Note's own one-window proof (AR D, effectivity note: "Existence suffices for Theorem 6 and for the
assembly"). Under MAIN_ATTEMPT Lemmas 1–2 (conditional on Gap G1) the barrier step is polynomially
effective and every constant becomes effective; nothing below uses this.

### 2.4 Corollary A (lem:window-cost unconditional; the width law)

**Corollary A.** In `lem:window-cost` (L1356–1389) the hypothesis "Suppose a depth-`m` cell has
chromatic error `C m |k/k_* - 1| + eps` and reflector cost `C_rho e^{-c m}`" is **discharged**: by
Lemma A a depth-`m`, length-`M` group tuned at `k_*` has, for `q = 1/2`, the certified window law

```
factor_I <= 1/2 + C_2 ( C_1 M m |I| * 2/kappa_K + M eps_c )        (I an interval through k_*),
```

i.e. a certified half-width `h >= eta kappa_K / (2 C_2 C_1 M m)` for tolerance `eta` at fixed
`eps_c`-share — the block law `C M m |k/k_* - 1| + M eps` with `C = 2 C_2 C_1 / kappa_K` explicit in
`(rho, beta, K)` (via `C_1`, `C_2`; the `beta`-power appears when the law is integrated, L1376–1382).
Consequently `lem:window-cost` holds with "cell" replaced by "group" throughout its proof, the window
count `N_m <= C_K A_rho m zeta^{-1/beta}` becomes `N_m <= C_K A_rho M m zeta^{-1/beta}` for the group,
and MAIN_ATTEMPT §7 Steps 3 and 6 rest on proved law. `square`

---

## 3. Theorem 6′ (per-probe finite broadband synthesis) — closes GAP H

### 3.1 Statement

**Theorem 6′.** Let `(W, x_1, ..., x_P, K)` be a state (`P` finitely many targeted probes), let
`0 < beta < 1`, and let `zeta > 0`. Then there exist

* finitely many generations `g = 1, ..., 3P`, each consisting of finitely many groups of smooth real
  scalar reciprocal cells of Riesz depth `m`, placed on **pairwise disjoint fresh radial shells**
  (successively, one prescribed inner radius each, disjoint from all previous supports),

such that, after all `3P` generations are assembled:

1. **(Per-probe contraction.)** For *every* probe `p in {1, ..., P}`,

```
int_K w_p^{beta, new} dk  <=  (27/64) int_K w_p^{beta, old} dk + zeta/10
                           <=  (1/2)  int_K w_p^{beta, old} dk + zeta/10 ,
```

   where `w_p^{beta, old}`, `w_p^{beta, new}` are the targeted beta-fractional densities before and
   after the whole `3P`-generation block. (Single-mode variant: running **one** generation per probe
   (`3P` replaced by `P`) gives the literal per-probe `3/4 + zeta/10` demanded by
   `prob:physical-grouped-global`'s phrasing.)

2. **(Protection.)** Every protected fractional moment (all `q != p` probes' moments on **all of `K`**,
   at every generation), every declared witness lock, and every protected continuous spectral test is
   nonexpansive, respectively moved, by at most its allocated share of `zeta` (total `<= zeta/10` per
   functional over the whole block).

3. **(Ledger.)** The total `X_3` cost of the block is at most `zeta`, all cells obey **one** pointwise
   amplitude bound depending only on `rho`, and all supports are pairwise disjoint.

Generation `g = 3(p-1) + s` (`s = 1, 2, 3`) is **aimed exclusively at probe `p`**: its targeted list is
`{x_p}` and its protected list is
`{ moments of x_q, q != p } union {declared witness locks} union {continuous tests}`.

### 3.2 Proof

**Step 0 (why the quantifier mismatch dissolves).** The one-window proposition
`prop:physical-grouped-one-window` (L1993–2065) contracts "*the sum of the targeted beta-fractional
moments on `I`*" (L2002–2003) — an aggregate over the targeted list. When the targeted list has
cardinality one, the sum-level statement **is** the per-probe statement. This single observation is the
repair mandated by AR items E/H: instead of one generation aimed at many probes, run one generation per
(probe, repetition) pair. Nothing else in the architecture changes; in particular the audit PASS items
A/B/C/D/F are consumed in their original form.

**Step 1 (schedule and freshness).** Fix the order of probes. Generation `g` is placed after generation
`g-1` with prescribed inner radius equal to the current outer radius ("successive disjoint shells",
L7734, MA330–333); the one-window proposition accepts any prescribed inner radius (L1998–1999). Supports
of distinct generations are therefore pairwise disjoint, and the pointwise amplitude ledger of the whole
block is a **maximum**, not a sum, over generations (AR G, amplitude bullet; `lem:bounded-reflector`
L1290–1293: no copy exceeds the fixed bump height; weak-slab amplitudes `T^{-1}||w||_2 -> 0`).

**Step 2 (construction of one aimed generation).** Fix `g = 3(p-1) + s`, current state
`(W_g, x_1^{(g)}, ..., x_P^{(g)}, K)` (`W_g = W +` sum of previously placed potentials; `x_p^{(g)}` the
current radiation vectors). Apply the one-window machinery with targeted list `{x_p}`:

* *(Cover.)* Exactly as MAIN_ATTEMPT §7 Step 1 (MA298–308): the assignment `k* -> V(k*)` of open
  FSM-valid neighbourhoods (`lem:finite-spectral-model` L1953–1991, built with recursion length
  `T = M(k*)` from the next bullet) covers `K`; compactness extracts a finite subcover centred at
  `c_1 < ... < c_L`, subsequently intersected with the chromatic windows of Lemma A/Corollary A.
  **No uniform width lower bound is used or produced** (AR C); the cover is planned against the one
  fixed current bundle of this generation.
* *(Stratum disposal and group lengths.)* Choose `tau > 0` killing the small-norm stratum
  (`||x_p^{(g)}(k)|| < tau`, total initial fractional moment below the allocated error; L2016–2018,
  L2027–2029, exact Hardy nonexpansion). On the closed stratum the normalized pairs
  `(Theta_{W_g}(k), x_p^{(g)}(k)/||x_p^{(g)}(k)||)` form a compact bundle with all associated spectral
  measures singular (Step 3), so `thm:singular-bundle-grouped-contraction` (L1632–1739) fixes a finite
  length `M_l` per closed window **before** any model is introduced (order of quantifiers L2042–2044).
* *(Realization and widths.)* At each centre: FSM with `T = M_l` (L2031–2034); block-Talbot closeness to
  the boost (`prop:full-block-talbot`); compact-output stability, reflection gap, one safety enlargement
  (L2038–2041); depth `m_l` chosen **last**, after the finite `M_max` of this generation, so that
  `L M_max C_rho e^{-c m_l} <=` share (MA361–364) — legitimate because Lemma A/Corollary A now supply
  the block chromatic law that `lem:window-cost` previously carried as hypothesis. Certified half-width
  per window `>= eta_l kappa_K / (2 C_2 C_1 M_l m_l)` (Corollary A); shrink the cover member to match —
  Step 1 of the cover kept it adjustable (MA325–326).
* *(Placement and protection.)* Free collar frequencies chosen successively; `lem:one-step-placement`
  (L640–674) realizes **all** inequalities simultaneously — the targeted integral accuracies on each
  `I_l`, **and** the global protected list of generation `g`: every `q != p` probe's fractional moment on
  all of `K`, every declared witness lock, every protected continuous test (L2046–2054; AR A.4: one `nu`
  locks all finitely many functionals; thresholds are finite maxima; growing frequency lists across
  generations are admissible at no charged cost — AR A.3). Protection rests on the *exact*
  pointwise-in-`k` identity `int_T F_z^* F_z dm = Id` (`lem:physical-hardy`, L1070–1081), which is
  insensitive to detuning: off its own windows a group is phase-mean-nonexpansive on all of `K` up to the
  placement epsilon only (`rem:physical-hardy-meaning` L1120–1134). Buffer/Schur/Galerkin residuals are
  uniform on `K` (`prop:explicit-buffer-stability` L1185–1210, sup over `k in K`, scaled by `||f||^2`),
  budgeted per group.
* *(Cost, amplitude, buffers.)* `X_3` per group `<= C_rho e^{-c m_l} +` weak-slab and residual shares
  (`lem:window-cost` unconditionally, via Corollary A; `lem:scale-compatibility` meets all finite
  requests without touching the reflector cost, L1332–1334); the closing scale order is
  `eq:physical-buffer-target` (L7702–7708) with the Galerkin condition of
  `prop:explicit-buffer-stability`. One amplitude bound `rho` for all cells of the block.

**Step 3 (re-certification of singularity for each new aim — explicit).** Before generation `g`, two
independent certificates establish that every spectral measure of the current pair
`(Theta_{W_g}(k), x_p^{(g)}(k)/||x_p^{(g)}(k)||)` is singular:

*(Certificate S1 — structural, vector-agnostic).* `W_g` is a finite sum of smooth real compactly
supported potentials, hence smooth, real, compactly supported. `rem:phase-criterion` (L528–568) applies
verbatim: stationary representation with smooth on-shell kernel (L555–561) gives
`Theta_{W_g}(k) - Theta_0(k) in mathfrak S_1` (L536–540); the free phase `Theta_0(k)` is diagonal in
spherical harmonics, hence pure point (L563–564); the unitary Kato–Rosenblum theorem (L564–566) kills the
absolutely continuous subspace; therefore **every** vector spectral measure of `Theta_{W_g}(k)` is
singular, and norm-continuity in `k` on compacts (L566–567) makes the bundle compact so that
`cor:strong-bundle` (L510–521) applies uniformly. This certificate neither knows nor cares which probe is
aimed at; it re-fires at **every** generation.

*(Certificate S2 — dynamical, along the placed trajectory).* The current radiation vectors are the
initials composed with the placed groups' transfer factors — **fractional (Mobius/fractional-linear)
transformations**: at the vector level, `x_p^{(g)}(k) = (B H + conj(A) Id)^{-1}`-compositions
(`eq:collapsed-vector-recursion` L1732–1736, recursion shape L682–687 and `eq:grouped-X-recursion`
L1542–1547); at the measure level, the spectral measure of the updated pair is the normalized pushforward

```
mathcal T_g nu = (Psi_g)_* ( |B h + conj(A)|^{-2} nu ) / int_T |B h + conj(A)|^{-2} d nu(h)
```

(`eq:su11-boundary-action`, `eq:su11-spectral-measure-action` L1827–1836). `Psi_g` is a Mobius map,
smooth with smooth inverse on the complement of its pole `h = -conj(A)/B` (which lies in `T` only when
`B > 0`; the pole is not charged by the absolutely continuous weighting, since
`|B h + conj(A)|^{-2} nu` is a finite measure carried off that point), and it maps the torus onto itself.
Hence `mathcal T_g nu` is supported on the image under `Psi_g` of `supp(nu)`, and the image of a
Lebesgue-null set under a smooth map is null. **A normalized pushforward of a singular measure is
singular.** Induction over the finitely many placed cells of all
previous generations (the atomicity induction of MAIN_ATTEMPT Lemma 1, MA97–122, which needs no
finite-dimensionality for the singularity statement proper) gives: singular at every stage, for every
probe, along the actual placed trajectory. (This also insulates the aims against the Mobius-orbit
phenomenon `prop:mobius-orbit-haar-obstruction` L1819–1951: that obstruction defeats *uniformity of `M`
over prior ideal histories*, not per-state re-certification — AR C, Thread C, and AR D.)

Either certificate suffices; the construction uses S1 (it feeds `cor:strong-bundle` directly) and records
S2 as the trajectory-level consistency check demanded by the repair specification.

**Step 4 (per-probe moment ledger across its three aimed generations).** Fix probe `p` and consider its
three consecutive aimed generations. Within one aimed generation, on each cover window `I_l` (centre
`k^{(l)}_*`, half-width `h_l`) the realized contraction is, by Lemma A with `q = 1/2` followed by the
placement lock,

```
int_{I_l} w_p^{beta, out} dk
   <= ( 1/2 + rho_l ) int_{I_l} w_p^{beta, in} dk + (additive share)_l ,
rho_l := C_2 ( 2 C_1 M_l m_l h_l / kappa_K + M_l eps_c^{(l)} ) ,
```

where the multiplicative degradation `rho_l` comes from the chromatic response (converted to density
level through the beta-power bound, L885–887) and the additive `(share)_l` collects the
placement/residual/buffer epsilon. Since the cover is **finite**, choose the widths `h_l` — after the
lengths `M_l`, depths `m_l`, and accuracies are fixed — so that `max_l rho_l <= 1/8`; this is possible
because each certified width is positive (AR C) and shrinking a window keeps it inside its open
FSM-valid neighbourhood. Summing over the cover (which is all of `K`) with the common factor
`gamma_g := max_l rho_l <= 1/8`:

```
int_K w_p^{beta, out} dk <= (1/2 + gamma_g) int_K w_p^{beta, in} dk + e_g ,
e_g := sum_l (additive share)_l  <=  the generation's additive allocation .
```

(the slack arithmetic `1/2 + 1/8 <= 5/8 <= 3/4 - 1/8` mirrors MA354–359), i.e. per aimed generation
the realized factor is at most `5/8 + o(1)` — a fortiori `3/4 + o(1)`. Three consecutive aimed
generations compose **multiplicatively** in their factors (each generation's output density is the next
one's input); additivity of the epsilon shares gives

```
int_K w_p^{beta, after} dk
   <= ( prod_{s=1}^{3} (1/2 + gamma_{g_s}) ) int_K w_p^{beta, before} dk + e^{(p)}
   <= (5/8)^3 int_K w_p^{beta, before} dk + e^{(p)}
    = (125/512) int_K w_p^{beta, before} dk + e^{(p)}
   <= (27/64) int_K w_p^{beta, before} dk + e^{(p)} ,
```

with `e^{(p)}` the accumulated additive shares of the three generations (`<= 3` generation shares).
Since `125/512 = 0.244... < 27/64 = 0.421875 < 1/2`, this is `<= (1/2) int_K w_p^{beta, before} dk +
e^{(p)}` — the per-probe delivery of `eq:dovetail-contract`.

**Step 5 (non-revocation: later generations do not revoke earlier probes' contractions).** After probe
`p`'s third aimed generation, every later generation `g'` (aimed at `q != p`) carries `x_p`'s moment in
its **protected list**. By Step 2's placement bullet and the pointwise-in-`k` Hardy identity, generation
`g'` changes `int_K w_p^beta dk` by at most its protection share: it is phase-mean-nonexpansive in `zeta`
(mean preserved exactly) and deterministic placement realizes the mean up to the share; residuals are
uniform on `K` and budgeted. Hence later generations "merely fail to improve" earlier certificates
(MA340–342; AR D(iii)). Combining with Step 4: after the whole block,

```
int_K w_p^{beta, new} dk <= (27/64) int_K w_p^{beta, old} dk + e^{(p)} + sum_{g' > 3p} share_{g'}
```

— all error terms are allocated shares of `zeta`, totaling `<= zeta/10` per probe by the bookkeeping of
Step 6.

**Step 6 (global bookkeeping over the triangular schedule).** In the assembly
(`prop:conditional-counterexample-final`, L7724–7748), stage `j` invokes Theorem 6′ with `P = j` probes
and stage budget `eps_j = 2^{-2j}` (L7728–7729). Allocation:

| Item | Share |
|---|---|
| per generation `g` of stage `j` (placement + residuals + buffer + `X_3`) | `eps_j / (10 * 3j)` |
| stage-`j` total (`3j` generations: probes `1..j`, three aims each) | `<= eps_j / 10 <= eps_j` |
| per probe `p <= j` at stage `j`: own aims (`3`) + protection through other aims (`3(j-1)`) | `<= 3j * eps_j/(10*3j) = eps_j/10` |
| per witness lock at stage `j` | `eps_j/(10*3j)`, total future error `sum_j eps_j/(30j) < infinity` |

Summability over stages: `sum_j eps_j = sum_j 2^{-2j} < infinity`, whence
`||V||_{X_3}^2 <= sum_j 2^{-2j} < infinity` (`eq:counterexample-X3-cost` L7736–7739) — the triangular
schedule `tau(j)` (L764–769) is respected and every error stream is summable.

**Step 7 (compatibility with `thm:scalar-dovetail`, L771–802).** At stage `j`, Theorem 6′ delivers, with
`I_{p,j} = int_K w_{p,j}^beta dk`:

* `eq:dovetail-nonexpand` (L781–782): for all `p <= j`,
  `I_{p,j} <= (27/64) I_{p,j-1} + eps_j/10 <= I_{p,j-1} + eps_j`. ✔ (Delivered by Steps 4–5: every
  active probe is either contracted by its own tripled aim or protected through the other aims; in both
  cases nonexpansive up to `eps_j`.)
* `eq:dovetail-contract` (L783): for `p = tau(j)`,
  `I_{tau(j), j} <= (27/64) I_{tau(j), j-1} + eps_j/10 <= (1/2) I_{tau(j), j-1} + eps_j`. ✔
  (Delivered by the tripled aimed generations; `27/64 < 1/2` replaces the assembly's external tripling
  sentence at L7731–7732 — that sentence is subsumed, and the proposition's hypothesis "Problem
  `prob:physical-grouped-global` holds at every finite stage" is consumed in its per-probe reading.)
* `eq:dovetail-moments` (L788–792): the first `j` continuous tests of the first `j` densities are in
  every generation's placement list with share `eps_j/(10*3j)` each; entrywise stage error
  `<= eps_j/10 <= eps_j`. ✔
* Witness freezing (L794–796): a witness declared at stage `j` for probe `p` enters every later finite
  test list (all `3j'` generations of stages `j' > j`) with prescribed shares whose total future error
  `sum_{j' > j} eps_{j'}/(10*3j') <= sum_{j'>j} 2^{-2j'}/10` is summable and prescribable. ✔

By `thm:scalar-dovetail` (proof L804–836: geometric drift along the infinitely many aiming stages with
error tails `2^{-2q}`, Cauchy moments via the dense sequence, permanent witness locks, support on the
null set `S = cup_p S_p`) and `cor:dense-probes` (L839–853), the exterior absolutely continuous
projection on `K` vanishes.

**Step 8 (carriers, crowding, smoothness ratchet — why nothing binds).** The collar-frequency lists grow
across the `3j` generations of a stage and across stages; `lem:scale-compatibility` (L1311–1354) orders
the scales so the carrier is chosen after the masks, at no charged `X_3` or amplitude cost, so crowding
is impossible (AR A.3). The Lipschitz ratchet `Lambda_{j+1} >= c Lambda_j / eps_{j+1}` (MA66–75) degrades
smoothness of the data bundles, never feasibility: Lemma A's law contains **no history term** (the
per-generation cover is planned against the current bundle, and the chromatic width
`eta kappa_K/(2 C_2 C_1 M m)` is insensitive to `Lambda`), so Theorem 6′ is robust to either reading of
Gap G2 (MA84–93) — the modulus, wherever it bites, is absorbed into the per-generation window widths,
which require positivity only, never uniformity. `square`

### 3.3 Where each audit PASS item is consumed

| Audit item | Consumed at |
|---|---|
| A (global protection via pointwise Hardy + simultaneous placement + no crowding) | Steps 2 (placement bullet), 5, 8 |
| B (off-window nonexpansive; uniform residuals; no cross-window contraction channel) | Steps 4–5 |
| C (width positivity at any `zeta`; no proved shrinkage force; obstructions attach to adaptive route) | Step 2 (cover bullet), Step 8 |
| D (re-certification S1/S2; compact bundle; non-revocation; effectivity note) | Steps 2–3, 5 |
| F (no hidden radialization/lens/outward-budget dependence) | Section 5–6 below |

---

## 4. Corollary 6″ (final): the global problem and the conditional counterexample

**Corollary 6″.** *Granting the Note's proved layer exactly as itemized in Section 5 (and nothing else):*

**(a) Per-probe global synthesis.** `prob:physical-grouped-global` (L2067–2083) holds in the per-probe
form: one stage's block of generations contracts **every** targeted fractional moment on **all of `K`**
by a factor at most `27/64 + o(1) <= 1/2 + o(1)` (single-mode: `3/4 + o(1)` per generation), preserves
the finite protected list up to the allocated errors, and has total `X_3` cost at most the stage budget
with one pointwise amplitude bound. The "remaining issue" flagged at L2076–2079 (no finite-cover lower
bound on widths) does not bind: no uniform width lower bound is used — each generation's cover is
extracted from compactness of `K` against that generation's own fixed bundle (AR C).

**(b) Activation.** `prop:conditional-counterexample-final` (L7712–7748) applies at every finite stage,
with its tripling sentence (L7731–7732) subsumed by Theorem 6′'s internal tripled schedule: there exist a
bounded real `V in X_3` and a nonempty compact `K Subset (0, infinity)` such that

```
P_ac(-Delta + V) 1_K(-Delta + V) = 0        (eq:final-counterexample, L7717–7719),
||V||_{X_3}^2 <= sum_j 2^{-2j} < infinity   (eq:counterexample-X3-cost, L7736–7739).
```

The proof of the proposition is otherwise unchanged: dense probe selection (L7725), strong-resolvent
identification of the weakly locked limits with the summed potential's spectral measures (shells disjoint,
`X_3`-summable, so `V_n -> V` in `X_3 cap L^\infty_loc`; truncation lemma S346–387), and transfer of
`P_ac 1_K = 0` from the exterior Dirichlet operator to the whole-space operator by completeness of local
wave operators under compactly supported recoupling (L7741–7748).

**(c) Falsity of Simon's multidimensional `L^2` conjecture (`d = 3`).** With
`H = -Delta + V` (`eq:H` S230–235) and `V in X_3` bounded, real (hence
`int_{R^3} |x|^{1-3} |V|^2 dx = ||V||_{X_3}^2 < infinity`), the conjecture (`eq:simon` S248–253;
Simon 2019, Conjecture 20.2) demands `m_ac(E; H) = infinity` for Lebesgue-a.e. `E > 0`. But
`P_ac(H) 1_K(H) = 0` on the nonempty open-interior compact `K` forces `m_ac(E; H) = 0` for a.e.
`E in K`. Hence the statement

> "`int |x|^{-nu+1} |V(x)|^2 dx < infinity` implies absolutely continuous spectrum of infinite
> multiplicity on `[0, infinity)` a.e."

is **FALSE for `nu = 3`** (`d = 3`), conditionally on the proved layer of Section 5. `square`

---

## 5. LOAD-BEARING DEPENDENCE LIST (complete)

Every result of the source corpus on which the chain
**Lemma A -> Theorem 6′ -> Corollary 6″** relies, with live locations and roles. Anything not listed is
not used; Section 6 lists the explicitly avoided items.

### From the Note (`operator_valued_riesz_singularity_note.tex`)

| # | Label | Lines | Role in this document |
|---|---|---|---|
| 1 | `rem:phase-criterion` | L528–568 | Singularity re-certification S1 at every generation (trace class, Kato–Rosenblum, norm continuity). |
| 2 | `thm:strong-barrier` | L466–509 | Poisson barrier `Q_r(nu) downarrow 0` for singular `nu`; source of the Dini threshold `r*`. |
| 3 | `cor:strong-bundle` | L510–521 | Uniform barrier over the compact finite-probe bundle; invoked via the one-window proof. |
| 4 | `lem:hardy` | L303–326 | Zeroth Fourier coefficient in the placement lemma's proof (L670–671). |
| 5 | `thm:finite-contraction` | L328–334 | Zeroth Fourier coefficient bound `kappa_{beta,n}` in the placement lemma's proof (L669–670). |
| 6 | `thm:scalar-dovetail` | L764–837 | Dovetail bookkeeping: schedule, `eq:dovetail-nonexpand/-contract/-moments`, witness freezing, singularity conclusion. |
| 7 | `cor:dense-probes` | L839–853 | Dense probes => `P_ac(H) 1_K(H) = 0`. |
| 8 | `lem:one-step-placement` | L640–674 | Deterministic simultaneous placement of all targeted and protected functionals (finitely many, one `nu`). |
| 9 | `lem:compact-output-stability` | L865–903 | Residual-to-output transfer; `(a-b)^{-1} = e^{rho}` (L896); beta-power density error (L885–887). |
| 10 | `lem:reflection-gap` | L919–934 | Uniform inverse bound `(1 - t)^{-1}`; factorization; chromatic-free gap input (C4)-adjacent. |
| 11 | `lem:physical-hardy` | L1058–1118 | Exact pointwise-in-`k` protection identity `int_T F_z^* F_z dm = Id`; the Hardy cap in Lemma A Step 6; global nonexpansion. |
| 12 | `rem:physical-hardy-meaning` | L1120–1134 | Off-window semantics: preservation without strict contraction; detuning-insensitivity. |
| 13 | `lem:schur-stability` | L1156–1183 | Schur-complement bound behind the buffer estimate. |
| 14 | `prop:explicit-buffer-stability` | L1185–1210 | Outgoing-buffer residuals uniform on `K` (sup over `k`); density version scaled by `||f||^2`. |
| 15 | `eq:product-laplacian`, envelope error | L1234–1247 | Product identity and `O(L)` envelope terms feeding the block Talbot proposition. |
| 16 | `prop:full-block-talbot` | L1254–1278 | Block-level Talbot closeness and Riesz concentration/refocusing on finite-dimensional classes (non-zonal). |
| 17 | `lem:bounded-reflector` | L1280–1309 | Boost realization; profile Cartan bound `rho + C_0`; amplitude bound; cost `C_rho`. |
| 18 | `lem:scale-compatibility` | L1311–1354 | Scale ordering; carrier after masks; uncharged carriers/radii/cutoffs; no crowding. |
| 19 | `lem:window-cost` | L1356–1389 | Cost bookkeeping (used with its hypothesis now discharged by Lemma A/Corollary A). |
| 20 | `eq:grouped-X/H-recursion` | L1542–1547 | Grouped ideal recursion (recursion shape for placed trajectories). |
| 21 | `thm:singular-bundle-grouped-contraction` | L1632–1739 | The engine: finite group length from the compact singular bundle; `eq:singular-bundle-product-contraction` L1649–1657; `eq:singular-vector-bundle-contraction` L1662–1666. |
| 22 | `eq:su11-random-product`, `eq:su11-hyperbolic-identity` | L1640–1647, 1672–1676 | Group structure of products (reused in Lemma A Step 1). |
| 23 | `eq:random-product-poisson-identity` | L1685–1692 | Phase-mean identity reused verbatim for realized products (Lemma A Step 5). |
| 24 | `eq:positive-radial-drift`, `eq:effective-height-concentration`, `eq:effective-poisson-radius` | L1704–1719 | Jensen drift, Azuma tail, radius floor — the `M`-uniform constants of Lemma A Steps 2–4. |
| 25 | `eq:collapsed-vector-recursion` | L1732–1736 | Collapsed Mobius action of a placed group on vectors (re-certification S2). |
| 26 | `eq:su11-boundary-action`, `eq:su11-spectral-measure-action` | L1827–1836 | Normalized pushforward of spectral measures (re-certification S2). |
| 27 | `lem:finite-spectral-model` | L1953–1991 | Finite spectral model; openness of the valid neighbourhood (cover construction). |
| 28 | `prop:physical-grouped-one-window` | L1993–2065 | The per-generation workhorse: window contraction `1/2` up to `zeta`, protection, cost, amplitude, prescribed inner radius. |
| 29 | `prob:physical-grouped-global` | L2067–2083 | The target problem (delivered in per-probe form). |
| 30 | `eq:exact-jost-shell-update-final` | L7691–7698 | Exact radial composition; provenance of flux exactness (C1). |
| 31 | `eq:physical-buffer-target` | L7702–7708 | Closing scale order of each generation. |
| 32 | `prop:conditional-counterexample-final` | L7712–7748 | The assembly (activated; tripling subsumed). |

### From the zonal layer (`fixed_potential_riesz_counterexample.tex`)

| # | Label | Lines | Role |
|---|---|---|---|
| 33 | `prop:scalar-reciprocal-riesz-cell` | F111–143 | Realized cell: existence, disjoint supports, cost `C_rho e^{-cm} + eps`, collar phase with arbitrarily large `vartheta'`. |
| 34 | `eq:physical-riesz-cell-chromatic-error` | F124–128 | Single-cell chromatic law `C_{K,K} m |s-1| + eps` (input (C3)). |
| 35 | `eq:long-weak-mask-transmission/reflection` | F150–157 | Weak-slab ledger; `k`-independent remainders (smoothness audit §2.2(a)). |
| 36 | `prop:zonal-talbot-factor` | F546–570 | Per-flight Talbot asymptotics; `eq:talbot-chromatic-bound` F566–568 (`C|s-1|` per flight). |
| 37 | `prop:talbot-riesz-concentration` | F593–624 | Depth-`m` train laws; `eq:riesz-chromatic-error` F618–622 (linear-in-`m` telescoping — input (C3)). |

### From the companion programme (`simon_fcen_new_attack_program.tex`)

| # | Label | Lines | Role |
|---|---|---|---|
| 38 | `eq:H`, `eq:Xd`, `eq:polar-cost` | S230–247 | Operator, `X_d` cost, polar form (statement of the class `V in X_3` bounded real). |
| 39 | `eq:simon` | S248–253 | Simon's Conjecture 20.2 — the statement falsified. |
| 40 | truncation lemma (referenced AR G) | S346–387 | Strong-resolvent identification of the staged sums. |

### From this settlement (inputs of record)

| # | Source | Role |
|---|---|---|
| 41 | `settlement/attack-hazard/MAIN_ATTEMPT.md` §7 (Theorem 6) | Architecture consumed; superseded per-probe by Theorem 6′. |
| 42 | `settlement/attack-hazard/MAIN_ATTEMPT.md` Lemmas 1–2 (MA97–163) | Atomicity induction for S2 (singularity part only — no rate used). |
| 43 | `settlement/audit-theorem6/AUDIT_REPORT.md` items A–H | Verification charter; PASS items consumed per §3.3; repairs E.1/H.1 executed here. |

---

## 6. EXPLICIT NON-DEPENDENCES

The chain above uses **none** of the following; any failure or circularity confined to them does not
touch the repair:

* **Lens / radialization machinery.** `thm:sphere-finite-frame-compiler`, `prop:uniform-adiabatic-lens-compilation`,
  `prop:outward-angular-time-budget`, `prob:short-time-radial-compiler` — absent from the transitive
  closure (AR F string-search; truth-ledger partition accurate). No circular dependence on the open
  radialization problem.
* **The hazard/adaptive route.** `prop:adaptive-centre-averaging` (L2085–2124), `eq:hazard-divergence`
  (L2119–2122), `cor:exact-hazard-bottleneck` (L2139–2158), MAIN_ATTEMPT Theorems 4–5, and Gaps
  G1/G2 — bypassed entirely; Theorem 6′ never adapts across states.
* **Adversarial obstructions.** `prop:no-uniform-chromatic-modulus`, `prop:coverage-obstruction`,
  `prop:grouped-root-zeno`, `prop:mobius-orbit-haar-obstruction` — all proved, all attaching to
  *uniformity over bundles/histories* or to summable-width iteration; the one-shot per-generation covers
  and per-state re-certification engage none of them (AR C, Thread C; AR D).
* **Commented-out text.** `prop:one-window-cell` / `prop:local-adapted-squeeze` (L7411–7481, `\iffalse`)
  are used only as *derivational evidence* for (C3) (the differentiation step L7471–7473); the live
  discharge of (C3) is F124–128/F618–622 plus §2.2(a). See R3.

---

## 7. Residual conditions and provenance notes (non-blocking)

* **R1 (flux-exactness provenance).** Exactness of `A^*A - B^*B = Id` for the *realized* pairs at every
  `k` is inherited structurally via `eq:exact-jost-shell-update-final` (L7691–7698) and the stability
  lemmas; the Note proves it for the model pair. Referee-of-record citation locus, as AR A recommends —
  a provenance note, not a gap.
* **R2 (effectivity).** `M_l`, `r*`, `M_1` arise from Dini's theorem on fixed compact families: finite,
  ineffective — the program's accepted standard for the synthesis route (AR D, effectivity note). Under
  Gap G1's verification, MAIN_ATTEMPT Lemmas 1–3 upgrade everything to polylogarithmic effectiveness;
  not needed here.
* **R3 (presentational debt).** The full-block *cell assembly* statement (`prop:one-window-cell`) lives
  in commented-out text; the live ingredients (item 16 + 9/10 + 17 + 18) suffice for every use made of
  (C2)–(C4) here (AR F caveat). Reinstating it as live text remains recommended hygiene.
* **R4 (scope).** The construction is for `d = 3` (`X_3` ledger, exterior Dirichlet recoupling on
  `R^3`). The conjecture is falsified at `nu = 3`; transport to other `d >= 2` requires re-running the
  angular layer and is outside this document.
* **R5 (conditionality).** The falsity statement is conditional on the correctness of the Note's proved
  layer as itemized in Section 5 — precisely the layer the audit examined and passed in items A–D, F, G
  (verdict table AR314–326). Within this program, no open problem is consumed by the synthesis chain.
