"""Broadband phase-mask refocusing stress test on a periodic angular model.

This is deliberately a toy model, not evidence for the full S^2 converter.
It tests whether products of energy-scaled phase masks and free angular
Schrodinger propagators can refocus a constant input into a concentrated,
oscillatory target over more than one energy.

Manuscript diagnostic commands (seeded and deterministic on the recorded
SciPy runtime):

  py -3 phase_mask_circle_ensemble.py --grid 48 --ell 5 --masks 6 \
      --samples 5 --s-min 0.95 --s-max 1.05 --restarts 5 \
      --maxiter 5000 --seed 20260722

  py -3 phase_mask_circle_ensemble.py --grid 48 --ell 5 --masks 4 \
      --samples 5 --s-min 0.75 --s-max 1.25 --restarts 3 \
      --maxiter 500 --seed 20260722
"""

from __future__ import annotations

import argparse
import json

import numpy as np
from scipy.optimize import minimize


def target_state(n_grid: int, ell: int) -> np.ndarray:
    x = 2.0 * np.pi * np.arange(n_grid) / n_grid
    distance = np.angle(np.exp(1j * x))
    state = np.exp(-0.5 * ell * distance**2) * np.exp(1j * ell * x)
    return state / np.linalg.norm(state)


def free_step(state: np.ndarray, s: float, sigma: float, modes_sq: np.ndarray) -> np.ndarray:
    coeff = np.fft.fft(state, norm="ortho")
    coeff *= np.exp(-1j * s * sigma * modes_sq)
    return np.fft.ifft(coeff, norm="ortho")


def free_step_adjoint(
    state: np.ndarray, s: float, sigma: float, modes_sq: np.ndarray
) -> np.ndarray:
    coeff = np.fft.fft(state, norm="ortho")
    coeff *= np.exp(1j * s * sigma * modes_sq)
    return np.fft.ifft(coeff, norm="ortho")


def apply_generator(state: np.ndarray, modes_sq: np.ndarray) -> np.ndarray:
    coeff = np.fft.fft(state, norm="ortho")
    coeff *= modes_sq
    return np.fft.ifft(coeff, norm="ortho")


class EnsembleObjective:
    def __init__(
        self,
        n_grid: int,
        n_masks: int,
        ell: int,
        samples: np.ndarray,
    ) -> None:
        self.n_grid = n_grid
        self.n_masks = n_masks
        self.samples = samples
        self.input = np.ones(n_grid, dtype=np.complex128) / np.sqrt(n_grid)
        self.target = target_state(n_grid, ell)
        modes = np.fft.fftfreq(n_grid, d=1.0 / n_grid)
        self.modes_sq = modes**2

    def unpack(self, parameters: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        split = self.n_grid * self.n_masks
        masks = parameters[:split].reshape(self.n_masks, self.n_grid)
        sigmas = parameters[split:]
        return masks, sigmas

    def value_and_grad(self, parameters: np.ndarray) -> tuple[float, np.ndarray]:
        masks, sigmas = self.unpack(parameters)
        grad_masks = np.zeros_like(masks)
        grad_sigmas = np.zeros_like(sigmas)
        loss = 0.0

        for s in self.samples:
            after_masks: list[np.ndarray] = []
            after_frees: list[np.ndarray] = []
            state = self.input.copy()
            for j in range(self.n_masks):
                state = np.exp(-1j * s * masks[j]) * state
                after_masks.append(state.copy())
                if j < self.n_masks - 1:
                    state = free_step(state, s, sigmas[j], self.modes_sq)
                    after_frees.append(state.copy())

            overlap = np.vdot(self.target, state)
            loss += 1.0 - float(abs(overlap) ** 2)

            adjoint = self.target.copy()
            for j in range(self.n_masks - 1, -1, -1):
                mask_state = after_masks[j]
                local = np.conj(overlap) * np.conj(adjoint) * mask_state
                grad_masks[j] += -2.0 * s * np.imag(local)

                adjoint = np.exp(1j * s * masks[j]) * adjoint
                if j > 0:
                    free_state = after_frees[j - 1]
                    generator_state = apply_generator(free_state, self.modes_sq)
                    local_sigma = np.conj(overlap) * np.vdot(adjoint, generator_state)
                    grad_sigmas[j - 1] += -2.0 * s * np.imag(local_sigma)
                    adjoint = free_step_adjoint(
                        adjoint, s, sigmas[j - 1], self.modes_sq
                    )

        scale = 1.0 / len(self.samples)
        loss *= scale
        gradient = np.concatenate(
            [(grad_masks * scale).ravel(), grad_sigmas * scale]
        )
        return loss, gradient

    def fidelities(self, parameters: np.ndarray, samples: np.ndarray) -> list[float]:
        masks, sigmas = self.unpack(parameters)
        values: list[float] = []
        for s in samples:
            state = self.input.copy()
            for j in range(self.n_masks):
                state *= np.exp(-1j * s * masks[j])
                if j < self.n_masks - 1:
                    state = free_step(state, s, sigmas[j], self.modes_sq)
            values.append(float(abs(np.vdot(self.target, state)) ** 2))
        return values


def gradient_check(objective: EnsembleObjective, parameters: np.ndarray) -> float:
    value, gradient = objective.value_and_grad(parameters)
    rng = np.random.default_rng(90210)
    direction = rng.normal(size=parameters.size)
    direction /= np.linalg.norm(direction)
    step = 1.0e-6
    plus, _ = objective.value_and_grad(parameters + step * direction)
    minus, _ = objective.value_and_grad(parameters - step * direction)
    finite_difference = (plus - minus) / (2.0 * step)
    analytic = float(np.dot(gradient, direction))
    return abs(finite_difference - analytic) / max(
        1.0, abs(finite_difference), abs(analytic), abs(value)
    )


def optimize_case(
    n_grid: int,
    n_masks: int,
    ell: int,
    samples: np.ndarray,
    restarts: int,
    maxiter: int,
    seed: int,
) -> dict[str, object]:
    objective = EnsembleObjective(n_grid, n_masks, ell, samples)
    bounds = [(-np.pi, np.pi)] * (n_grid * n_masks)
    bounds += [(0.0, 0.5)] * (n_masks - 1)
    rng = np.random.default_rng(seed)
    best = None

    for restart in range(restarts):
        masks = 0.35 * rng.normal(size=(n_masks, n_grid))
        sigmas = rng.uniform(0.015, 0.12, size=n_masks - 1)
        initial = np.concatenate([masks.ravel(), sigmas])
        result = minimize(
            fun=lambda p: objective.value_and_grad(p),
            x0=initial,
            jac=True,
            method="L-BFGS-B",
            bounds=bounds,
            options={"maxiter": maxiter, "ftol": 1.0e-12, "gtol": 1.0e-8},
        )
        if best is None or result.fun < best.fun:
            best = result

    assert best is not None
    dense_samples = np.linspace(float(samples.min()), float(samples.max()), 41)
    train_fidelity = objective.fidelities(best.x, samples)
    dense_fidelity = objective.fidelities(best.x, dense_samples)
    return {
        "n_grid": n_grid,
        "n_masks": n_masks,
        "ell": ell,
        "training_samples": samples.tolist(),
        "success": bool(best.success),
        "iterations": int(best.nit),
        "objective": float(best.fun),
        "train_min_fidelity": float(min(train_fidelity)),
        "train_mean_fidelity": float(np.mean(train_fidelity)),
        "dense_min_fidelity": float(min(dense_fidelity)),
        "dense_mean_fidelity": float(np.mean(dense_fidelity)),
        "dense_max_fidelity": float(max(dense_fidelity)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid", type=int, default=48)
    parser.add_argument("--ell", type=int, default=5)
    parser.add_argument("--masks", type=int, nargs="+", default=[2, 4, 6])
    parser.add_argument("--samples", type=int, default=5)
    parser.add_argument("--s-min", type=float, default=0.75)
    parser.add_argument("--s-max", type=float, default=1.25)
    parser.add_argument("--restarts", type=int, default=3)
    parser.add_argument("--maxiter", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260722)
    parser.add_argument("--check-gradient", action="store_true")
    args = parser.parse_args()

    samples = np.linspace(args.s_min, args.s_max, args.samples)
    if args.check_gradient:
        objective = EnsembleObjective(args.grid, args.masks[0], args.ell, samples)
        rng = np.random.default_rng(args.seed)
        parameters = rng.normal(
            scale=0.1,
            size=args.grid * args.masks[0] + args.masks[0] - 1,
        )
        print(json.dumps({"gradient_relative_error": gradient_check(objective, parameters)}))

    results = [
        optimize_case(
            n_grid=args.grid,
            n_masks=n_masks,
            ell=args.ell,
            samples=samples,
            restarts=args.restarts,
            maxiter=args.maxiter,
            seed=args.seed + n_masks,
        )
        for n_masks in args.masks
    ]
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
