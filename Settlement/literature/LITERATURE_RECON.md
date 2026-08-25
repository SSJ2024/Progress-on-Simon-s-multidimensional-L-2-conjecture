# LITERATURE RECONNAISSANCE: Simon's Multidimensional L^2 Conjecture

**Compiled:** 25 August 2026 (automated literature recon, WebSearch + WebFetch)
**Scope:** Status of the multidimensional L^2 conjecture; partial results; embedded-eigenvalue counterexamples; 2020–2026 arXiv activity; control-theory side for internal reduction.

---

## EXECUTIVE VERDICT (TL;DR)

1. **The conjecture is OPEN in every dimension d ≥ 2**, as of August 2026. There is **no published proof and no published disproof** for any d ≥ 2, including d = 2, 3, and also d ≥ 4. The user's prior belief that "d ≥ 4 or d ≥ 5 may be settled positively by Killip–Visan type results" could **not be verified**: no Killip–Visan paper resolving the multidimensional L^2 conjecture exists in any dimension (the famous Killip–Visan papers of that name concern *nonlinear* Schrödinger equations — mass/energy-critical NLS well-posedness — a completely different subject that pollutes keyword searches).
2. **No known counterexample** constructs V in the weighted-L^2 class of Conjecture 20.2 destroying AC spectrum on an interval in d ≥ 2. The closest negative results (Frank–Simon, Bögli–Cuenin, Ionescu–Jerison) all live at decay rates / integrability classes strictly weaker than what the conjecture assumes.
3. On the control side, **no theorem is known producing one input-independent control approximating a prescribed unitary uniformly over a parameter continuum in arbitrarily small time**. The ensemble-control literature gives state-to-state transfers under non-resonance gap conditions (Liang–Boscain–Sigalotti), and small-time controllability on manifolds via saturation/diffeomorphism methods (Chambrion–Pozzoli 2023, Beauchard–Pozzoli 2025) — but not uniform-in-parameter unitary approximation.

---

## PART 1 — THE CONJECTURE AND ITS CURRENT STATUS

### 1.1 Statement (Simon, Conjecture 20.2)

Source: B. Simon, "Tosio Kato's work on non-relativistic quantum mechanics, Part 2," *Bull. Math. Sci.* **9**, 1950008 (2019). [PDF: https://math.caltech.edu/SimonPapers/R62.pdf]

> Let d ≥ 2 and let V be real-valued with
> ∑_{n∈Z^d} ||n||^{2(1+ε)} ||V||²_{L²(cell n)} < ∞   (some ε > 0),
> i.e., roughly V ∈ L²(R^d) with polynomial weight (1+|x|)^{1+ε}. Then −Δ + V has absolutely continuous spectrum of infinite multiplicity on (0, ∞) (equivalently: essential support [0, ∞), with σ_ac ⊇ (0,∞)).

The equivalent "Denisov form" (used throughout the survey literature): with H = −Δ + V on L²(R^d),

    ∫_{R^d} |V(x)|² / (1 + |x|^{d−1}) dx < ∞   ⟹   [0, ∞) ⊆ σ_ac(H), of infinite multiplicity.

Note the two forms are *not* literally identical as function spaces but are the same scale of condition; both appear in the sources below.

### 1.2 Status as of August 2026: OPEN FOR ALL d ≥ 2

- S. A. Denisov, ["Multidimensional L² conjecture: a survey"](https://arxiv.org/abs/1203.4255) (2012): *"This conjecture was completely solved only for d = 1"* (Deift–Killip). Even pointwise |V(x)| ≲ (1+|x|)^{−(1−)} is unknown in d ≥ 2. Denisov's companion paper with Nikolskii ([people.math.wisc.edu/~denissov/nikolskii.pdf](https://people.math.wisc.edu/~denissov/nikolskii.pdf)) resolves an analogue on the Cayley tree — explicitly flagged there as the model where "the true multidimensional L² condition" works — but this does not transfer to Euclidean space.
- O. Safronov's survey ("Spectral properties of multi-dimensional Schrödinger operators with slowly decaying potentials", in *Spectral Theory of Differential Operators*, AMS 2011) states the same open status and remarks it is *"not clear what is the proper generalization of condition [Deift–Killip] in d ≥ 2."*
- Targeted searches for claimed resolutions ("L² conjecture solved/disproved", "Denisov conjecture", 2024–2026 arXiv activity) returned **nothing** claiming resolution in any d ≥ 2. The most recent adjacent item found is ballistic transport for discrete multi-dimensional decaying potentials (arXiv:2507.04988, July 2025), which *presupposes* AC spectrum rather than proving it under the L²-type hypothesis.
- No retraction/correction trail, no blog or referee-level dispute about a claimed solution was found.

**Conclusion for RQ1:** As of 2026-08-25 the conjecture remains open in d = 2, 3 (and all d ≥ 4).

---

## PART 2 — KEY PARTIAL RESULTS, AND WHERE THE DIMENSIONAL FRONTIER ACTUALLY IS

### 2.1 Dimension d = 1 (settled, the template)

- P. Deift, R. Killip, ["On the Absolutely Continuous Spectrum of One-Dimensional Schrödinger Operators with Square Summable Potentials"](https://doi.org/10.1007/s002200050615), *Comm. Math. Phys.* **203** (1999) 341–347. V ∈ L²(R) ⟹ AC spectrum preserved on [0, ∞).
- R. Killip, B. Simon, ["Sum rules for Jacobi matrices and their applications to spectral theory"](https://doi.org/10.4007/annals.2003.158.253), *Ann. of Math.* **158** (2003) 253–321 (discrete analogue); B. Simon, ["Sum rules and spectral measures of Schrödinger operators with L² potentials"](https://arxiv.org/abs/math/0608767), *Ann. of Math.* **170** (2009) 739–782 (continuous version).
- Extensions to ℓ¹-weighted variants: Kiselev–Last–Simon; higher-order sum rules: Kupin.

### 2.2 Multidimensional partial positives (all require MORE than L²-with-weight)

The honest summary is: every positive result in d ≥ 2 adds structure — oscillation, Fourier-side regularity, radial/angular regularity, cone localization, or randomness. None handles the bare weighted-L² class.

**(a) Laptev–Naboko–Safronov program (oscillatory/Fourier-side conditions), d ≥ 3.**
- A. Laptev, S. Naboko, O. Safronov, ["Absolutely continuous spectrum of Schrödinger operators with slowly decaying and oscillating potentials"](https://doi.org/10.1007/s00220-004-1157-9), *Comm. Math. Phys.* **253** (2005) 611–631. Method: bound spectral measures by eigenvalue sums of −Δ+V and −Δ−V; requires oscillation of V̂ (decay of the partial Fourier transform in one variable). Valid for **d ≥ 3**; the authors themselves note *"the validity of [these methods] in dimension d = 2 remains open."* ([paper PDF](https://www.ma.ic.ac.uk/~alaptev/Papers/schr2.pdf))
- A. Laptev, S. Naboko, O. Safronov, "A Szegő condition for a multidimensional Schrödinger operator," *J. Funct. Anal.* **219** (2005) 285–305.
- Cone refinements: Damanik–Killip–Simon-type extension by B. Simon student lineage — specifically the mp_arc 06-159 paper (R. Killip & collaborators' circle; see [web.ma.utexas.edu/mp_arc/c/06/06-159.pdf](https://web.ma.utexas.edu/mp_arc/c/06/06-159.pdf)) proves AC support in d ≥ 3 when the potential decays slowly only inside a cone, arbitrary bounded potential outside.

**(b) Safronov's typical-potential and div-Q results (any d, incl. d = 2, but with extra hypotheses).**
- O. Safronov, ["Absolutely continuous spectrum of multidimensional Schrödinger operator"](https://arxiv.org/abs/math/0408376) (2004): for V = div Q with Q slowly decaying, d = 3 (method generalizes to other d), AC fills R⁺.
- O. Safronov, ["On the absolutely continuous spectrum of multi-dimensional Schrödinger operators with slowly decaying potentials"](https://doi.org/10.1007/s00220-004-1161-0), *Comm. Math. Phys.* **254** (2005) 361–366.
- O. Safronov, ["Absolutely continuous spectrum of a typical Schrödinger operator with a slowly decaying potential"](https://arxiv.org/abs/1111.5552) (2012) and ["For a.e. coupling constant" results](https://doi.org/10.1090/s1061-0022-2013-01275-1), *Trans. AMS* (2013): for V with ∫|∇_θ V|²-type angular regularity, −Δ + αV has essentially supported AC on [0,∞) **for a.e. α**. These are "almost every coupling" statements — they do NOT give AC for each fixed operator.

**(c) Perelman.**
- G. Perelman, "Stability of the absolutely continuous spectrum for multidimensional Schrödinger operators" (cited as *Russ. J. Math. Phys.* or similar, mid-2000s): stability under perturbations of periodic-type backgrounds with slow decay.

**(d) Random potentials.**
- For random decaying potentials, AC spectrum holds under much weaker moment assumptions than deterministic L²; see e.g. Safronov's works and references therein. This is a genuinely different mechanism (averaging kills coherent reflection).

**(e) What about "high dimensions are easier"?**
There is folklore that high-dimensionality helps (more transverse directions to escape along; Wigner–von Neumann-type traps concentrate near lower-dimensional sets). The Ionescu–Jerison construction indeed exploits concentration near (d−1)-dimensional planes, and its critical exponent (d+1)/2 grows with d — consistent with high-d being "safer". However:
- **No theorem converts this into AC spectrum under the bare weighted-L² class in any d ≥ 2.** In particular the attribution "d ≥ 4 or d ≥ 5 settled by Killip–Visan" is a **misattribution**: the actual Killip–Visan corpus (see §2.3) is about NLS, not about this conjecture. Searches across arXiv math.SP/math.AP, Google Scholar, and review articles surfaced no result of the form "for d ≥ k₀, weighted-L² implies AC."
- The only rigorous "dimension threshold" statements adjacent to the conjecture are (i) absence-of-positive-eigenvalue thresholds (Koch–Tataru: V ∈ L^{(d+1)/2} suffices to exclude embedded positive eigenvalues; sharp by Ionescu–Jerison) and (ii) Lieb–Thirring/eigenvalue-sum bounds whose exponents change with d. Neither yields the full conjectural conclusion (essential support + infinite multiplicity) from the conjecture's hypothesis.

### 2.3 The "Killip–Visan" red herring (verification note for RQ2)

Searches for "Killip Visan multidimensional Schrödinger L² conjecture" return mostly their NLS papers (focusing energy-critical NLS in d≥5; mass-critical radial d=3; Strichartz estimates on tori, etc.). E.g. [Killip's publication list](https://www.math.ucla.edu/~killip/Preprints.html) contains no paper on the multidimensional L² problem. The confusion likely arises because "Killip–Visan" co-occurs with "multidimensional Schrödinger" in PDE contexts. **Verdict: the claim "d ≥ 4/5 settled" is unsupported by the literature; treat it as false until a specific reference is produced.**

### 2.4 Other named tools mentioned in the brief

- **Bär–Ballmann**: C. Bär, W. Ballmann, "Boundary value problems for elliptic differential operators of first order" (and follow-ups with Rohleder et al.) provide boundary-triple/Weyl-function machinery characterizing AC spectrum for elliptic operators (e.g., [Behrndt–Rohleder-type applications](https://doi.org/10.1016/j.aim.2015.08.016)). This is infrastructure for *proving* AC given enough information about solutions — it has not been combined with the weighted-L² class to yield new cases of the conjecture.
- **Multichannel WKB**: Denisov's survey emphasizes the WKB correction picture (evolution equation for wave propagation through slowly-decaying media) and Itô-diffusion/paths-space reformulation (Denisov, ["Itô's diffusion in multidimensional scattering"](https://arxiv.org/abs/1106.2155)); the Cayley-tree case is fully solved (Denisov; Kupin) precisely because paths-space sum rules close there. No multichannel WKB proof of the Euclidean conjecture exists.

**Bottom line for RQ2:** Open for ALL d ≥ 2. Closest positive results: Laptev–Naboko–Safronov (d ≥ 3 + oscillation), Safronov a.e.-α results (any d + angular regularity), Deift–Killip/Killip–Simon (d = 1, exact class), Cayley tree (exact analogue). The d = 2 case resists even the oscillatory method.

---

## PART 3 — NEGATIVE RESULTS: EMBEDDED EIGENVALUES AND WHY L² IS BORDERLINE

These delimit how far one can weaken the hypothesis before things break. Crucially, none reaches the conjecture's own class.

### 3.1 Classical Wigner–von Neumann (d = 1, but radially embeds in all d)
Wigner–von Neumann potential ~ sin(2x)/x produces an eigenvalue at λ = 1. Note: |sin(2x)/x| ∈ L^q(R^d) iff q > d (radial embedding). So VvN ∈ L^q ∀ q > d — far weaker summability than weighted L²? Careful: weighted-L² (weight |x|^{2(1+ε)}) FAILS for 1/x-type decay (∫ r^{2} · r^{−2} · r^{d−1} dr = ∞). So the classical example is *outside* the conjectured class — good news for the conjecture.

### 3.2 Kiselev–Last–Simon and successors: dense singular/pure point spectrum from sparse oscillatory potentials
- Kiselev–Last–Simon ("Modified Prüfer and EFGP transforms…", *Anal. PDE* / *J. Anal. Math.* era works) construct potentials decaying pointwise like o(1/x) (even faster on average) with prescribed (dense!) pure point spectrum embedded in (0,∞) — but these use delicate phase engineering along the line; the constructions are 1D. Simon's "arbitrary positive pure point spectrum" examples (following Naboko) show AC can be destroyed on intervals by potentials decaying like x^{-1/2}-type oscillatory — again outside the L²-weighted class.
- Naboko–Simonov-type results: for Wigner–von Neumann sums with amplitudes c_k, eigenvalues occur exactly at α_k²/4 when Σ|c_k|² = ∞ vs < ∞ dichotomy — the L² borderline appears already in 1D oscillatory theory. See ["Schrödinger operators with slowly decaying Wigner–von Neumann type potentials"](https://arxiv.org/abs/1201.4840) (Kiselev et al.).

### 3.3 Frank–Simon: small-norm embedded eigenvalues, optimal exponent (d+1)/2
- R. Frank, B. Simon, ["Eigenvalue bounds for Schrödinger operators with complex potentials. II"](https://doi.org/10.4310/JST.2017.v7.n3.a4), *J. Spectr. Theory* 7 (2017) 633–658, building on Ionescu–Jerison: there exist real V_n ∈ L^q(R^d) for ANY q > (d+1)/2 with ‖V_n‖ → 0 and −Δ + V_n possessing an embedded eigenvalue at λ = 1.
- Context: Koch–Tataru prove NO embedded positive eigenvalues for V ∈ L^{(d+1)/2}(R^d); Ionescu–Jerison's example shows sharpness. Their potential concentrates near a (d−1)-plane (decays 1/|x₁| along it, 1/|x'|² across).
- **Relation to the conjecture:** L^q(R^d), q > (d+1)/2, does NOT imply the conjecture's weighted L² (which forces q ≥ 2 with weight). Conversely weighted-L² does not imply L^{(d+1)/2}. The Frank–Simon examples live in a *different*, overlapping-but-not-containing regime; they do NOT disprove the conjecture. They do show the conjecture is "close to the edge": if one weakened the weight exponent from (1+ε) toward ½-ish integrability thresholds, counterexamples exist.

### 3.4 Complex potentials: Bögli–Cuenin kill Laptev–Safronov conjecture (not ours)
- S. Bögli, J.-C. Cuenin, ["Counterexample to the Laptev–Safronov conjecture"](https://doi.org/10.1007/s00220-022-04546-z), *Comm. Math. Phys.* **398** (2023) 1349–1370: complex V ∈ L^q, q ∈ ((d+1)/2, d], with eigenvalues accumulating at every point of [0, ∞). Non-selfadjoint setting; Fermi golden rule blocks naive real-valued transplant. Also: Frank (Bull. LMS 2011) proved LS-conjecture true for q ≤ (d+1)/2; Bögli (radial counterexample) killed q ≥ d/2 radial range; Frank–Simon gave the z ∈ R⁺ real-part obstruction. Full picture in recent surveys (e.g. [arXiv:2408.15783](https://arxiv.org/pdf/2408.15783)).
- **Relevance:** demonstrates that at q just above the (d+1)/2 threshold, even *bounded* potentials can create spectrum-filling discrete eigenvalues (complex case) — the strongest current evidence that L²-without-structure is dangerous territory. But no real-valued counterpart reaching our class is known.

### 3.5 Taimanov–Tsarev / Novikov–Veselov Moutard constructions (d = 2)
- I. Taimanov, S. Tsarev: 2D rational Wigner–von Neumann potentials with fast-decaying rational tails and multidimensional L²-kernel (via Moutard transformation), Russ. Math. Surveys 62 (2007); extended by ["Two-dimensional von Neumann–Wigner potentials with a multiple positive eigenvalue"](https://arxiv.org/abs/1307.5141) (Naboko–Simonov school, ~2013): explicit 2D potentials decaying like 1/|x| with multiple embedded eigenvalues. Decay 1/|x| ⇒ outside weighted-L²(1+ε) class. These are the sharpest *explicit* 2D embedded-eigenvalue machines, still above the conjecture's decay floor.

### 3.6 Verdict for RQ3
No published construction places V inside the Conjecture-20.2 class while killing AC on an interval. The "danger zone" evidence (Frank–Simon, Bögli–Cuenin, KLS/Naboko) consistently sits at decay/integrability levels strictly weaker than weighted-L²(ε>0). Any attempted disproof would have to thread between:
(i) Deift–Killip-style sum-rule obstructions (which in d=1 exactly protect the L² level), and
(ii) the Wigner–von Neumann reflection mechanism, which needs ~1/r oscillatory tails incompatible with the weight.
This is why the conjecture is considered plausible yet hard.

---

## PART 4 — RECENT ARXIV ACTIVITY (2020–2026): REFINEMENTS ADJACENT TO THE CONJECTURE

Nothing claims resolution. Notable adjacent items:

1. **Ballistic transport, discrete multi-d, decaying potentials** — [arXiv:2507.04988](https://arxiv.org/abs/2507.04988) (July 2025): Mourre/commutator methods, V_n = o(|n|^{-1}), arbitrary d. Presumes AC subspace; quantitative transport. Sign of life in the area; no attack on the conjecture itself.
2. **Eigenvalue sums for complex radial potentials** — [arXiv:2408.15783](https://arxiv.org/abs/2408.15783) (Aug 2024): sharpens Frank–Sabin trace-ideal resolvent bounds; documents the complete current map of single-eigenvalue bounds (Frank 2011; Frank–Simon 2017; Bögli–Cuenin 2023; Bögli radial counterexample).
3. **Random Schrödinger with complex decaying potentials** — [APDE 18 (2025) 279ff](https://doi.org/10.2140/apde.2025.18.279): randomized versions of the tube-concentration counterexamples; shows randomness destroys the bad examples almost surely up to scale h ≤ ε^{...}; interesting inversion of the usual intuition (randomness HELPS here).
4. **Frank–Sabin spectral machinery** (uniform Sobolev/Strichartz in Schatten classes, [arXiv:1404.2817](https://arxiv.org/abs/1404.2817), *Duke*/*Mem. AMS*-lineage): the standard modern engine behind eigenvalue bounds; used negatively (to bound possible eigenvalues) rather than to build AC.
5. **Web–Sagawa–Aomoto-type trace identities**: not located as a distinct active line touching the conjecture; the trace-formula side relevant here remains the Killip–Simon/Kupin sum-rule framework and Denisov's paths-space version.
6. **Multichannel/transfer-matrix criteria in multi-d**: no transfer-matrix L² criterion exists beyond d = 1 (transfer matrices are fundamentally 1D); the multi-d substitutes are the LNS eigenvalue-sum estimates and Denisov's Itô-diffusion formulation ([arXiv:1106.2155](https://arxiv.org/abs/1106.2155)).

Assessment: the field's center of gravity moved to (a) non-selfadjoint eigenvalue bounds, (b) discrete/tree models, (c) ballistic propagation — leaving the original conjecture untouched since the 2012–2013 survey wave.

---

## PART 5 — CONTROL THEORY SIDE (FOR THE INTERNAL REDUCTION)

Target property (as posed internally): ONE input-independent (open-loop, parameter-blind) control u(t) such that the induced propagator approximates a PRESCRIBED UNITARY on a family of eigenspaces, UNIFORMLY over a parameter continuum α ∈ 𝒟, in arbitrarily small time. Survey of what exists:

### 5.1 Chambrion–Pozzoli 2023 (small-time on manifolds; S² molecule)
T. Chambrion, E. Pozzoli, ["Small-time bilinear control of Schrödinger equations with application to rotating linear molecules"](https://arxiv.org/abs/2207.03818), *Automatica* **153** (2023) 111028. DOI:10.1016/j.automatica.2023.111028.
- Setting: i∂_t ψ = Δψ + u(t)·W(x)ψ on closed manifold M; focus S² with W₁ = x, W₂ = y (trigonometric interaction).
- Results: small-time reachability of {e^{iφ}ψ₀ : φ ∈ saturation space H_∞} (Theorem 6); for S² the saturation space (polynomials in x,y,z generated by brackets of Δ and W_j) is dense in L²(S²,R) ⟹ **small-time approximate controllability among particular eigenstates (spherical harmonics Y_j^m)** (Corollary 4).
- **What it does NOT give:** no single parameter-independent control achieving a prescribed *unitary matrix* on a finite eigenspace family; no uniformity-over-continuum statement; controls depend on target and initial state; time-smallness achieved via conjugated-trajectory composition, with error constants that blow up as t → 0 (no rate uniform in parameters).

### 5.2 Beauchard–Pozzoli 2025 (STAC on T^d and R^d; diffeomorphism method)
K. Beauchard, E. Pozzoli, ["Small-time approximate controllability of bilinear Schrödinger equations and diffeomorphisms"](https://arxiv.org/abs/2410.02383), *Ann. Inst. H. Poincaré C* (2025), DOI:10.4171/AIHPC/162.
- New method: STC of phases (reach e^{iφ}ψ₀ in small time) + STC of flows of vector fields (Lie bracket techniques) + simplicity of Diff⁰_c(M) (Thurston) + Moser transitivity ⟹ **global L² small-time approximate controllability (STAC)** on T^d and R^d. Does not need discrete spectrum.
- Companion: Beauchard–Pozzoli, "Examples of small-time controllable Schrödinger equations," *Ann. Henri Poincaré* (2025).
- **What it does NOT give:** approximate controllability ≠ unitary-operator simulation; no prescribed-unitary-on-eigenspace-family result; no uniform-over-parameter-continuum version (their parameter is the potential/drift, not an uncertainty continuum); no explicit input-independent control law for a target unitary.

### 5.3 Liang–Boscain–Sigalotti (ensemble, scalar control, n-level)
R. Liang, U. Boscain, M. Sigalotti, ["Ensemble control of n-level quantum systems with a scalar control"](https://arxiv.org/abs/2501.12357) (Jan 2025).
- Setting: continuum of n-level systems iψ̇ = (H(α) + ω(t)H_c(δ))ψ, α ∈ 𝒟 ⊂ R^m (dispersed gaps λ_j(α)), δ_{jk} in known intervals.
- Result (Thm 1 + Prop 4): chirped-pulse control ω_{ε1,ε2} (explicit, same for all α, δ) achieves population inversion e_p → e^{iθ}e_q **uniformly over the ensemble**, with error O(max(ε₂/ε₁, ε₁^{2}/ε₂)) etc., provided: (i) gap λ_q(α) − λ_p(α) stays inside a window (v₀,v₁); (ii) NO other transition frequency enters the closed window [v₀, v₁]; (iii) stronger 2-resonance exclusion for Prop 4's sharper rate. Cascade of inversions realizes longer chains.
- Mechanism: rotating-wave + adiabatic approximations in cascade; total time T/(ε₁ε₂) → ∞ as fidelity → 1.
- **What it does NOT give:** (a) only state-to-state (population inversion), not arbitrary unitary on a multi-dimensional eigenspace family; (b) NOT small-time — quite the opposite, control horizon diverges; (c) requires non-resonance windows — fails when eigengaps overlap the window (they demonstrate numerically that violating hypotheses destroys transfer). For a degenerate-multiplicity setting (our internal reduction involves eigenspaces of multiplicity ≥ 2 on S²), the RWA-based selection rules do not obviously separate channels within a degenerate eigenspace.

### 5.4 Phase-saturation theorem (Chambrion-lineage)
The "saturation" technique (from Boscain–Caponigro–Chambrion–Sigalotti, *Comm. Math. Phys.* 311 (2012) 423–455, "A weak spectral condition…" [DOI:10.1007/s00220-012-1441-z]) and its small-time descendants (Duca–Nersesyan 2023 torus nonlinear; Chambrion–Pozzoli 2023; Beauchard–Pozzoli 2025) gives: if the Lie-algebraic saturation space generated by {iH₀, iW_j} is dense, then phases e^{iφ}ψ₀ are reachable (in large time originally; small time in the newer papers). This is the closest thing to a "phase saturation theorem"; it controls PHASES of a fixed state, not conjugation action on subspaces.

### 5.5 Verdict for RQ5
**No published theorem supplies the missing step** (single parameter-blind input ⟹ prescribed unitary on finite eigenspace family, uniform over continuum, arbitrarily small time). The three pillars give, respectively: ensemble state-transfer under gap-window separation and long times (LBS), small-time global AC on specific manifolds without ensemble uniformity (BP), and small-time phase/saturation control (CP + lineage). Combining them is exactly the open gap our internal reduction would need to fill. Flagged risk: degenerate eigenspaces (multiplicity > 1, unavoidable on S²) are untreated in ALL ensemble-control papers found; LBS explicitly assume simple spectra (diagonal H(α)).

---

## PART 6 — SUSPICIOUS / UNREFEREED ITEMS FLAGGED

- Nothing claiming resolution of the conjecture was found anywhere (refereed or not), so there is no suspicious *resolution claim* to flag.
- mp_arc 06-159 (cone-restricted LNS method) is a preprint-era document hosted on legacy servers; verify final journal status before citing formally (results attributed there are consistent with peer-reviewed companions).
- The user-supplied belief "Killip–Visan settled d ≥ 4/5" should be treated as a citation hallucination risk — likely conflation with their NLS program (§2.3).
- arXiv:2501.12357 is a preprint (presented at IEEE CDC 2024 in a 3-level precursor [14]); Theorem 1's full generality may still be under journal review as of Aug 2026 — cite as "preprint, 2025".
- Beauchard–Pozzoli AIHPC 162 is "published online first" (EMS Press) — final volume assignment pending; HAL: hal-04719730.

---

## PART 7 — DIRECT ANSWERS TO (a)/(b)

**(a) Does any published result construct V in the weighted-L² class destroying AC on an energy interval in d ≥ 2?**
NO. Closest approaches and why they fall short:
| Construction | Class | Why insufficient |
|---|---|---|
| Wigner–von Neumann | ~ sin(2x)/x | weight ∫r^{2(1+ε)}·r^{−2}·r^{d−1}dr diverges ⟹ outside class |
| Ionescu–Jerison | L^q, q > (d+1)/2 | different scale; not implied-by nor implying weighted-L² |
| Frank–Simon 2017 | same as above, small norm | idem |
| Kiselev–Last–Simon / Naboko sparse oscillatory | pointwise o(1/x), engineered phases | 1D constructions; fail weight; no d ≥ 2 transplant |
| Taimanov–Tsarev / Naboko–Simonov 2D Moutard | ~1/|x| rational/oscillatory | outside class |
| Bögli–Cuenin 2023 | complex L^q ((d+1)/2, d] | complex-valued; Fermi-golden-rule obstruction to real case |

**(b) Does any published control-theorem supply the missing step?**
NO (see Part 5). Nearest neighbors: LBS 2025 (ensemble, state-transfer, non-small-time, gap-window condition), CP 2023 (small-time, S², eigenstate population moves, not unitary synthesis, not ensemble-uniform), BP 2025 (small-time global AC on T^d/R^d, not S², not ensemble, not unitary-targeted), BCCS 2012 weak spectral condition (large-time, saturation).

---

## PART 8 — CONSOLIDATED REFERENCE LIST

1. B. Simon, "Tosio Kato's work…Part 2," Bull. Math. Sci. 9 (2019) 1950008 — Conjecture 20.2. https://math.caltech.edu/SimonPapers/R62.pdf
2. S. A. Denisov, "Multidimensional L² conjecture: a survey," arXiv:1203.4255 (2012). https://arxiv.org/abs/1203.4255
3. S. A. Denisov, L. Nikolskii, tree-model resolution notes. https://people.math.wisc.edu/~denissov/nikolskii.pdf
4. P. Deift, R. Killip, CMP 203 (1999) 341–347. doi:10.1007/s002200050615
5. R. Killip, B. Simon, Ann. Math. 158 (2003) 253–321. doi:10.4007/annals.2003.158.253
6. B. Simon, Ann. Math. 170 (2009) 739–782. arXiv:math/0608767
7. A. Laptev, S. Naboko, O. Safronov, CMP 253 (2005) 611–631. doi:10.1007/s00220-004-1157-9
8. A. Laptev, S. Naboko, O. Safronov, JFA 219 (2005) 285–305. doi:10.1016/j.jfa.2004.06.009
9. O. Safronov, CMP 254 (2005) 361–366. doi:10.1007/s00220-004-1161-0
10. O. Safronov, arXiv:math/0408376 (2004); arXiv:1111.5552 (2012); Trans. AMS (2013) doi:10.1090/s1061-0022-2013-01275-1
11. G. Perelman, stability results (mid-2000s), cited per Denisov survey ref. list.
12. D. Ionescu, D. Jerison, "On the absence of positive eigenvalues of Schrödinger operators with potentials," GAFA 16 (2006) (example concentrated near hyperplanes).
13. H. Koch, D. Tataru, absence of embedded eigenvalues for V ∈ L^{(d+1)/2}. https://math.berkeley.edu/~tataru/papers/em4.pdf
14. R. Frank, B. Simon, J. Spectr. Theory 7 (2017) 633–658 (embedded eigenvalues with vanishing L^q norm, q>(d+1)/2).
15. S. Bögli, J.-C. Cuenin, CMP 398 (2023) 1349–1370. doi:10.1007/s00220-022-04546-z
16. I. Taimanov, S. Tsarev, Russ. Math. Surveys 62 (2007) 631–633; Naboko–Simonov-school 2D vN–W multiple-eigenvalue families: arXiv:1307.5141.
17. A. Kiselev, Y. Last, B. Simon, modified Prüfer/EFGP; Wigner–von Neumann type slowly decaying potentials: arXiv:1201.4840.
18. R. Frank, J. Sabin, restriction/orthonormal-Strichartz/uniform Sobolev: arXiv:1404.2817.
19. Ballistic transport discrete multi-d: arXiv:2507.04988 (2025).
20. Eigenvalue sums complex radial: arXiv:2408.15783 (2024); random complex decaying: APDE 18 (2025) 279. doi:10.2140/apde.2025.18.279
21. T. Chambrion, E. Pozzoli, Automatica 153 (2023) 111028. arXiv:2207.03818
22. K. Beauchard, E. Pozzoli, AIHPC (2025). arXiv:2410.02383; companion Ann. Henri Poincaré (2025).
23. R. Liang, U. Boscain, M. Sigalotti, arXiv:2501.12357 (2025).
24. U. Boscain, M. Caponigro, T. Chambrion, M. Sigalotti, CMP 311 (2012) 423–455. doi:10.1007/s00220-012-1441-z
25. C. Bär, W. Ballmann, first-order elliptic BVPs; boundary-triple spectral characterization infrastructure: e.g. Behrndt–Rohleder AIM (2015). doi:10.1016/j.aim.2015.08.016
26. R. Killip, M. Vişan (NLS corpus — NOT related to this conjecture): focusing energy-critical d≥5; mass-critical radial d≥3 (APDE 2008 1:229); Strichartz on tori (MRL 2016).

---

## APPENDIX: SEARCH TRAIL (reproducibility)

Queries run (WebSearch): "multidimensional L2 conjecture Schrödinger absolutely continuous spectrum status"; "Killip Visan multidimensional Schrödinger L2 conjecture dimensions"; "Frank Laptev Naboko Safronov absolutely continuous spectrum multidimensional oscillating potentials"; "embedded eigenvalues weak-L2 potential Schrödinger operator multidimensional counterexample"; "Kiselev Last Simon modified Wigner von Neumann potentials higher dimensions absolutely continuous spectrum"; "Frank Sabin absolutely continuous spectrum Schrödinger Lp potentials spectral theorem 2014"; "arXiv 2024 2025 multidimensional Schrödinger 'absolutely continuous spectrum' slowly decaying potentials breakthrough"; "'L2 conjecture' Simon Schrödinger solved disproved counterexample 2024 2025"; "Denisov multidimensional L2 conjecture 2023 2024 2025 new results Cayley tree"; "Chambrion Pozzoli bilinear Schrödinger equation controllability arXiv 2023"; "Beauchard Pozzoli small-time approximate controllability bilinear Schrödinger sphere arXiv"; "Chambrion Pozzoli saturating set phase control Schrödinger eigenfunctions saturation"; "Bär Ballmann Schrödinger operators boundary triples absolutely continuous spectrum multiplicity".
Fetches: arXiv abstract/full pages for 2501.12357, 2410.02383, 2207.03818, math/0408376, 1111.5552, 1203.4255 (survey), 1307.5141, 1201.4840, math/0509668, 1404.2817, 2507.04988, Laptev's schr2.pdf, mp_arc 06-159, Bögli–Cuenin (CMP/DNB), Koch–Tataru (Berkeley), Frank–Simon-context (JST 298), Killip publication page, arXiv math.SP recent listing (checked through 2026-08-25).
