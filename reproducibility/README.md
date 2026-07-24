# Reproducibility and diagnostic code

The scripts in `numerical/` are finite-dimensional diagnostics. They support
auditing and falsification, but they are not used as substitutes for analytic
proofs.

Tested environment:

- Python 3.13.14
- NumPy 2.4.4
- SciPy 1.17.1

Install the recorded dependencies with:

```powershell
py -3 -m pip install -r requirements.txt
```

## Paper I diagnostics

- `finite_cutoff_scalar_lift.py`: rank and conditioning audit for the
  cutoff-edge scalar two-state lift.
- `barrier_composite_sphere.py`: full-modal stress test for a
  barrier-assisted composite converter.
- `reciprocal_tensor_cascade.py`: finite tensor model for reciprocal barrier
  cascades.

## Paper II diagnostics

- `lens_inverse_circle_gate.py`: periodic-model stress test for a
  lens-assisted inverse gate.
- `phase_mask_circle_ensemble.py`: broadband phase-mask refocusing stress
  test.
- `resonant_shell_lie_test.py`: Lie-closure computations for resonant
  spherical-harmonic shell pairs.
- `growing_cluster_lie_test.py`: finite checks for growing consecutive-shell
  clusters.
- `nonadjacent_saturated_lie_test.py`: audits for saturated nonadjacent
  resonances.
- `maximal_tensor_isometry_search.py`: numerical search in the maximal tensor
  coupling model.

The Markdown files in `research-notes/` record the reciprocal synchronization,
Riesz-Talbot realization, and uniform lacunary diagonal arguments.
