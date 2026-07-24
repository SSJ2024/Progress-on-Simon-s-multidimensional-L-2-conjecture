# Riesz--Talbot reciprocal cell (working proof)

## Angular factor

On the flat fast variable put `D=-d_x^2` and

\[
 U_s=e^{-i\pi sD/2}e^{-ias\cos x},\qquad 0<a<\pi/4.
\]

At `s=1`, even and odd Fourier modes give

\[
 U_1 1=g(x)=\cos(a\cos x)-\sin(a\cos x)>0,
 \qquad p=g^2=1-\sin(2a\cos x),
\]

with mean `int p=1`.  If `X=log p`, strict Jensen gives
`int X<0`, while the tilted mean `int pX=D_p` is positive.  Choose
`0<alpha<D_p`.  For superlacunary integer frequencies `L_t`,

\[
 P_m(\theta)=\prod_{t=1}^m p(L_t\theta),\qquad
 E_m=\{\log P_m\ge \alpha m\}.
\]

The ordinary measure of `E_m` is `O(e^{-alpha m})`; Chernoff under the
`p`-tilted law gives `int_{E_m^c}P_m|f|^2 <= C e^{-c m}||f||^2`, uniformly
on any prescribed finite-dimensional smooth incoming space.  Superlacunarity
is chosen successively so that all exponential-moment factorizations used by
Chernoff hold in operator norm on that space.  Positive spherical smoothing of
`1_{E_m}` gives a finite-band `0<=chi_m<=1` with the same estimates up to an
arbitrarily small error and `||chi_m||_2^2 <= C e^{-c m}`.

For `cos(L theta)=T_L(cos theta)`, the exact spherical factor satisfies

\[
 e^{-i\pi sA_3/(2L^2)}e^{-ias\cos(L\theta)}f
 =g_s(L\theta)f+O_K(\sqrt{\log L}/L).
\]

The reverse physical factor is a sign-reversed mask after a `3pi/2` scaled
free flight.  At `s=1` it is the inverse quarter-Talbot factor on the fast
microstructure, up to the same curvature error.  Reversing the order of the
`m` factors gives `W_1U_1=I+O(epsilon)` on the incoming space, while

\[
 ||W_sU_s-I||+||(I-\chi_m)U_s||
 \le C(m|s-1|+e^{-cm}+\epsilon).
\]

## Radial realization

A smooth weak slab of length `T` and amplitude `T^{-1}w(omega)` has outgoing
transmission `exp[-iw/(2k)]`, reflection `O_K(T^{-1})`, and charged cost
`O(||w||_2^2/T)`.  The integer frequencies can all be chosen odd, so the
zonal masks have exactly zero spherical mean.  A free collar from `r_0` to
`r_1` supplies

\[
 \exp\left[-\frac{iA_3}{2k}(r_0^{-1}-r_1^{-1})\right].
\]

Choose the cell radius and all integer frequencies so that the prescribed
quarter and inverse-quarter angular times fit, every slab length is much
smaller than its available radial interval, and the largest cell bandwidth is
`o(R)`.  The base frequency can be taken arbitrarily large after all finite
operator-norm and cost tolerances are fixed, so these requirements are
compatible even for `m` superlacunary factors.

One explicit scale choice is as follows.  After the finite ratios between the
`m` fast frequencies and the smoothing multiplier needed for `chi_m` have been
fixed, choose an odd base frequency `L_*` so large that

\[
 D_{\rm in}\ll L_*,\qquad
 B_{\rm cell}\ll L_*^{3/2},\qquad
 T_{\max}\ll L_*^4/L_{\max}^2.
\]

Put the focus radius `R\asymp L_*^2`.  The last inequality fits every weak
slab into its free-flight interval.  The second gives both
`B_cell/R=o(1)` and the uniform outgoing Hankel error
`B_cell^4/R^3=o(1)`.  The quarter and inverse-quarter times use fixed
fractions of `1/R`, so the complete forward--barrier--reverse cell lies in an
annulus with radii comparable to `R`.  All constraints are finite before
`L_*` is chosen and hence can be made as small as the prescribed cell error.

At the focus insert

\[
 Q(r-R)\,[\chi_m(\omega)-\langle\chi_m\rangle],
\]

where a fixed real compact bump `Q` has nonzero one-dimensional reflection on
the energy window.  The radial mean is exactly zero, its charged cost is
`O(e^{-cm})`, and on the concentrated image it has the fixed hyperbolic
coefficients `a(k),b(k)` of `Q`, up to `O(e^{-cm}+epsilon)`.  The reverse
Talbot train refocuses the transmitted block.  Volterra estimates for the
outgoing/incoming envelopes make all statements uniform on the prescribed
finite incoming space and compact energy interval.

All masks and barriers can be chosen zonal.  Hence the selected evolution stays
in the azimuthal `m=0` sector; the active angular block has one channel per
degree, and no azimuthal bookkeeping is needed.

For `m_j=C log(j+1)`, choose `C` so that the barrier costs and concentration
errors are summable.  Choose slab lengths so that the sum of all mask costs and
reflections is also finite.  Disjoint cells then define one bounded real
mean-zero scalar potential in `X_3`.

## Translation and all diagonals

The reflected block of a cell at radius `R` has the common radial phase
`z=e^{2ikR}`; all degree-dependent Bessel factors remain in its coefficient
`B_R(k)`.  The flux identity gives the Hardy phase isometry for every real
angular smoothing, every partial radial cell, and every Galerkin cutoff, so the
phase-mean selected loss is nonnegative even when that model does not resolve
the Riesz cell.

For a resolved cell and `|s-1|<=w_j`, reciprocal synchronization makes the
phase-mean loss at least a fixed `c_0>0`.  Cell positions are selected
superlacunarily by a uniform Riemann--Lebesgue lemma over the compact closure of
all smoothing degrees, partial-cell cut positions, and Galerkin cutoffs.  This
ensures actual energy-integrated increment at least `c_0|I_j|-epsilon_j` on
`I_j={|s-1|<=w_j}`, and at least `-epsilon_j` on its complement.  Taking
`epsilon_j` summable relative to `|I_j|` and

\[
 w_j=[j\log(j+1)\log\log(j+2)]^{-1}
\]

forces divergent signed selected loss for every cofinal smoothed, radially
truncated, double-buffered Galerkin diagonal.  The already proved uniform bound
on positive logarithmic density then converts signed divergence into divergence
of the negative entropy.
