# G1_FREEZE_CHECK.md — does the temporal-carrier compiler survive the density-freezing no-gos?

Scope: settle honest gap **G1** of MAIN_RESULT.md — whether the temporal-carrier
short-time compiler (MAIN_RESULT.md + MAGNUS_FEASIBILITY.md +
ADDENDUM_QSL_AND_LEDGER.md) survives the slab/log-shell density-freezing no-gos of
`output/latex/operator_valued_riesz_singularity_note.tex`
(props `prop:direct-scaled-slab-density-no-go`, `prop:bounded-depth-density-no-go`,
`prop:log-shell-ballistic-degree`, and the reciprocal-radius product criterion
`eq:multiscale-density-no-go-condition`).

Method: each criterion is stated as a precise inequality with its exact hypotheses,
then checked against the carrier construction, with a verdict
APPLIES-AND-VIOLATED / APPLIES-AND-SATISFIED / DOES-NOT-APPLY.

---

## 1. The criteria as stated in the source

### 1.1 prop:direct-scaled-slab-density-no-go ("every cost-compatible direct slab freezes spatial densities", l. 6499–6597)

Setting: the *semiclassical angular gate* on the scaled interval $0\le x\le T$,

$$i\partial_x \mathcal U_{s,N}(x) = s\Big(\frac{A_3}{N}+M_{Q_N(x)}\Big)\mathcal U_{s,N}(x),$$

which is the exact forward model of one **single-scale direct scaled slab** at radius
$r=R_N+L_Nx$, $L_N=R_N^2/N$, physical control $V_N=L_N^{-1}Q_N$
(prop:direct-scaled-slab, l. 6272–6374). Hypotheses:

- $\mathfrak C$ = normalized trajectories from one fixed finite smooth input frame;
  $E_N=\sup_{s,x,f}\|A_3\mathcal U_{s,N}f\|_2$ finite.
- **Compatibility (vanishing cost + vanishing frozen-radius error):**
  $$\frac{N}{R_N^2}\to 0,\qquad \frac{R_NE_N}{N^2}\to 0.$$

Conclusion: for every real smooth multiplication observable $X$,

$$\sup_{s,x,f}\big|\langle\psi,M_X\psi\rangle-\langle f,M_Xf\rangle\big|
 \le \frac{C(1+\sqrt{E_N})}{N}\to 0 .$$

All position densities freeze. Corollary drawn in the proposition itself: such a
family cannot converge, up to scalar phase, to $e^{is\tau A_3}$ on
$\mathrm{span}\{e_0,e_\lambda\}$ for any nondegenerate $S$, because on
$f=(e_0+e_\lambda)/\sqrt2$ the target changes
$\langle M_{e_\lambda}\rangle$ by $(4\pi)^{-1/2}(\cos(s\tau\lambda)-1)\not\equiv 0$.

Key mechanism: $M_{Q_N(x)}$ commutes with $M_X$; only the kinetic term moves
densities, at rate $O(s/N)$. **The freezing bound is uniform in the temporal profile
of $Q_N(x)$** — fast oscillation in $x$ does not help, because the estimate is an
$x$-integrated first-order commutator bound (convexity/averaging in time is already
built into the Duhamel estimate).

Note what the proposition excludes: convergence to the lens *as $N\to\infty$ along
the direct single-scale window* $\sqrt N\ll R_N\ll N$. It is a statement about the
scaled family $(Q_N,R_N,N)$, i.e. about architectures that live at **one frozen
radius per slab with a single scale $N$**, with cost $O(N/R_N^2)\to0$.

### 1.2 prop:bounded-depth-density-no-go and eq:multiscale-density-no-go-condition ("bounded-depth multiscale slabs also freeze densities", l. 6599–6701)

Setting: concatenate $m_q$ scaled slabs; slab $j$ has scaled duration $T_{q,j}$,
parameters $N_{q,j},R_{q,j}$, trajectory energy $E_{q,j}$. Define

$$\alpha_q=\sum_j\frac{T_{q,j}}{N_{q,j}},\quad
  \beta_q=\sum_j\frac{T_{q,j}R_{q,j}E_{q,j}}{N_{q,j}^2},\quad
  \gamma_q=\sum_j\frac{T_{q,j}}{R_{q,j}} .$$

Conclusion (density freezing across the cascade):

$$\sup_{s,f}\big|\langle\psi_q,M_X\psi_q\rangle-\langle f,M_Xf\rangle\big|
 \le C_{S,X}\big(\alpha_q+\sqrt{\beta_q\gamma_q}\big).$$

Consequently, if $\mathfrak C$ contains $f=(e_0+e_\lambda)/\sqrt2$ and

$$\boxed{\ \alpha_q\to0\ \text{ and }\ \beta_q\gamma_q\to0\ }$$
(eq:multiscale-density-no-go-condition)

the cascade cannot produce the lens inverse on $\mathrm{span}\{e_0,e_\lambda\}$.

**The "reciprocal-radius product criterion"** (l. 6665–6670): any surviving
multiscale compiler must *violate*

$$\Big(\sum_j\frac{T_{q,j}R_{q,j}E_{q,j}}{N_{q,j}^2}\Big)
 \Big(\sum_j\frac{T_{q,j}}{R_{q,j}}\Big)\longrightarrow 0,$$

i.e. must keep the product (total frozen-radius error × total reciprocal-radius
budget) **away from zero**. Special case killed outright: bounded depth
($m_q$ bounded), bounded slab durations, $\min N_{q,j}\to\infty$,
$\min R_{q,j}\to\infty$, $\beta_q\to0$.

The source's own summary (l. 7093–7097): a positive result inside this model "must
use an unbounded number of genuinely interacting scales and must violate the
reciprocal-radius product criterion".

### 1.3 prop:log-shell-ballistic-degree ("bounded-action logarithmic shells require ballistic angular degree", l. 6829–6948)

Setting: logarithmic shell $r=Re^t$, $V_R(r)=r^{-1}W_R(t,\omega)$, rescaled model
$i\partial_tU=s\big(e^{-t}A_3/R+M_{W_R(t)}\big)U$ on $0\le t\le T$. Hypotheses:

- **Band-limited controls:** $W_R(t)\in\bigoplus_{j\le D_R}\mathcal H_j$
  (harmonic degree at most $D_R$);
- **Bounded rescaled action:** $\int_0^T\|W_R(t)\|_\infty\,dt\le M$ uniformly in $R$;
- fixed low-degree input frame $P_{\le L_0}L^2$, fixed nondegenerate $S$.

Conclusion: gradient bound $\|\nabla_\omega U f\|\le C(1+D_R)$, hence density
freezing

$$\big|\langle\psi,M_X\psi\rangle-\langle f,M_Xf\rangle\big|
 \le C\frac{1+D_R}{R}.$$

If $D_R=o(R)$, the log shell cannot produce the lens inverse. Equivalently
(eq:log-shell-ballistic-degree-necessity): any successful bounded-action
logarithmic-shell lens needs $\liminf D_R/R>0$ — angular wavelength $O(R^{-1})$,
physical tangential wavelength $O(1)$, the **non-paraxial regime**.

Companion results bounding the same escape:
- prop:log-shell-microstructure (l. 6703–6827): under the *uniform smoothness*
  class $\sup_R\{\int\|W_R\|_2^2+\int\|W_R\|_{W^{2,\infty}}\}<\infty$ the shell
  converges to a mere phase multiplier $Z=e^{-isM_{\Phi_R}}$ within $C/R$ — which
  preserves $|f|$ pointwise and so cannot give $e^{is\tau A_3}$ on the two-harmonic
  frame; quantitatively, success forces
  $\|\Delta\Phi_R\|_\infty+\|\nabla\Phi_R\|_\infty^2\ge cR$ ($\sqrt R$ microstructure).
- prop:log-shell-ballistic-born-cost (l. 6950–7034): an isolated Born-level
  ballistic carrier of degree $D_R$ with $\liminf D_R/R>0$ that transfers uniformly
  on $S$ pays physical cost $\ge c\,\Lambda_R/R^2>0$ ($\Lambda_R=D_R(D_R+1)$).

### 1.4 What the radialization problem actually needs the word to do

prop:outward-angular-time-budget (l. 6248–6270): a controller supported beyond
radius $R$ has total positive angular kinetic time at most
$\int_R^\infty dr/r^2=1/R$ (slabs consume their share; subdivision does not evade
it). And the closing discussion (l. 7878–7932): the compiled word must be
compressed to total positive $A_3$-time $o(R^{-1})$ **before insertion** into the
remote-shell ledger; then it must be radially realized with small charged cost,
one pointwise height bound, full-sphere leakage control, uniform accuracy on
$S=[s_0,s_1]$.

Crucially, the *target* of prob:short-time-radial-compiler is the lens gate
$\chi(s)e^{is\tau A_3}|_\mathcal E$ — a relative-**phase** (spectral-function)
operation on a fixed finite conjugation-invariant space $\mathcal E$ — not a
spatial density displacement per se. But note the two-harmonic fact used by all
three freezing propositions: on $f=(e_0+e_\lambda)/\sqrt2$, changing the relative
phase between $e_0$ and $e_\lambda$ **does** change the position density
($\langle M_{e_\lambda}\rangle$ moves by $(4\pi)^{-1/2}(\cos(s\tau\lambda)-1)$).
So "angular phase gate" and "density motion" are not separable on superpositions:
a correct phase gate necessarily moves some densities, and density-freezing bounds
therefore do constrain the phase gate. This is the audit's central point, developed
in §3.0 below.

---

## 2. The construction as a radial object, and the numbers check

### 2.1 Inventory of the construction (MAIN_RESULT §2–3, MAGNUS_FEASIBILITY §§0–6, ADDENDUM §§2–3)

- Word: $W_s=\overleftarrow{\prod}_j e^{-ist_jA_3}e^{-isM_{q_j}}$, flight sum
  $\sum_jt_j=T<\eta$ with $\eta$ arbitrary; masks enter as instantaneous kicks with
  integrated profiles $w_j$; only flight coefficients consume the $\eta$ budget.
- Mask class: real smooth, ONE uniform pointwise height
  $h\ge\frac{|\tau-1|}{2}\max|\mathrm{spec}(A_3)|_\mathcal E|+\text{margin}$;
  FIXED harmonic degree (the finitely many harmonics tying $\mathrm{spec}(\mathcal E)$
  to its immediate complement, e.g. $z=\cos\theta$ for $\mathcal E=\mathrm{span}\{Y^0_0,Y^1_m\}$).
- Temporal carrier: $u(t,x)=\sum_ka_k\cos(\omega_kt)\phi_k(x)$,
  $\omega_k\to\infty$ as $\eta\to0$, detuned $O(1)$ from active gaps; realized as
  alternating-sign sub-slab profiles $w_{j,k}$; amplitudes $a_k\sim\sqrt{|\tau-1|}$ bounded.
- Charged cost: $\sum_jT_j^{-1}\|w_j\|^2$ with $\|w_j\|=O(hT_j)$, total $O(h^2\eta)\to0$.
- Claimed accuracy: $\Omega=-iT(A_3+\bar Q)+O(T^2\|\bar Q\|^2)+O(T^3)$ on the
  $\mathcal E$-compression; leakage mass $\sim\kappa^2T^2\to0$; uniform in
  $s\in S=[s_0,s_1]$ (fixed nondegenerate compact interval).
- Radial insertion: weak slabs on exterior shells beyond $R$; a slab of frozen-radius
  length $T_{\rm slab}$ at radius $R$ consumes angular kinetic time $T_{\rm slab}/R^2$
  and costs $\|w\|^2/T_{\rm slab}$; ADDENDUM §3 resolves the cost/time conflict
  "by going farther out": $T_{\rm slab}\le\varepsilon R$ gives both $\to0$.

Resource inventory — what grows, what stays bounded:

| quantity | behavior in the family |
|---|---|
| flight sum $\sum t_j$ | $\to0$ ($\eta$ arbitrary) |
| mask height $h$ | $O(1)$ |
| mask harmonic degree $D$ | FIXED (hence $o(R)$ at every radius) |
| number of carriers | $\le\dim\mathcal E$, fixed |
| carrier frequency $\omega$ | $\to\infty$ — a TEMPORAL scale |
| trajectory energy $\sup\langle A_3\rangle$ along the family | $O(1)$: total mask $L^\infty$ action is $a=s_1\!\int\!\|u\|_\infty=O(s_1hT)\to0$, and the Clebsch–Gordan/Dyson bound of the proof of prop:log-shell-ballistic-degree (l. 6881–6920) gives $\|A_3^{1/2}\psi\|\le e^a(L_0+1+aD)=O(1)$ — **independent of the letter count and of $\omega$** |
| radial scales ($N_j$, $R_j$) | whatever the insertion chooses; the family itself contributes no diversity |

The decisive structural fact: **every resource that enters any freezing estimate is
spatial/spectral** — kinetic time, harmonic degree, trajectory energy, radial/semiclassical
scales $(N_j,R_j,E_j)$. The carrier's new scale $\omega$ is temporal. Multiplication
operators commute with every $M_X$ at every instant, so temporal oscillation contributes
exactly nothing to density motion, and the freezing proofs nowhere assume slow temporal
profiles: they integrate the exact commutator identity
$\frac{d}{dx}\langle\psi,M_X\psi\rangle=\frac{is}{N}\langle\psi,[A_3,M_X]\psi\rangle$
(l. 6544–6567) resp. its log-shell cousin (l. 6922–6936), which hold for arbitrary
(measurable-in-time) controls. $\omega\to\infty$ is invisible to
$\alpha_q,\beta_q,\gamma_q$, to $E_N$, and to $D_R$. MAIN_RESULT's hope that
"convexity/averaging makes the freezing estimates insensitive to fast alternation"
(l. 121–125) is correct — and it cuts against the construction: insensitivity means
alternation purchases nothing.

### 2.2 Numbers check (task item 3)

- Outward budget: $\int_R^\infty dr/r^2=1/R$ (prop:outward-angular-time-budget);
  slabs consume their share; subdivision does not evade it. ✓ as stated.
- Insertion needs $\sum t_j=o(R^{-1})$ (l. 7878–79); any fixed $\eta$ fits by taking
  $R$ large. No tension here. ✓
- Cost-vs-angular-time tension at large R — **VERIFIED**: direct-slab ledger
  (eq:direct-slab-cost/height/angular-time): physical cost
  $\frac{N}{R^2}\int_0^T\|Q_N\|_2^2dx\to0$, height $\frac{N}{R^2}\|Q_N\|_\infty\to0$,
  angular time $\frac TN+O_T(\frac RN)=o(R^{-1})$ in the window $\sqrt N\ll R\ll N$;
  weak-slab ledger (ADDENDUM §3): cost $\ge\|w\|^2/(\varepsilon R)\to0$ while
  consumption $\le\varepsilon/R\to0$; construction's own quadratic cost
  $O(T\|\bar q\|_\infty^2)=O(h^2\eta)\to0$. All mutually consistent. ✓
- **But the third ledger does not relax with $R$.** The freezing errors are
  $\frac{(1+\sqrt{E_N})}N$ (direct), $\alpha_q+\sqrt{\beta_q\gamma_q}$ (cascade),
  $\frac{1+D_R}R$ (log shell). Each tends to 0 precisely when the architecture becomes
  INCAPABLE of density motion. Large $R$ buys cheapness and angular room and
  simultaneously tightens freezing. "Both ledgers close at large radius" (ADDENDUM §3)
  is true and incomplete: closing the cost and time ledgers is exactly what trips the
  freezing ledger. The claim under verification — that the tension resolves at large $R$ —
  is correct for the two ledgers checked and **false as a resolution of G1**.

---

## 3. Verdict per criterion

Notation for verdicts: **APPLIES-AND-VIOLATED** = the construction falls under the
proposition's hypotheses and the proposition's conclusion excludes the intended
conclusion (lens production); **APPLIES-AND-SATISFIED** = the criterion constrains the
construction and the construction meets it; **DOES-NOT-APPLY** = hypotheses fail
identifiably.

### 3.0 Preliminary: do the no-gos apply to angular gates at all? (task item 3, second question)

**They do.** The dichotomy "phase gate vs. density motion" is false on multi-harmonic
frames: for $f=(e_0+e_\lambda)/\sqrt2$ (l. 6578–6596, recomputed independently),

$$\big\langle e^{is\tau A_3}f,\,M_{e_\lambda}\,e^{is\tau A_3}f\big\rangle-\langle f,M_{e_\lambda}f\rangle
=\tfrac{1}{\sqrt{4\pi}}\{\cos(s\tau\lambda)-1\},$$

which is $\ge c(S,\tau,\lambda)>0$ at some $s\in S$. Every freezing proposition
converts this display into its lens corollary. The only angular operations exempt from
the density test are scalar phases (single shell — where $A_3$ is scalar and the lens
is trivial — or the global $\chi(s)$). The lens on any conjugation-invariant
$\mathcal E$ containing $\ge2$ shells is NOT of this type. Hence: architecture-level
statements that freeze $\langle M_X\rangle$ for all smooth $X$ exclude the phase gate;
the inverse drift and the angular phase gate are the same obstruction in different
observables.

Underlying mechanism (used repeatedly below): **mask flows preserve $|\psi|$
pointwise** ($M_q$ is a phase multiplier), so *all* density motion is charged to the
kinetic term; a family with total kinetic resource $\Theta$ and trajectory gradients
$\le G$ moves every $\langle M_X\rangle$ by at most $C_{S,X}\,\Theta\,(1+G^2)$.

### 3.1 Criterion prop:direct-scaled-slab-density-no-go — **APPLIES-AND-VIOLATED**

Applicability. This proposition governs the semiclassical single-scale insertion —
the only insertion route for which the source proves a complete forward reduction
including backscatter control (props:direct-scaled-slab, direct-scaled-slab-backscatter).
Placing the carrier program in $Q_N(x,\omega)$ (fast $x$-oscillation permitted):
$\sup_N\int\|Q_N\|_2^2<\infty$ ✓ (heights $O(1)$, degrees fixed),
$\sup\|Q_N\|_\infty<\infty$ ✓, trajectory bound $\|A_3\mathcal U f\|=O(1)\le C_{\mathfrak C}N$ ✓
(bounded-degree trajectories), compatibility $\frac NR_N^2\to0$,
$\frac{R_NE_N}{N^2}=\frac{O(R_N)}{N^2}\to0$ ✓ in $\sqrt N\ll R\ll N$. All hypotheses hold.

Conclusion. Freezing $\frac{C(1+\sqrt{E_N})}N\to0$ contradicts the $O(1)$ two-harmonic
density motion of the lens. The carrier's temporal profile is subsumed: the proof
never constrains the $x$-dependence of $Q_N$ beyond the trajectory bound. The
attempted escape "the construction introduces an unbounded sequence of scales through
$\omega\to\infty$" (MAIN_RESULT l. 89–95) fails: $\omega$ is not among the
proposition's resources, and the conceded escape at l. 7093–7097 refers to the
radial/scaling parameters $(m_q,N_{q,j},R_{q,j},E_{q,j})$, none of which the carrier
diversifies.

### 3.2 Criterion prop:bounded-depth-density-no-go and eq:multiscale-density-no-go-condition (reciprocal-radius product criterion) — **APPLIES-AND-VIOLATED**

Applicability. Any concatenation of the carrier program into scaled slabs lies in this
model. Compute the resource sums for a carrier cascade with sub-slab durations
$T_{q,j}=T/m_q$ (one per carrier half-period, so $m_q\sim\omega T\to\infty$: depth IS
unbounded), shared scale $N_{q,j}=N$, radii $R_{q,j}\approx R$, energies
$E_{q,j}=O(1)$:

$$\alpha_q=\frac TN\to0,\qquad
  \beta_q\gamma_q=\Big(\frac{TRE}{N^2}\Big)\Big(\frac TR\Big)\longrightarrow0 .$$

Depth alone is not a scale: with all cells at the same $(N,R)$, the product collapses
regardless of $m_q$. The condition $\alpha_q\to0$ AND $\beta_q\gamma_q\to0$ therefore
HOLDS for every bounded-resource insertion of the family, and the proposition forbids
lens convergence.

The sanctioned escape — *violating* the product criterion — is quantitatively out of
reach for the carrier: violating it requires
$\beta_q=\sum_j\frac{T_{q,j}R_{q,j}E_{q,j}}{N_{q,j}^2}\not\to0$, i.e. trajectory
energies $E_j\sim N_j^2/R_j$-scale — ballistic spectral content. Note also that
$\gamma_q=\sum_jT_{q,j}/R_{q,j}$ is (up to constants) the outward angular-time budget:
a violator compatible with the outward budget ($\gamma_q\lesssim1/R$) needs
$\beta_q\gtrsim cR$ — enormous trajectory energies again. These are spectral/radial
scales; the temporal carrier supplies none. Verdict: the criterion applies and the
construction, as specified, sits on the wrong side of it (it satisfies the freezing
hypothesis rather than violating the criterion).

### 3.3 Criterion prop:log-shell-ballistic-degree (with prop:log-shell-microstructure and prop:log-shell-ballistic-born-cost) — **APPLIES-AND-VIOLATED**

Applicability. On a logarithmic shell $V_R=r^{-1}W_R$, the construction's physical
height $h$ relates to the rescaled control by $W_R=rV_R\approx hRe^t$: either
$W_R=O(1)$ (then physical height $\to0$: trivial control) or the bounded-action
hypothesis $\int_0^T\|W_R\|_\infty dt\le M$ fails. In the bounded-action class — the
only one where the shell is a cheap $O(R^{-1})$ cell — the construction's FIXED
degree gives $D_R=O(1)=o(R)$, and the freezing bound
$C\frac{1+D_R}{R}\to0$ excludes the lens. The proposition's own converse
(eq:log-shell-ballistic-degree-necessity, $D_R\asymp R$, tangential wavelength $O(1)$,
non-paraxial) directly contradicts the construction's fixed-degree principle.
Moreover, upgrading to $D_R\asymp R$ to satisfy the necessity does not rescue the
carrier: prop:log-shell-ballistic-born-cost then charges every isolated Born-level
uniform-transfer carrier a physical cost $\ge c_{S,T}\eta^2\Lambda_R/R^2>0$ — it can no
longer be a vanishing-cost cell; and prop:log-shell-microstructure separately excludes
any uniformly smooth $W_R$ (phase multipliers preserve $|f|$ pointwise). What remains
on the log-shell route is a nonperturbative collective gate controlling the entire
growing resonant cluster (l. 7929–7932) — not the temporal-carrier construction.

### 3.4 Criterion prop:outward-angular-time-budget — **APPLIES-AND-SATISFIED**

This is a budget, not a no-go: $\sum t_j=\eta$ fixed, insert beyond
$R\gg1/\eta$: respected; slab shares accounted (ADDENDUM §3 arithmetic verified in
§2.2). No violation — but it is the channel through which the freezing mechanism
enters the weak-slab insertion: beyond $R$ the total density-moving resource is
$s/R\to0$, so a fixed-degree controller freezes all multiplication observables at
rate $C(1+D^2)/R$ no matter how the cost ledger is booked.

### 3.5 Derived criterion (word-level freezing corollary — this document's addition; same commutator engine one layer deeper) — **APPLIES-AND-VIOLATED**

Statement. Let $W_s=\overleftarrow{\prod}_{j\le m}e^{-ist_jA_3}e^{-isM_{q_j}}$ with
$q_j\in\bigoplus_{k\le D}\mathcal H_k$, $\|q_j\|_\infty\le h$, fixed $m$ (or a Trotter
limit of a bounded-action continuous program). Then uniformly for $s\in S$ and $f$ in
a fixed smooth frame,

$$\big|\langle W_sf,M_XW_sf\rangle-\langle f,M_Xf\rangle\big|
\le C_{S,X}\,s\,\Big(\sum_jt_j\Big)\big(1+G^2\big),
\qquad G\le e^{s_1mh}(L_0+1+s_1mhD),$$

using: mask kicks preserve $|\psi|$ pointwise; flights move $\langle M_X\rangle$ at
rate $\le C(1+\|A_3^{1/2}\psi\|^2)$; and the Clebsch–Gordan/Dyson gradient bound of
the proof of prop:log-shell-ballistic-degree (l. 6881–6920), which depends only on
total mask action and degree — not on letter count or modulation frequency.

Consequence. Matching the lens on $\mathrm{span}\{e_0,e_\lambda\}$ requires
$\sup_S|\cos(s\tau\lambda)-1|/\sqrt{4\pi}\le C_{S,X}s_1\Sigma t_j(1+G^2)$, hence the
**necessary tradeoff**
$$\Sigma t_j\ \ge\ \frac{c(S,\tau,\lambda)}{s_1(1+G^2)} .$$
For the carrier family $G=O(1)$ (fixed degree, bounded height, total action
$O(s_1hT)\to0$), so $\Sigma t_j\ge c'>0$: the headline claim "$T=\sum t_j\to0$ with no
amplitude growth and fixed degree" is internally inconsistent with the target it is
supposed to approximate. The Magnus verification does not see this because it tests
only the $P_\mathcal E(\cdot)P_\mathcal E$ block and books leakage as
$O(\kappa^2T^2)$; but vector-norm accuracy on the frame *with full-sphere leakage
control* (eq:finite-frame-ensemble-compiler, l. 6200–6206 — the very theorem
prob:short-time-radial-compiler strengthens) forces $\|W_sf-\chi e^{-is\tau A_3}f\|\to0$,
hence the density motion, hence $G\to\infty$. Consistency checks: the source's own
working positive machines — adiabatic well permutations, shrinking-window ballistic
carriers (l. 7792–7815) — all spend either $O(1)$ angular kinetic time or degree
$\asymp R$, exactly as the corollary demands; and the large-flight finite-frame
compiler is unaffected ($\Sigma t_j=O(\tau)$).

Consequence for the "unbounded scales" concession: l. 7093–7097 locates the required
scale diversity in the radial model; the corollary shows it is already required at the
ABSTRACT word level. A short-time compiler, if it exists, must drive trajectory
gradients $G\to\infty$ (unbounded harmonic-degree excursions created and refocused by
the masks) — precisely the ballistic content that the radial criteria 3.2–3.3 then
price. The temporal carrier, which keeps $G=O(1)$ by design, cannot be the mechanism.

---

## 4. Scorecard and final assessment

| # | criterion | verdict |
|---|---|---|
| 1 | prop:direct-scaled-slab-density-no-go (compatibility $\frac NR_N^2\to0$, $\frac{R_NE_N}{N^2}\to0$; freezes $\langle M_X\rangle$ to $O(1/N)$) | **APPLIES-AND-VIOLATED** — all hypotheses hold for the carrier program placed in $Q_N(x)$; temporal profile unconstrained by the proof; lens excluded |
| 2 | prop:bounded-depth-density-no-go / eq:multiscale-density-no-go-condition (reciprocal-radius product criterion: survivor must keep $\beta_q\gamma_q\not\to0$) | **APPLIES-AND-VIOLATED** — carrier cascade has unbounded depth but shared $(N,R,E)$: $\alpha\to0$, $\beta\gamma\to0$ regardless of depth; the required violation needs ballistic $E_j\sim N_j^2/R_j$, a spectral scale the temporal carrier does not supply |
| 3 | prop:log-shell-ballistic-degree (bounded action $\int\|W_R\|_\infty\le M$, degree $D_R=o(R)\Rightarrow$ freezing at $(1+D_R)/R$) | **APPLIES-AND-VIOLATED** — fixed degree means $D_R=O(1)=o(R)$ in the only (bounded-action) regime where the shell is cheap; the necessity $D_R\gtrsim R$ contradicts the fixed-degree principle, and the ballistic upgrade is then cost-floored by prop:log-shell-ballistic-born-cost |
| 4 | prop:outward-angular-time-budget ($\int_R^\infty dr/r^2=1/R$) | **APPLIES-AND-SATISFIED** — budget respected by inserting beyond $R\gg1/\eta$; not itself a no-go, but it fixes the total density-moving resource available on remote shells |
| 5 | word-level freezing corollary (derived here: $\langle M_X\rangle$-motion $\le C_{S,X}s(\Sigma t_j)(1+G^2)$ with $G=O(1)$ for fixed-degree bounded-height words) | **APPLIES-AND-VIOLATED** — forces the necessary tradeoff $\Sigma t_j\ge c(S,\tau,\lambda)/(s_1(1+G^2))>0$ at $G=O(1)$; the construction's headline "$T=\sum t_j\to0$ at fixed degree and bounded height" is incompatible with vector-norm lens accuracy plus full-sphere leakage control |

### FINAL ASSESSMENT

**NO — the temporal-carrier compiler does NOT pass the radial audit as specified.**
The density-freezing propositions apply to it, not merely to "spatial drift"
architectures: because multiplication flows preserve position densities pointwise,
the lens phase gate $e^{is\tau A_3}|_{\mathrm{span}\{e_0,e_\lambda\}}$ necessarily
moves the displayed two-harmonic density by an $O(1)$ amount, so any architecture
that freezes all multiplication observables excludes the lens *qua phase gate*.
The carrier's one genuinely new scale, the modulation frequency
$\omega\to\infty$, is invisible to every quantity entering the freezing estimates
(kinetic time, harmonic degree, trajectory energy, semiclassical/radial scales):
the proofs integrate exact commutator identities valid for arbitrary temporal
profiles, so fast alternation neither helps nor hurts — it simply purchases nothing.
Concretely: the single-scale insertion satisfies all compatibility hypotheses and is
excluded; the multiscale cascade satisfies $\alpha_q\to0$ and
$\beta_q\gamma_q\to0$ at every depth because depth without scale diversity is free;
and the logarithmic-shell version has fixed degree $D_R=o(R)$ under the bounded
action that makes shells cheap. The numbers check confirms MAIN_RESULT/ADDENDUM's
cost-vs-angular-time reconciliation at large $R$ (outward budget $1/R$; slab cost
$\to0$; consumption $\to0$) but exposes its insufficiency: large $R$ closes the cost
and time ledgers precisely by driving the freezing error to zero. What survives is
sharper than G1 feared: combining the outward budget with the product criterion and
the derived word-level tradeoff, any short-time compiler must generate unbounded
trajectory gradients (ballistic harmonic-degree excursions, $G\to\infty$, equivalently
degree $\asymp R$ gratings or trajectory energies $E_j\sim N_j^2/R_j$) while keeping
$\Sigma t_j\to0$ — i.e., the escape demanded by l. 7093–7097 is real but lies in
spectral/radial scale diversity, which the temporal carrier by design does not
provide. The verdict of MAIN_RESULT.md should be downgraded from LIKELY TRUE to:
word-level Magnus feasibility stands, but G1 resolves NEGATIVELY for the
temporal-carrier mechanism; prob:short-time-radial-compiler remains open only for
architectures with unbounded interacting *spatial/spectral* scales.
