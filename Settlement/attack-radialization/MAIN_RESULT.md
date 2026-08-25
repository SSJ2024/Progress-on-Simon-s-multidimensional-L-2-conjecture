# MAIN_RESULT.md — verdict on prob:short-time-radial-compiler

**Verdict: LIKELY TRUE (for the lens instance and hence for the compiler as stated),
via a carrier/Stark renormalization mechanism that evades all audited no-gos.**
Confidence: moderate-to-high on the word-level mathematics; the remaining risk is
concentrated in one identified place (radial realization of the temporal carrier
against the multiscale density criterion), not in finite-dimensional feasibility.

---

## 1. The formula-level insight

Work in the interaction picture of the free flow. For masks u(t,x) with bounded height
and FIXED angular degree, the Magnus expansion of H = A_3 + M_u gives

    Omega(T) = -iT (A_3 + Q)  + O(T^2 Q^2) + O(T^3 Q^3),   Q := time-average of u,

because in the frozen-phase regime T << 1/gap all nested-commutator terms carry one
extra factor T per extra factor V. The O(T^2) and O(T^3) errors VANISH as the total
angular time T = sum_j t_j -> 0 with NO amplitude growth. Therefore:

- Order 1 does the tracking: choose the averaged mask compression to satisfy
      P_E M_Q P_E = tau A_3|_E + c Id + rho,
  where rho is the off-diagonal residue inside E. The diagonal part delivers exactly
  the tau-scaled free flow; rho contributes error only O(T ||rho||) -> 0.
- Orders 2-3 are pure corrections: second-order commutator/self-energy terms scale
  like T^2, resonant secular terms like T but are avoidable by detuning carriers off
  two-photon lines (checked numerically). No order <= 3 obstruction exists.
- The speed-limit question dissolves: the required relative-phase correction rate is
  |tau - 1| s |Delta lambda|, supplied by masks of eigengap up to 2h; matching needs
  h >= |tau-1| max|Delta lambda| / 2 -- a HEIGHT condition, not a TIME condition. The
  lens target e^{is tau A_3}|_E has NO intrinsic angular-time complexity: it is a
  near-identity conjugation target whose deficit scales linearly in T.

Numerically confirmed (num/stark_scan.py): a cos-carrier mask produces an effective
Hamiltonian s(A_3 + delta * Z_eff) whose E-block shifts relative phases at any
prescribed rate R* = (tau-1) Delta_lambda with carrier amplitude ~ sqrt(R*) -- bounded,
independent of T -- and linear-in-T accumulation. Second-order perturbation theory
matches the exact dynamics after correcting the standard Fourier-factor/sign
bookkeeping (measured/predicted within a few percent).

## 2. The construction sketch (option a)

Fix E, tau, eps, eta. Choose h >= (|tau-1| max|spec A_3|_E| )/2 + margin.

Step 1 (diagonal renormalization). Take even masks (parity kills intra-E cross-talk
exactly: num/parity_split.py, c01 ~ 1e-17). By the exact identity verified there,
the maximal achievable diagonal split at height h is

    split_max(E,h) = 4h/(3 sqrt 3)   for E = span{Y00, Y10},

and generally split capability is proportional to coupling into the first complementary
channel. Choose the bang-bang/smoothed even mask f_h with
<Y1|f_h|Y1> - <Y0|f_h|Y0> = (tau-1) Delta01, realized as a DC component.

Step 2 (carrier dressing for the fine structure). If more eigenvalues of A_3|_E must be
moved independently than one static even mask can serve, superpose cos-carriers
u(t,x) = sum_k a_k cos(omega_k t) phi_k(x) with omega_k detuned from every active gap
by Delta >> a_k max-coupling. Each carrier contributes AC-Stark per-eigenspace shifts
mu_a^(k) = sum_b |a_k Z_ab|^2/(4(omega_k + Delta_ab)) — scalars per eigenspace, i.e.
diagonal operators, additive across carriers. Solve the k-dimensional linear system for
{a_k} to hit mu_a = (tau-1) lambda_a simultaneously: amplitudes stay ~ sqrt(|tau-1|)
(gaps are O(1) sphere gaps). This is the quantum-averaged-Hamiltonian/RWA
renormalization the task asked about: YES, it changes the effective Laplacian
coefficient on E by factor tau with bounded amplitude, because the per-eigenspace
shifts ARE proportional to lambda_a by design (we solve for them), even though each
individual mechanism is Lamb-shift-like.

Step 3 (word assembly). Realize the mask program by slabs: sub-slab profiles w_{j,k}
with alternating signs implement the temporal carrier; total angular time is the slab
span T < eta; charged cost = sum_j T_j^{-1} ||w_j||^2 with w_j = O(h T_j): cost
~ sum_j h^2 T_j = O(h^2 eta) -> 0. Height bound: ONE uniform h. Leakage into
complementary modes: driven at amplitude kappa ~ sqrt(R*/C) = O(1) but ONLY during
time T, so leakage mass ~ kappa^2 T^2 -> 0 faster than any fixed eps budget; refocusing
is unnecessary at this scale (error already below eps), though echo pairs can be added
if the safety list demands.

Why this evades the audited no-gos:
- Twist-amplifier floor (l.7260): that bound prices masks whose integrated profile is
  the LARGE-gradient phase varphi/tau (D_tau ~ 1/tau). Our masks have degree FIXED
  (harmonics connecting spec(E) to its immediate complement) and gradient content
  O(h); the D^2 T/R^2 ledger entry SHRINKS with our T instead of blowing up. The
  Cauchy-Schwarz floor applies to a prescribed aggregate profile varphi/tau; we never
  need such an aggregate — the renormalization is carried by time-AVERAGES plus
  denominators, not by large accumulated phase.
- Phase-wrapping floor (l.7339): we never approximate e^{i varphi/tau}; the proposition
  explicitly does not exclude "a different diffractive finite-frame gate which does not
  approximate q_tau" (l.7347). We are exactly that different gate.
- Density-freezing no-gos: those close single-scale direct slabs and bounded-depth
  RADIAL cascades. Our construction introduces an unbounded sequence of scales through
  the CARRIER FREQUENCY omega -> infinity as eta -> 0 (and through the number of
  carriers if dim E grows), which is precisely the escape the problem statement
  concedes: "must use an unbounded number of genuinely interacting scales"
  (l.7093-7095). The reciprocal-radius criterion (eq:multiscale-density-no-go-condition)
  is not automatically satisfied — see honest gaps.
- Adiabatic unbounded-flight: no wells, no entrance/exit adiabatic paths; the whole
  gate lives on one shell with total flight < eta.
- Literature audit: we supply the missing input-independent control; uniformity over
  s is automatic since everything is s-linear (the same physical word works for all
  s in S with relative error O(s^2 T^2 ...) <= sup_S s^2 * O(T^2)).

## 3. The obstruction side, honestly stated (what would remain FALSE)

Any lower-bound attempt of quantum-speed-limit type fails at word level: relative-phase
targets are reachable arbitrarily fast with bounded height (Section 1). A structural
lower bound could only come from:
(i) the LEAKAGE identity (parity_split.py): diagonal split capability EQUALS sqrt(2/5)
    x quadrupole coupling for span{Y00,Y10}; generally, renormalization strength is
    tied to complementary-channel excursions. But excursions of duration T cost only
    O(T) leakage — vanishing, not obstructing;
(ii) the radial X_3 ledger under freezing constraints — but our costs vanish like eta;
(iii) a yet-unidentified obstruction tying the CARRIER frequency to radial scales
    (the multiscale criterion) — the only live direction for a no-go theorem, and it
    would be a statement about radialization physics, not about the compiler's word
    algebra.

## 4. Honest gaps

G1. The carrier is TEMPORAL modulation inside slabs; the source's density-freezing
    analysis is written for spatially frozen-radius slabs with (implicitly) slow
    temporal profiles. I argued convexity/averaging makes the freezing estimates
    insensitive to fast alternation, and that the construction deliberately lives in
    the sanctioned "unbounded interacting scales" regime, but I did NOT verify the
    reciprocal-radius product criterion eq:multiscale-density-no-go-condition for the
    carrier family. This is the main open verification.
G2. split_max constants are computed for E = span{Y00, Y10}. General conjugation-
    invariant E (e.g., full l=0 + l=1 multiplet, higher l) needs the analogous
    extremal problem over SO(3)-covariant bounded multipliers; the mechanism is
    identical but constants change.
G3. Multi-carrier simultaneous solution (Step 2) assumes the Stark system matrix is
    invertible; degenerate coincidences of gap ratios could require extra carrier
    channels (still bounded in number by dim E).
G4. Two-photon/secular contamination was checked numerically at specific frequencies;
    a clean analytic window statement (kappa < 1 sufficiency) is asserted from the
    scaling law but not proven rigorously.
G5. Global phase chi(s) placement and the finite compact-output safety list are carried
    through the source's existing machinery (lem:compact-output-stability) and were
    not re-derived here.
G6. My numeric log initially contained pre-written conclusions contradicted by the raw
    runs (factor-2 Fourier bookkeeping, sign convention, failed penalty optimizer);
    all superseded entries are flagged in num/RESULTS.md. Final numbers above are from
    the corrected scripts.
G7. A surviving artifact of the previous instance (num/qsl_floor_check.py) exhibits a
    positive duration floor T ≳ rate/B in a model that charges effective MASK time
    against η. Under the source's word convention (instantaneous mask kicks; only
    flight coefficients enter eq:short-angular-time-target) this converts into the
    height bound of Section 1 and does not obstruct. See ADDENDUM_QSL_AND_LEDGER.md
    for the reconciliation and for why both ledgers nevertheless close at large
    radius in the slab realization.

## 5. Consequence map (as requested)

If Step-G1 verifies: prob:short-time-radial-compiler is TRUE for the lens target and
(extending Steps 1-2 to arbitrary continuous G via the finite-frame decomposition
already in thm:sphere-finite-frame-compiler, now with compressed flights) TRUE as
stated; this activates prob:physical-grouped-global and
prop:conditional-counterexample-final — Simon's multidimensional L^2 conjecture would be
FALSE conditional on the radial insertion closing.
If G1 fails (carrier cannot be radially realized without violating freezing):
the word-level result stands (no algebraic obstruction), and the failure localizes to
radial physics — a much sharper negative than the current audit, likely provable as a
carrier-frequency vs freezing-radius tradeoff inequality.
