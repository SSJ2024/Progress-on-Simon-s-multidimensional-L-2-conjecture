# SCALING_NOTES — exact conventions extracted from the source note

All references are to `output/latex/operator_valued_riesz_singularity_note.tex` (the
canonical ~8000-line note; `siam-siraji-simon-l2-research/papers/paper-2-operator-valued-riesz/main.tex`
contains the same statements at offset −1153 lines). Line numbers below refer to the canonical file.

## 1. The dynamical system and the common-dilation parameter

The physical angular model is, everywhere,

$$i\,\partial_t U_s(t)=s\,(A_3+M_{V(t)})\,U_s(t),\qquad U_s(0)=\mathrm{Id},$$
with $A_3=-\Delta_{\mathbb S^2}$ (line 5917, 6182–6186), $V$ a smooth real scalar potential
(mask) on the sphere, and $M_V$ multiplication by $V$. The **common-dilation parameter** $s$
is *not time*: it multiplies the whole Hamiltonian. Equivalently, if $\tilde t=st$ is real
time, then $U_s(t)=\widetilde U(\tilde t)$ where $\widetilde U$ solves the unscaled equation
$i\partial_{\tilde t}\widetilde U=(A_3+M_{V(\tilde t/s)})\widetilde U$. So:

- **"Angular kinetic time" of a flight segment = its coefficient** $t_j$: the segment is the
  operator $e^{-is t_j A_3}$ (lines 5501–5504). The *physical* duration is $s\,t_j$, but all
  ledgers are stated in unscaled units.
- **Angular time is additive across concatenated segments**: the total flight time of the word
  $\mathcal W_s=\overleftarrow{\prod}_j e^{-is t_jA_3}e^{-isM_{q_j}}$ is $\sum_j t_j$
  (`eq:short-angular-time-target`, line 7041).
- **CORRECTION (second pass; supersedes §2 below).** The mask factors $e^{-isM_{q_j}}$ carry
  **no time parameter**: a mask is charged through its amplitude / integrated profile and
  through the quadratic $X_3$ cost, *never* through the flight ledger. "Angular kinetic
  time" means exactly the sum of positive-flight coefficients. Hence spatially disjoint or
  simultaneous mask segments do not split any flight budget — there is nothing to halve.
  The eta-short demand constrains how much $A_3$-free evolution the word uses, while masks
  may act arbitrarily long at bounded height, subject only to the separate
  small-charged-cost requirement (summability of $\|w_j\|_2^2/T_j$).

## 2. What "sum t_j < η" means; concurrency

The word in `eq:lens-assisted-word` (lines 5500–5505) and in
Problem `prob:short-time-radial-compiler` (lines 7036–7046) is an **ordered product**:
segments act one after another. There is **no concurrency bookkeeping anywhere in the note**:
no statement counts simultaneous spatially-disjoint masks as consuming the ledger once.
The ledger is literally the sum of coefficients over segments. Two consequences:

- If one builds parallel channels (masks supported on disjoint caps acting simultaneously),
  the Trotter/Lie product formalism used throughout (`eq:adiabatic-lens-trotter`,
  lines 5752–5760) would still slice them into sequential factors, each contributing its own
  $t_j$ to $\sum_j t_j$. A cap-localized swap of duration $t$ costs $t$, not $t/(\#\text{caps})$,
  unless one re-proves the whole compiler with a different accounting.
- Therefore the only way concurrency could help is by reducing **depth**: e.g., $N$ swaps done
  in $N$ layers cost their sum regardless, but doing disjoint swaps in the same layer does not
  reduce that layer's contribution either (each factor's coefficient adds).
  **Conclusion: concurrency buys nothing under the present definition.**
  *(First-pass addendum, now superseded by the §1 correction: the deeper point is that mask
  segments never consumed flight time at all — the eta budget is a positive-flight budget,
  so "interaction time" was never part of $\sum t_j$.)*

## 3. The outward radial reduction and the $1/R$ budget

`prop:outward-angular-time-budget` (lines 6248–6260): in the outgoing radial reduction of the
3D problem, the angular generator appears as $A_3/r^2$ and the dilation parameter as the
common factor $(2k)^{-1}=s$. Positive-flight radial ordering means the angular kinetic
coefficients of successive collars/slabs add, so the total positive angular kinetic time
available beyond radius $R$ is

$$\int_R^\infty \frac{dr}{r^2}=\frac 1R .$$

This is why Problem prob:short-time-radial-compiler demands $\sum_jt_j<\eta$ for **arbitrary**
$\eta>0$: inserting one generation into shells near radius $R$ consumes angular-time budget
$\lesssim 1/R$, and $R$ grows with generation index, so the per-generation allowance tends to
zero along the induction. The compiler theorem as proved (`thm:sphere-finite-frame-compiler`,
lines 6189–6207) has **unbounded** total $A_3$-flight (adiabatic entrance/exit with
$T\gg (s_0g^2)^{-1}$, line 5993), which cannot be placed on high shells.

## 4. Cost ledgers

Three distinct cost notions appear; do not conflate them.

**(a) $X_3$ cost / quadratic "charged" cost.** For a weak slab of length $T_j$ carrying
integrated mask $w_j$, the cost is $T_j^{-1}\|w_j\|_2^2$ (proof of
`prop:gradient-flow-radial-cost-no-go`, lines 7285–7290); summed over slabs this is the
$\operatorname{Cost}_{X_3}$ of the note (e.g. lines 7260–7264, 7339–7343). In the resonant
carrier language it bounds quadratic control energy: the two-level Rabi envelope is a bounded
linear functional of the scalar profile, so its quadratic energy is bounded above by a
constant times the physical $X_3$ cost (`prop:zs-broadband-energy-floor` discussion, lines
5462–5468). The shrinking-window carrier lift `thm:shrinking-window-carrier-lift`
(lines 4169–4219) realizes gates with peak height $\le B$, quadratic cost $\le\zeta$
arbitrarily small, and finite $L^1$ budget — but only on a window $S_\lambda=[c-\lambda R/N,
\,c+\lambda R/N]$ **shrinking with $\lambda$**, not on a fixed compact interval $S$.

**(b) Pointwise height bound.** One bound $\sup_{t,\omega}|Q(t,\omega)|\le B$ valid for the
whole construction ("one pointwise height bound", lines 2006–2007, 7046). This is the
amplitude cap that enters any quantum-speed-limit style obstruction.

**(c) Finite mask ledger.** Finitely many smooth mask shapes per generation (a finite list of
$q_j$'s); no analyticity or uniform-shape constraint beyond smoothness.

## 5. What exactly must be approximated

Two equivalent target formulations appear.

**(i) Lens-assisted inverse** (`prob:lens-assisted-inverse`, lines 5492–5516): given
$\tau>0$, realize
$$\mathcal W_s=\overleftarrow{\prod}_{j=1}^N e^{-is t_jA_3}e^{-isM_{q_j}}
\;\approx\;\chi(s)\,e^{is\tau A_3}\quad\text{on }\mathcal E,\text{ uniformly } s\in S,$$
(`eq:lens-assisted-inverse-target`, lines 5507–5514), i.e. emulate **free evolution with the
wrong speed** $\tau$ up to a scalar phase, with $\sum_j t_j$ small. Note: the *target*
operator itself carries $A_3$-time $\tau$; only the word's own flight budget is constrained.
The target is fixed once $\mathcal E,\tau,S$ are fixed; the word may depend on all data and on
$\eta,\varepsilon$, but **not** on $s$ or on the input vector (one control for the whole frame;
this input-independence is precisely what `prop:small-time-literature-audit` says the
literature does not supply).

**(ii) Compiler form** (`prob:short-time-radial-compiler`, lines 7036–7046): strengthen
`thm:sphere-finite-frame-compiler` by adding $\sum_jt_j<\eta$ while retaining (uniform-in-$s$
accuracy incl. leakage into the full complement), finite mask ledger, arbitrarily small
charged cost, and one pointwise height bound.

The two are equivalent in difficulty: the compiler reduces to the lens inverse plus finite
phase calibration (Step 4 of `thm:sphere-multiwell-permutation`, lines 5999–6031).

## 6. Which $U$ / which gate the machinery needs

- `prop:broadband-transposition-criterion` (lines 2433 ff.): it suffices to realize
  **drift-decorated transpositions** $\mathcal S_{j,s}\simeq$ signed permutation matrix
  decorated by $e^{is(C+T\lambda_{\pi(j)})}$ phases on the eigenbasis (see
  `eq:uniform-signed-sphere-permutation`, lines 5920–5928). So the required unitary is a
  genuine non-diagonal permutation-type gate on finitely many harmonics — **not** a phase-only
  gate. This kills any hope that the short-time problem degenerates to pure phases.
- `prop:positive-flight-no-recurrence` (lines 2161 ff.): free flights alone can never do it;
  masks are essential.
- Known proved fast piece: `thm:shrinking-window-carrier-lift` — full SU block on two shells
  in short physical time via resonant carrier $2a\cos(cNt)$ with amplitude $\le B$, but only on
  a shrinking $s$-window of width $\lambda R/N$. On a **fixed** compact $S=[s_0,s_1]$ with
  $h=s_1-s_0>0$ fixed, isolation requires $h\le c/(2(N+1))$ (`eq:saturated-carrier-isolation-window`,
  line 4057), forcing $N\lesssim c/h$: **bounded gap ⇒ bounded Rabi rate ⇒ positive swap floor**.
  This is the quantitative heart of the obstruction analysis in MAIN_RESULT/MAGNUS files.

## 7. Scale windows actually available in the double-well module

`prop:double-well-broadband-su2` (lines 6102–6120): tunnel splitting $\gamma$ (rate of the X
generator), imbalance scale $\delta$, external gap $G_{\rm ext}$, with the compatible order
$\gamma\ll\delta\ll G_{\rm ext}$. Gate-core durations are $t/\gamma$ and $|u|/\delta$.
Shrinking wells raises both absolute $\gamma,G_{\rm ext}$ while keeping ratios — the note
explicitly says the core "can be accelerated by shrinking the wells" (lines 7048–7050).
What is **not** accelerated in any proved statement is entrance/exit between low harmonics and
localized wells (lines 7050–7056), because adiabatic transport needs $T\gg(s_0g^2)^{-1}$
(`eq:uniform-common-dilation-adiabatic`, lines 5743–5748).

## 8. No-go results already banked (do not re-litigate)

- `prop:gradient-flow-radial-cost-no-go` (7248–7283): $1/\tau$ phase kicks cost
  $\ge \|\varphi\|^2/(\varepsilon c^2)\cdot R$ → diverges.
- `prop:phase-wrapping-cost-no-go` (7303–7435): modulo-$2\pi$ representatives keep a positive
  cost floor $\ge a_\varphi b_\varphi/(4\pi\varepsilon c^2)$.
- `prop:direct-scaled-slab`, backscatter & density-freezing no-gos (6272 ff.): single-scale and
  bounded-depth multiscale slabs freeze densities.
- `prop:log-shell-microstructure/ballistic-degree/ballistic-born-cost` (6550–7034):
  logarithmic shells need degree $\asymp R$ gratings; perturbative carriers have a Plancherel
  cost floor.
- `prop:small-time-literature-audit` (7123–7168): Chambrion–Pozzoli and Beauchard–Pozzoli give
  state-dependent controls and/or phase multipliers only; neither gives one input-independent
  unitary approximation on a full finite frame uniform in $s\in S$.

## 9. Summary table of conventions

| Object | Meaning | Ledger |
|---|---|---|
| $t_j$ | coefficient of $e^{-is t_jA_3}$ ("angular kinetic time") | sums: $\sum t_j<\eta$ |
| $q_j$ | smooth real mask shape | finite list |
| charged cost | $\sum_j T_j^{-1}\|w_j\|_2^2$ (weak-slab quadratic) | must be arbitrarily small |
| height | $\sup|Q|$ pointwise amplitude | one bound $B$ |
| $s$ | common dilation, multiplies Hamiltonian | sup over $s\in S$, $S$ compact nondegenerate |
| leakage | error measured $\mathcal E\to L^2(\mathbb S^2)$ full space | $<\varepsilon$ incl. complement |
| target | $\chi(s)e^{is\tau A_3}$ resp. signed permutation $G(s)$ | uniform in $s$ |
