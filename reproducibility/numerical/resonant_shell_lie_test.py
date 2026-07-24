import math
import sys

import numpy as np


def factorial(value: int) -> int:
    return math.factorial(value) if value >= 0 else 0


def wigner_3j(
    j1: int, j2: int, j3: int, m1: int, m2: int, m3: int
) -> float:
    if m1 + m2 + m3 != 0:
        return 0.0
    if any(abs(m) > j for j, m in ((j1, m1), (j2, m2), (j3, m3))):
        return 0.0
    if j3 < abs(j1 - j2) or j3 > j1 + j2:
        return 0.0

    triangle = (
        factorial(j1 + j2 - j3)
        * factorial(j1 - j2 + j3)
        * factorial(-j1 + j2 + j3)
        / factorial(j1 + j2 + j3 + 1)
    )
    magnetic = math.prod(
        factorial(j + m) * factorial(j - m)
        for j, m in ((j1, m1), (j2, m2), (j3, m3))
    )
    prefactor = ((-1) ** (j1 - j2 - m3)) * math.sqrt(triangle * magnetic)

    lower = max(0, j2 - j3 - m1, j1 + m2 - j3)
    upper = min(j1 + j2 - j3, j1 - m1, j2 + m2)
    total = 0.0
    for z in range(lower, upper + 1):
        denominator = (
            factorial(z)
            * factorial(j1 + j2 - j3 - z)
            * factorial(j1 - m1 - z)
            * factorial(j2 + m2 - z)
            * factorial(j3 - j2 + m1 + z)
            * factorial(j3 - j1 - m2 + z)
        )
        total += ((-1) ** z) / denominator
    return prefactor * total


def gaunt_coefficient(
    j1: int, j2: int, j3: int, m1: int, m2: int, m3: int
) -> float:
    return (
        math.sqrt((2 * j1 + 1) * (2 * j2 + 1) * (2 * j3 + 1) / (4 * math.pi))
        * wigner_3j(j1, j2, j3, 0, 0, 0)
        * wigner_3j(j1, j2, j3, m1, m2, m3)
    )


def triangle_delta(j1: int, j2: int, j3: int) -> float:
    if j3 < abs(j1 - j2) or j3 > j1 + j2:
        return 0.0
    return math.sqrt(
        factorial(j1 + j2 - j3)
        * factorial(j1 - j2 + j3)
        * factorial(-j1 + j2 + j3)
        / factorial(j1 + j2 + j3 + 1)
    )


def wigner_6j(a: int, b: int, c: int, d: int, e: int, f: int) -> float:
    prefactor = (
        triangle_delta(a, b, c)
        * triangle_delta(a, e, f)
        * triangle_delta(d, b, f)
        * triangle_delta(d, e, c)
    )
    if prefactor == 0:
        return 0.0
    lower = max(a + b + c, a + e + f, d + b + f, d + e + c)
    upper = min(a + b + d + e, a + c + d + f, b + c + e + f)
    total = 0.0
    for z in range(lower, upper + 1):
        denominator = (
            factorial(z - a - b - c)
            * factorial(z - a - e - f)
            * factorial(z - d - b - f)
            * factorial(z - d - e - c)
            * factorial(a + b + d + e - z)
            * factorial(a + c + d + f - z)
            * factorial(b + c + e + f - z)
        )
        total += ((-1) ** z) * factorial(z + 1) / denominator
    return prefactor * total


def complex_profile_coupling(ell: int, n_harmonic: int) -> np.ndarray:
    """Matrix <L,M|Y_{J,N}|ell,m>, with L=ell+1 and J=2ell+1."""
    upper = ell + 1
    degree = 2 * ell + 1
    matrix = np.zeros((2 * upper + 1, 2 * ell + 1), dtype=complex)
    for upper_m in range(-upper, upper + 1):
        for lower_m in range(-ell, ell + 1):
            # conj(Y_{L,M}) = (-1)^M Y_{L,-M}
            if -upper_m + n_harmonic + lower_m != 0:
                continue
            value = ((-1) ** upper_m) * gaunt_coefficient(
                upper,
                degree,
                ell,
                -upper_m,
                n_harmonic,
                lower_m,
            )
            matrix[upper_m + upper, lower_m + ell] = complex(value)
    return matrix


def hermitian_from_coupling(coupling: np.ndarray) -> np.ndarray:
    upper_dim, lower_dim = coupling.shape
    result = np.zeros((lower_dim + upper_dim, lower_dim + upper_dim), dtype=complex)
    result[lower_dim:, :lower_dim] = coupling
    result[:lower_dim, lower_dim:] = coupling.conj().T
    return result


def real_profile_controls(ell: int) -> list[np.ndarray]:
    degree = 2 * ell + 1
    complex_couplings = {
        n: complex_profile_coupling(ell, n) for n in range(-degree, degree + 1)
    }
    controls = [hermitian_from_coupling(complex_couplings[0])]
    for n in range(1, degree + 1):
        cosine = (complex_couplings[n] + ((-1) ** n) * complex_couplings[-n]) / math.sqrt(2)
        sine = (complex_couplings[n] - ((-1) ** n) * complex_couplings[-n]) / (
            1j * math.sqrt(2)
        )
        controls.append(hermitian_from_coupling(cosine))
        controls.append(hermitian_from_coupling(sine))
    return controls


def real_vector(matrix: np.ndarray) -> np.ndarray:
    return np.concatenate((matrix.real.ravel(), matrix.imag.ravel()))


def lie_dimension(generators: list[np.ndarray], tolerance: float = 1e-10) -> int:
    basis: list[np.ndarray] = []
    orthonormal: list[np.ndarray] = []

    def add(candidate: np.ndarray) -> bool:
        vector = real_vector(candidate)
        for unit in orthonormal:
            vector -= np.dot(unit, vector) * unit
        norm = np.linalg.norm(vector)
        if norm <= tolerance:
            return False
        orthonormal.append(vector / norm)
        basis.append(candidate)
        return True

    for generator in generators:
        add(generator)

    cursor = 0
    while cursor < len(basis):
        left = basis[cursor]
        current = list(basis)
        for right in current:
            add(left @ right - right @ left)
        cursor += 1
    return len(basis)


if __name__ == "__main__":
    for ell_text in sys.argv[1:] or ["0", "1", "2", "3"]:
        ell = int(ell_text)
        lower_dim = 2 * ell + 1
        upper_dim = 2 * ell + 3
        total_dim = lower_dim + upper_dim
        detuning = np.diag(
            np.array(
                [-upper_dim / total_dim] * lower_dim
                + [lower_dim / total_dim] * upper_dim
            )
        )
        controls = real_profile_controls(ell)
        generators = [1j * detuning] + [1j * control for control in controls]
        dimension = lie_dimension(generators)
        control_dimension = lie_dimension([1j * control for control in controls])
        print(
            f"ell={ell} dim={total_dim} controls={len(controls)} "
            f"Lie-dim={dimension} control-only={control_dimension} "
            f"su={total_dim**2 - 1} u={total_dim**2}"
        )
