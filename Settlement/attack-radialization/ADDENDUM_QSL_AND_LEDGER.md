# ADDENDUM — QSL-floor remnant, ledger reconciliation, and the slab bookkeeping

## 1. Provenance

`num/qsl_floor_check.py` is a surviving artifact of the earlier (lost-context)
instance. Its scope note already concedes the decisive point: it charges MASK TIME
against the eta budget, i.e. it studies the stricter pairwise model
H = A_3 + u(t) M_Q with |u| <= B and total duration eta, NOT the source's word ledger.

Its results (run 2026-08-25, see terminals log):
- T1 (population swap |0>->|1>, fidelity .99): T_min ~= 4.71 / 2.17 / 0.80 for
  B = 0.25 / 0.5 / 1.0 — scaling ~ const/B, slightly beating the Rabi prediction
  pi/(2B) = 6.28 / 3.14 / 1.57 (the diagonal entry 2 in M_Q assists).
- T2 (gate chi*exp(i*tau A_3), tau = 2, B = 0.5): fidelity 0.94 at eta = 0.7,
  0.998 at eta = 1.0; non-monotone middle values are optimizer artifacts.
  => In the mask-time-charged model there IS a positive duration floor
  T >= ~ (target relative-phase rate)/(max available split rate).

## 2. Which ledger does prob:short-time-radial-compiler use?

TEXTUAL ANSWER (SCALING_NOTES section 4): the word is
    W_s = prod_j ( e^{-i s t_j A_3} e^{-i s M_{q_j}} ),
masks enter as instantaneous kicks; eq:short-angular-time-target (l. 7040) sums ONLY
the flight coefficients t_j. The mask-time floor above therefore does NOT apply at
word level. What applies instead is the HEIGHT condition derived in
MAGNUS_FEASIBILITY section 5:

    h >= (|tau - 1| / 2) * max |spec(A_3|_E)|     (+ carrier margin),

and the error/leakage terms vanish like O(s^2 T^2 h^2) + O(s T ||rho||) as
T = sum t_j -> 0. The earlier instance's own scope note agrees ("does not obstruct
the lens target ... where the mask compression can realize the split statically").

## 3. The subtle point both readings must respect: slabs consume angular time too

In the radial realization, realizing one kick by a weak slab of frozen-radius length
T_slab at radius r consumes angular kinetic time ~ T_slab / r^2 INSIDE the slab (the
free A_3/r^2 keeps acting), and this is part of the same outward budget
(prop:outward-angular-time-budget proof: slabs "consume their share"). The apparent
conflict — small cost wants LONG slabs (cost = ||w||^2/T_slab), small angular time
wants SHORT slabs — is resolved by going farther out:
    T_slab <= eps R (freezing),   cost -> ||w||^2/(eps R) -> 0,
    angular consumption <= eps R / R^2 = eps/R -> 0.
Both ledgers close simultaneously at large radius. This is why the problem is about
COMPRESSING THE FLIGHT SUM before insertion, and why the compiler result is not
vacuous.

## 4. Consequence for the verdict

Unchanged: LIKELY TRUE. The QSL remnant is retained as evidence that any alternative
convention charging effective mask durations into sum t_j produces a genuine
positive floor (~ rate/B with B the height cap); under the source's convention the
floor converts into the height lower bound above plus vanishing error terms. A
referee insisting on the stricter convention would flip the verdict to FALSE-with-
quantitative-bound T >= c(tau, E)/h_max; the source text supports our convention.
