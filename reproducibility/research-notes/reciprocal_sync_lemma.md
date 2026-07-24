# Reciprocal phase synchronization lemma (working proof)

Let `a=cosh(rho)`, `b=sinh(rho)`, and let `H` be the symmetric unitary
reciprocal phase on a finite active angular block.  An ideal refocused barrier
acts by

\[
  \Phi_z(H)=(aI+zbH)^{-1}(aH+\bar z bI),\qquad |z|=1.
\]

For scalar phases `h,lambda` on the unit circle,

\[
 |\Phi_z(h)-\Phi_z(\lambda)|
 =\frac{|h-\lambda|}
 {|a+zbh|\,|a+zb\lambda|}.
\]

The identity follows by cross multiplication; its numerator is
`(a^2-b^2)(h-lambda)=h-lambda`.  In particular, at a synchronized phase
`lambda` the projective derivative is

\[
 L_z(\lambda)=|a+zb\lambda|^{-2}.
\]

It satisfies

\[
 \mathbb E_z L_z=1,
 \qquad
 q_\beta:=\mathbb E_z L_z^\beta<1
 \quad(0<\beta<1),
\]

the second assertion being strict Jensen because `L_z` is nonconstant.  For a
spectral measure supported in a sufficiently short arc, the reweighting of that
measure by the selected inverse state changes the corresponding fractional
pair-dispersion only by `1+O(d)`.  Hence, for some `d_0>0`, `q<1`, and
`C<infinity`,

\[
 \mathbb E_z d_+^\beta\le qd^\beta+C\eta^\beta
\]

whenever the cell differs from the ideal scalar cell by projective error at
most `eta` and `d<=d_0`.

There is an elementary dimension-free way to keep the process in this local
regime.  If the spectrum of `H` lies in an arc `I`, its ideal image lies in the
arc `Phi_z(I)` and

\[
 |\Phi_z(I)|=\int_I |a+zbe^{i\theta}|^{-2}\,d\theta.
\]

The phase average of this length equals `|I|`, while strict concavity gives a
uniform fractional-moment contraction for arcs of length at most a fixed
`ell_0<2pi`.  To blow a short arc up past `ell_0`, the random repelling point
must fall within `O(|I|+eta)` of that arc; this has probability
`O(|I|+eta)`.  Starting from a point and adding projective cell errors
`eta_j`, the probability of such an excursion through time `N` is bounded by
`C sum_{j<=N}eta_j`; on its complement the fractional-moment recursion above
applies.  This proves the required stochastic stability without a dimension
factor or a general random-dynamical-systems theorem.

Consequently, if a cell made from `m_j` Talbot factors has

\[
 \eta_j(s)\le C m_j|s-1|+\epsilon_j,
 \qquad m_j\asymp\log(j+1),
 \qquad \sum_j\epsilon_j^\beta\ll1,
\]

then the following conservative finite-cascade statement is sufficient.  For
`N>=3`, put

\[
 |s-1|\le w_N,
 \qquad
 w_N=\frac{c}{N\log(N+1)\log\log(N+2)}.
\]

The total chromatic defect through the first `N` cells is then bounded by
`w_N sum_{j<=N}m_j=O(1/log log N)`.  Thus the excursion probability tends to
zero, apart from an arbitrarily small summable physical-error budget.
Stochastic stability of the Mobius recurrence gives

\[
 \mathbb E_{z_1,\ldots,z_N}
   [-\log\|J_N(s,z)^{-1}e_0\|]
 \ge c_0N-C.
\]

Equivalently, all but `o(N)` cells have a fixed positive conditional Hardy loss
in phase average.  Use dyadic blocks `2^{n-1}<j<=2^n` and the common window
`|s-1|<=w_{2^n}`.  The `n`-th block contributes at least

\[
 c2^n w_{2^n}\asymp\frac{c}{n\log n}
\]

to the energy-integrated signed loss.  The sum over `n` diverges.  This dyadic
form is preferable to a cell-by-cell window because only one oscillatory
averaging problem is needed per block.

Two facts must remain explicit in the final proof:

1. the random-circle synchronization is applied to the reciprocal scattering
   phase, not to an arbitrary state vector;
2. the deterministic shell locations are selected by uniform oscillatory
   averaging over the compact family of angular smoothings, radial partial
   cells, and Galerkin cutoffs.
