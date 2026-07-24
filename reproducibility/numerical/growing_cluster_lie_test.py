"""Finite Lie-closure checks for consecutive spherical-harmonic shell clusters.

For a specification ``ell:A``, the script compresses multiplication by all
real degree-(2*ell+1) profiles to

    H_ell + H_{ell+1} + ... + H_A

and reports the dimensions of the control-only and drift-plus-control Lie
algebras.  These checks are evidence only; the LaTeX note does not promote the
observed general pattern to a theorem.
"""

from __future__ import annotations

import math
import sys

import numpy as np

from resonant_shell_lie_test import gaunt_coefficient


def real_vector(matrix: np.ndarray) -> np.ndarray:
    return np.concatenate((matrix.real.ravel(), matrix.imag.ravel()))


def lie_dimension_fast(
    generators: list[np.ndarray], tolerance: float = 2e-9
) -> int:
    """Close under adjoint actions of the original generators."""

    basis: list[np.ndarray] = []
    orthonormal: list[np.ndarray] = []

    def add(candidate: np.ndarray) -> None:
        vector = real_vector(candidate)
        for unit in orthonormal:
            vector -= np.dot(unit, vector) * unit
        norm = np.linalg.norm(vector)
        if norm > tolerance:
            orthonormal.append(vector / norm)
            basis.append(candidate)

    for generator in generators:
        add(generator)

    cursor = 0
    while cursor < len(basis):
        current = basis[cursor]
        for generator in generators:
            add(generator @ current - current @ generator)
        cursor += 1
    return len(basis)


def shell_basis(ell: int, top: int) -> list[tuple[int, int]]:
    return [
        (degree, magnetic)
        for degree in range(ell, top + 1)
        for magnetic in range(-degree, degree + 1)
    ]


def complex_profile_control(
    ell: int, top: int, profile_index: int
) -> np.ndarray:
    profile_degree = 2 * ell + 1
    basis = shell_basis(ell, top)
    matrix = np.zeros((len(basis), len(basis)), dtype=complex)
    for row, (upper_degree, upper_magnetic) in enumerate(basis):
        for column, (lower_degree, lower_magnetic) in enumerate(basis):
            if -upper_magnetic + profile_index + lower_magnetic != 0:
                continue
            matrix[row, column] = (
                (-1) ** upper_magnetic
                * gaunt_coefficient(
                    upper_degree,
                    profile_degree,
                    lower_degree,
                    -upper_magnetic,
                    profile_index,
                    lower_magnetic,
                )
            )
    return matrix


def real_profile_controls(ell: int, top: int) -> list[np.ndarray]:
    profile_degree = 2 * ell + 1
    complex_controls = {
        index: complex_profile_control(ell, top, index)
        for index in range(-profile_degree, profile_degree + 1)
    }
    controls = [complex_controls[0]]
    for index in range(1, profile_degree + 1):
        controls.append(
            (
                complex_controls[index]
                + ((-1) ** index) * complex_controls[-index]
            )
            / math.sqrt(2)
        )
        controls.append(
            (
                complex_controls[index]
                - ((-1) ** index) * complex_controls[-index]
            )
            / (1j * math.sqrt(2))
        )
    return controls


def check_cluster(ell: int, top: int) -> None:
    basis = shell_basis(ell, top)
    dimension = len(basis)
    eigenvalues = np.array(
        [degree * (degree + 1) for degree, _ in basis], dtype=float
    )
    drift = np.diag(eigenvalues - eigenvalues.mean())
    controls = real_profile_controls(ell, top)

    control_dimension = lie_dimension_fast(
        [1j * control for control in controls]
    )
    full_dimension = lie_dimension_fast(
        [1j * drift] + [1j * control for control in controls]
    )
    print(
        f"ell={ell} top={top} N={dimension} "
        f"control={control_dimension}/{dimension * (dimension - 1) // 2} "
        f"full={full_dimension}/{dimension**2 - 1}"
    )


if __name__ == "__main__":
    specifications = sys.argv[1:] or ["0:2", "1:3", "2:4"]
    for specification in specifications:
        lower_text, upper_text = specification.split(":", maxsplit=1)
        check_cluster(int(lower_text), int(upper_text))
