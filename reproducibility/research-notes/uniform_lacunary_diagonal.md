# Uniform lacunary placement and every buffered diagonal (working proof)

## Uniform torus averaging

Let `Theta` be compact and let

\[
 F(k,\vartheta,z_1,\ldots,z_q)
\]

be a compact family in `L^1(I;C(T^q))`.  For every `epsilon>0`, the radii can
be chosen successively and arbitrarily large so that

\[
 \sup_{\vartheta\in\Theta}\left|
 \int_I F(k,\vartheta,e^{2ikR_1},\ldots,e^{2ikR_q})\,dk
 -\int_I\int_{T^q}F(k,\vartheta,z)\,dz\,dk
 \right|<\epsilon.
\]

Proof: uniformly approximate the compact family in the torus variables by a
finite Fourier polynomial.  Choose `R_q` after `R_1,...,R_{q-1}` and use the
Riemann--Lebesgue lemma on every nonzero last Fourier mode.  Induct on `q`.
Uniform decay holds because Fourier transforms vanish uniformly on compact
subsets of `L^1(I)`.

For one finite radial prefix, the closure of the family obtained by varying

- the positive angular smoothing degree `B` (including its strong limit),
- the partial radial cut position inside the last cell, and
- the zonal Galerkin cutoff `L` (including the full-space limit)

is compact in the selected scattering data on a fixed positive-energy window.
The Jost matrices have no positive-real singularities, and every cell has a
fixed finite transfer bound, so the logarithmic loss functions form the compact
family required above.

## Dyadic blocks

Group cells by `2^{n-1}<j<=2^n`.  On

\[
 I_n=\{|s-1|\le w_{2^n}\},\qquad
 w_N=[N\log(N+1)\log\log(N+2)]^{-1},
\]

the robust reciprocal-cascade lemma gives the `q=2^{n-1}`-phase mean block
increment at least `c q`, once that block and the preceding blocks are resolved.
For every unresolved smoothing, partial cell, or cutoff, conditional Hardy
isometry gives nonnegative phase-mean increment.  Apply uniform torus averaging
both on `I_n` and on its complement.  The actual deterministic positions can
therefore be chosen so that the resolved block contributes

\[
 c2^n|I_n|-\epsilon_n\gtrsim\frac{c}{n\log n}-\epsilon_n
\]

to the signed selected loss on the fixed energy window, while every unresolved
or partial later block contributes at least `-epsilon_n`.  Choose
`sum epsilon_n<infinity`.  Since `sum_n 1/(n log n)=infinity`, the signed loss
diverges.

## Quantifiers

Choose increasing resolution thresholds for each finite cell.  Along any
cofinal sequence of positive angular smoothings and radial truncations, the
number of fully included and resolved dyadic blocks tends to infinity.  The
uniform lower bounds above therefore imply divergence along every such
sequence.  The outgoing high-channel coercivity estimate makes the zonal
finite-cutoff radiation column converge to the full one whenever
`L/(B+R+1)->infinity`; unresolved cutoff channels already satisfy the same
nonnegative Hardy phase-mean estimate.  Hence the divergence persists along
every double-buffered Galerkin diagonal, not merely along one hand-picked
radial prefix.

Because every cell is radially mean zero, the relative scalar Jost factor is
identically one.  The uniform positive-log spectral-mass estimate then turns
divergence of the signed loss into divergence of the negative selected-density
entropy.
