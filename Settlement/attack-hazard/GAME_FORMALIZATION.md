# GAME FORMALIZATION — Global chromatic coverage vs. the hazard route

Source: `output/latex/operator_valued_riesz_singularity_note.tex` (all line refs below refer to it).
Target problem: `prob:physical-grouped-global` (lines 2067–2083).

---

## 1. Players

**Contractor (the program).** Must produce, at each stage `j = 1,2,…`, a finite
group assembly (a "generation") acting on the current smooth real finite
partial potential `W_{j-1}`, such that the dovetail requirements of
`thm:scalar-dovetail` (lines 771–802) stay satisfiable:
nonexpansion of protected moments (eq. line 781), contraction of the targeted
moment by `1/2` per visit (eq. line 783), preservation of `C(K)`-moments of the
first `j` densities (eq. line 789), and permanent lockability of declared
witnesses (lines 794–796). The end goal is `prop:conditional-counterexample-final`
(lines 7712–7748): all cells on successive disjoint shells (line 7734), one
uniform amplitude bound, `X_3` cost `sum_j 2^{-2j}` (eq. line 7737),
`(3/4)^3 < 1/2` per stage triple (lines 7731–7733).

**Adversary (Nature / the certificate chain).** Controls nothing explicitly,
but the Contractor's *certificates* are only as good as the oracles below; any
quantity the oracles leave unbounded (window widths, continuity moduli,
frequencies) is adversary territory. Two explicit adversary blueprints are
proved in the source: `prop:grouped-root-zeno` (lines 1741–1817) and
`prop:mobius-orbit-haar-obstruction` (lines 1819–1951); a third,
`prop:coverage-obstruction` (lines 1391–1418), is a pure measure-theoretic
stall.

---

## 2. State space (what generation `j` leaves to generation `j+1`)

| Object | Symbol | Source anchor |
|---|---|---|
| Partial potential | `W_j` smooth, real, finite | hyp. of prop line 1995 |
| Active block dimension | `n_j` (probes + channels + angular cutoff) | FSM lemma line 1953 |
| Reciprocal-phase fiber | `H_j(k) in U(n_j)`, `k in K` | one-window proof line 2014 ff. |
| Radiation vectors | `x_{p,j}(k)`, `p <= j` | line 2014 |
| beta-densities | `w_{p,j}(k)`, `I_{p,j} = int w^beta` | thm line 773–777 |
| Frequency content | `Lambda_j` = supremum of modulation frequencies of `k -> (H_j(k), x_{p,j}(k))` | **not in source; introduced here** |
| Certified window | `I = K cap (k*-h, k*+h)`, `h > 0` | prop line 2000 |
| Placement frequency | `nu` (collar phase `z(k) = e^{i nu k}`) | lem line 651 |
| Group length / depth | `M_j`, `m_j`; cost `M_j C_rho e^{-c m_j}` | lines 2056–2058 |

**Crucial rule asymmetry.** The one-window proposition asserts only
"`h > 0` … no uniform lower bound for `h` is asserted" (line 2010). The FSM
lemma grants a neighbourhood "if `H(k)` and `x_p(k)` are norm-continuous"
(line 1961–1963) — *norm continuity, no modulus*. So the rules pin the weak
moments of `w_{p,j}` but leave the `k`-modulus of `(H_j, x_{p,j})` completely
unregulated. That unregulated quantity is where every adversary and every
repair lives.

---

## 3. Oracle rules (what certificates the Contractor may invoke)

1. **One-window contraction**, `prop:physical-grouped-one-window`
   (1993–2065): factor `<= 1/2` up to `zeta` on `I`; protected moments
   nonexpansive up to `zeta` on all of `K`; `X_3 <= zeta`; amplitude bounded
   by `rho` alone (line 2006–2007). Internally: group length `M` fixed from
   the *infinite-dimensional* singular bundle **before** the finite model
   (lines 2031–2044); placement afterwards (lines 2046–2054).
2. **Finite spectral model**, `lem:finite-spectral-model` (1953–1991):
   recursions of length `<= T` differ by `C_{rho,T} delta` (1983–1985); valid
   on a neighbourhood whose size is *whatever norm continuity yields*
   (1961–1963).
3. **Deterministic placement**, `lem:one-step-placement` (640–674):
   arbitrarily large `nu` realize torus means + test preservation to
   `epsilon`. Proof = Fourier-in-`z` + Riemann–Lebesgue (664–673).
   Section preamble warns of the **moving-spike defect** if concentration
   witnesses are not carried along (632–638).
4. **Physical Hardy identity**, `lem:physical-hardy` (1058–1118): exact
   phase-mean isometry ⇒ nonexpansion of fractional moments. Explicitly
   "does not supply a strict contraction away from the cell's tuning window"
   (remark 1120–1134, esp. 1132–1133).
5. **Compact output stability / reflection gap / scales / window cost**
   (866 ff., 920 ff., 1311–1354, 1356–1389). Window cost: chromatic error
   `C m |k/k* - 1| + eps`, windows `h_m = (CA_rho m)^{-1} (zeta/4|K|)^{1/beta}`,
   count `N_m <= C_K A_rho m zeta^{-1/beta}` (1369–1375); "carrier, radii and
   cutoffs do not enter the charged cost" (1351–1353).
6. **Group contraction engines**:
   `thm:grouped-ideal-contraction` (1531–1630) — **uniform over all
   `H_0 in U(n)`**, burn-in `M(n) <= C_rho log(n+1) + C_rho`
   (eq. 1536–1539), `q* = 1/2` (line 1625);
   `thm:singular-bundle-grouped-contraction` (1632–1739) — uniform over a
   weakly compact family `frak M` of singular measures;
   `lem:uniform-reciprocal-synchronization` (1479–1529) with chord identity
   (eq. 1500–1504).
7. **Adaptive averaging + hazard**, `prop:adaptive-centre-averaging`
   (2085–2137): per-step gain `(1 - gamma h/|K|)` (eq. 2104), product bound
   (eq. 2110–2117), divergence criterion `sum gamma_j h_j = infinity`
   (eq. 2120). Reduction recorded at `cor:exact-hazard-bottleneck`
   (2139–2159): `gamma_0 = 1/2 - o(1)` (2144–2147).

## 4. Adversary blueprints shipped with the source

- **Root-Zeno**, `prop:grouped-root-zeno` (1741–1817): certified widths
  `h_j = eta/(C M_j m_j)` with `M_j >= log N_j / (2 rho)` (1765–1771);
  `N_j = ceil e^{j^2}` makes `sum h_j < infinity` (1772–1778). Moral
  (1779–1784): "must use additional structure of the actually generated phase
  bundles".
- **Möbius orbit to Haar**, `prop:mobius-orbit-haar-obstruction`
  (1819–1951): a *pure-point* `nu` with **infinitely many atoms**
  (atomic-zoom mixture, eq. 1898–1903) follows boosts so that
  `T_{g_n} nu -> m`; hence for fixed `M` the grouped moment is `1` for some
  history (eq. 1850–1858); "cannot be made uniform over all prior ideal scalar
  histories without an additional restriction" (1861–1864).
- **No uniform chromatic modulus**, `prop:no-uniform-chromatic-modulus`
  (1420–1460): `Q_{beta,N}(t) <= q` forces `rho >= (1/2) log N - c`
  (eq. 1429–1436).
- **Coverage stall**, `prop:coverage-obstruction` (1391–1418): if
  `sum h_j < |K|`, legal densities exist with
  `inf_j int w_j^beta > 0`.

## 5. Scoreboard

- **Contractor wins** the stage game iff every generation is certifiable by
  rules 1–7 with the prescribed error schedule `eps_j` (assembly uses
  `2^{-2j}`, line 7729) and the dovetail hypotheses (781)–(789) hold with
  summable errors.
- **Adversary wins** iff it exhibits a legal play with
  `inf_j I_{p,j} > 0` for some targeted `p`, or blocks certification
  outright.
- **The hazard functional** `H_N = sum_{j<=N} gamma_j h_j` (rule 7) is *not*
  itself the score — it is the Contractor's preferred driving mechanism
  (`cor:exact-hazard-bottleneck`). Whether it must diverge along generated
  trajectories is exactly the question under attack.

## 6. Ledger feedback laws (derived in MAIN_ATTEMPT.md; preview)

```
Lambda_{j+1} >= max(Lambda_j, all frequencies used at stage j)     (monotonicity)
nu_used >= c * Lambda_j / eps * (Diophantine penalty)              (certification threshold)
h_{j+1} <= pi / nu_top                                             (FSM width ceiling)
L_j ~ |K| Lambda_{j-1},   m_j ~ log L_j,   cost_j <= 2^{-2j}       (cover ledger, absorbed)
M_j <= C_rho log n_j + C_rho                                       (dimension-uniform length)
```

The tension: laws 2–3 (ratchet) vs. law 5 (dimension-uniform length) vs.
law 4 (direct cover). Resolution in MAIN_ATTEMPT.md / COUNTEREXAMPLE_SEARCH.md.
