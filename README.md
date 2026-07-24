# Selected-channel entropy and reciprocal Riesz contraction

This repository contains two journal-style mathematical preprints by
Siam Siraji, together with their LaTeX sources, compiled PDFs, stage notes,
and diagnostic code developed during the project.

## Scientific status

The repository does **not** claim a proof or disproof of Simon's
multidimensional \(L^2\) conjecture.

- Paper I proves a negative result for a proposed proof strategy: the universal
  fixed-potential, fixed selected-channel entropy estimate fails.
- Paper II proves operator-valued contraction and obstruction results, then
  isolates an explicit short-angular-time radialization problem. The proposed
  counterexample to Simon's conjecture remains conditional on that problem.

This distinction is part of the mathematical result, not a presentational
qualification. Any public description of the work should preserve it.

## Papers

### Paper I

**Simon's Multidimensional \(L^2\) Conjecture and the Failure of
Fixed-Potential Selected-Channel Entropy: Plücker-Schur Reductions and a
Reciprocal Riesz-Talbot Construction**

- Source: `papers/paper-1-selected-channel-entropy/main.tex`
- Included construction:
  `papers/paper-1-selected-channel-entropy/fixed_potential_riesz_counterexample.tex`
- PDF: `papers/paper-1-selected-channel-entropy/siraji_selected_channel_entropy_failure.pdf`

Main conclusion: one bounded, real, mean-zero zonal \(X_3\) potential makes
the selected \(N=1\) entropy diverge along every cofinal positively smoothed,
radially truncated, double-buffered Galerkin diagonal. This closes the fixed
selected-channel completion route but leaves the spectral multiplicity of the
limiting operator undecided.

### Paper II

**Simon's Multidimensional \(L^2\) Conjecture: Operator-Valued Reciprocal
Riesz Contraction and the Radial Short-Time Problem**

- Source: `papers/paper-2-operator-valued-riesz/main.tex`
- PDF: `papers/paper-2-operator-valued-riesz/siraji_operator_valued_riesz_contraction.pdf`

Main conclusions: a one-cell dimension-free contraction is false; grouped
fixed-height contraction is valid for compact singular spectral-measure
families; several proposed physical realizations are ruled out; and the
remaining bridge to the full radial Schrödinger problem is stated as one
explicit open theorem.

Convenience copies of both PDFs are in `output/pdf/`.

## Repository layout

```text
archive/stage-notes/                 Earlier equation-level stage manuscripts
papers/paper-1-selected-channel-entropy/
papers/paper-2-operator-valued-riesz/
reproducibility/numerical/           Diagnostic numerical and Lie-algebra checks
reproducibility/research-notes/      Construction and synchronization notes
output/pdf/                          Final convenience copies
```

Downloaded literature is intentionally excluded. The bibliographies contain
links to the cited primary sources.

## Building the papers

The sources compile with Tectonic. From PowerShell:

```powershell
.\build.ps1
```

To build one paper:

```powershell
.\build.ps1 -Paper paper1
.\build.ps1 -Paper paper2
```

Paper I uses `enumitem`; a full TeX Live installation also works when that
package is installed. Paper II compiles with a standard LaTeX installation.

## Reproducibility

The scripts are diagnostics and finite-dimensional audits. They are not
substitutes for the analytic proofs. See `reproducibility/README.md` for the
role of each script and the tested Python environment.

## Before journal submission

The manuscripts are formatted as neutral mathematical preprints, not in a
publisher-specific class. Before submission:

1. obtain independent expert verification of every main proof;
2. decide whether the two long manuscripts should be shortened or split
   further for the target journal;
3. adapt the source to the journal class and reference style;
4. choose a repository and code license;
5. archive a fixed release and add its DOI to `CITATION.cff`.

See `RELEASE_CHECKLIST.md` for a concise release audit.

## Author

Siam Siraji
The University of Adelaide
siam.siraji@adelaide.edu.au
