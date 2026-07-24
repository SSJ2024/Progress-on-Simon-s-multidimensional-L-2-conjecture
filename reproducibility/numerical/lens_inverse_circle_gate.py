"""Finite periodic-model stress test for the lens-assisted inverse gate.

This is a deterministic diagnostic, not a proof for the sphere.  It asks
whether alternating scalar phase masks and positive free flights can
approximate the inverse free propagator, modulo one scalar phase, on a
selected low Fourier block uniformly over a compact detuning interval.

The loss is the phase-insensitive entanglement infidelity

    1 - |tr(T_s^* P_E W_s P_E)|^2 / d^2.

Because the propagated columns have total Frobenius norm sqrt(d), leakage
outside the selected block is penalized automatically.
"""

from __future__ import annotations

import argparse
import json

import numpy as np
from scipy.optimize import minimize


def free_step(
    states: np.ndarray,
    s: float,
    flight: float,
    modes_sq: np.ndarray,
) -> np.ndarray:
    coeff = np.fft.fft(states, axis=0, norm="ortho")
    coeff *= np.exp(-1j * s * flight * modes_sq)[:, None]
    return np.fft.ifft(coeff, axis=0, norm="ortho")


def free_step_adjoint(
    states: np.ndarray,
    s: float,
    flight: float,
    modes_sq: np.ndarray,
) -> np.ndarray:
    coeff = np.fft.fft(states, axis=0, norm="ortho")
    coeff *= np.exp(1j * s * flight * modes_sq)[:, None]
    return np.fft.ifft(coeff, axis=0, norm="ortho")


def apply_generator(states: np.ndarray, modes_sq: np.ndarray) -> np.ndarray:
    coeff = np.fft.fft(states, axis=0, norm="ortho")
    coeff *= modes_sq[:, None]
    return np.fft.ifft(coeff, axis=0, norm="ortho")


class GateObjective:
    def __init__(
        self,
        n_grid: int,
        n_cells: int,
        selected_modes: list[int],
        samples: np.ndarray,
        tau: float,
        target_kind: str,
    ) -> None:
        self.n_grid = n_grid
        self.n_cells = n_cells
        self.samples = samples
        self.tau = tau
        self.target_kind = target_kind
        modes = np.fft.fftfreq(n_grid, d=1.0 / n_grid)
        self.modes_sq = modes**2
        self.selected_modes = np.asarray(selected_modes, dtype=int)
        self.selected_eigenvalues = self.selected_modes.astype(float) ** 2
        x = np.arange(n_grid)
        self.input = np.exp(
            2j * np.pi * x[:, None] * self.selected_modes[None, :] / n_grid
        ) / np.sqrt(n_grid)
        self.dimension = len(selected_modes)

    def unpack(self, parameters: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        split = self.n_grid * self.n_cells
        masks = parameters[:split].reshape(self.n_cells, self.n_grid)
        flights = parameters[split:]
        return masks, flights

    def target(self, s: float) -> np.ndarray:
        if self.target_kind == "swap":
            if self.dimension != 2:
                raise ValueError("the swap target requires exactly two selected modes")
            return self.input[:, ::-1]
        return self.input * np.exp(
            1j * s * self.tau * self.selected_eigenvalues
        )[None, :]

    def value_and_grad(self, parameters: np.ndarray) -> tuple[float, np.ndarray]:
        masks, flights = self.unpack(parameters)
        grad_masks = np.zeros_like(masks)
        grad_flights = np.zeros_like(flights)
        loss = 0.0
        d2 = float(self.dimension**2)

        for s in self.samples:
            after_masks: list[np.ndarray] = []
            after_flights: list[np.ndarray] = []
            states = self.input.copy()
            for j in range(self.n_cells):
                states = np.exp(-1j * s * masks[j])[:, None] * states
                after_masks.append(states.copy())
                states = free_step(states, s, flights[j], self.modes_sq)
                after_flights.append(states.copy())

            target = self.target(float(s))
            overlap = np.vdot(target, states)
            loss += 1.0 - float(abs(overlap) ** 2) / d2

            adjoint = target.copy()
            for j in range(self.n_cells - 1, -1, -1):
                free_state = after_flights[j]
                generator_state = apply_generator(free_state, self.modes_sq)
                local_flight = np.vdot(adjoint, generator_state)
                grad_flights[j] += (
                    -2.0
                    * s
                    * np.imag(np.conj(overlap) * local_flight)
                    / d2
                )
                adjoint = free_step_adjoint(
                    adjoint, s, flights[j], self.modes_sq
                )

                mask_state = after_masks[j]
                local_mask = np.sum(np.conj(adjoint) * mask_state, axis=1)
                grad_masks[j] += (
                    -2.0
                    * s
                    * np.imag(np.conj(overlap) * local_mask)
                    / d2
                )
                adjoint = np.exp(1j * s * masks[j])[:, None] * adjoint

        scale = 1.0 / len(self.samples)
        gradient = np.concatenate(
            [(grad_masks * scale).ravel(), grad_flights * scale]
        )
        return loss * scale, gradient

    def metrics(
        self,
        parameters: np.ndarray,
        samples: np.ndarray,
    ) -> dict[str, float]:
        masks, flights = self.unpack(parameters)
        fidelities: list[float] = []
        errors: list[float] = []
        for s in samples:
            states = self.input.copy()
            for j in range(self.n_cells):
                states *= np.exp(-1j * s * masks[j])[:, None]
                states = free_step(states, s, flights[j], self.modes_sq)
            target = self.target(float(s))
            overlap = np.vdot(target, states)
            phase = overlap / abs(overlap) if abs(overlap) else 1.0
            fidelities.append(
                float(abs(overlap) ** 2 / self.dimension**2)
            )
            errors.append(
                float(np.linalg.norm(states - phase * target, ord=2))
            )
        return {
            "min_gate_fidelity": float(min(fidelities)),
            "mean_gate_fidelity": float(np.mean(fidelities)),
            "max_operator_error": float(max(errors)),
            "mean_operator_error": float(np.mean(errors)),
        }


def gradient_check(objective: GateObjective, parameters: np.ndarray) -> float:
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
    n_cells: int,
    selected_modes: list[int],
    samples: np.ndarray,
    tau: float,
    target_kind: str,
    restarts: int,
    maxiter: int,
    seed: int,
    mask_scale: float,
) -> dict[str, object]:
    objective = GateObjective(
        n_grid=n_grid,
        n_cells=n_cells,
        selected_modes=selected_modes,
        samples=samples,
        tau=tau,
        target_kind=target_kind,
    )
    bounds = [(-np.pi, np.pi)] * (n_grid * n_cells)
    bounds += [(0.0, 1.0)] * n_cells
    rng = np.random.default_rng(seed)
    best = None

    for _ in range(restarts):
        masks = mask_scale * rng.normal(size=(n_cells, n_grid))
        flights = rng.uniform(0.05, 0.95, size=n_cells)
        initial = np.concatenate([masks.ravel(), flights])
        result = minimize(
            fun=lambda p: objective.value_and_grad(p),
            x0=initial,
            jac=True,
            method="L-BFGS-B",
            bounds=bounds,
            options={"maxiter": maxiter, "ftol": 1.0e-13, "gtol": 1.0e-9},
        )
        if best is None or result.fun < best.fun:
            best = result

    assert best is not None
    dense_samples = np.linspace(float(samples.min()), float(samples.max()), 81)
    return {
        "n_grid": n_grid,
        "n_cells": n_cells,
        "selected_modes": selected_modes,
        "target_kind": target_kind,
        "training_samples": samples.tolist(),
        "success": bool(best.success),
        "iterations": int(best.nit),
        "objective": float(best.fun),
        "train": objective.metrics(best.x, samples),
        "dense": objective.metrics(best.x, dense_samples),
        "max_mask": float(np.max(np.abs(best.x[: n_grid * n_cells]))),
        "total_flight": float(np.sum(best.x[n_grid * n_cells :])),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid", type=int, default=24)
    parser.add_argument("--cells", type=int, nargs="+", default=[2, 4, 6])
    parser.add_argument("--modes", type=int, nargs="+", default=[0, 1])
    parser.add_argument("--samples", type=int, default=7)
    parser.add_argument("--s-min", type=float, default=0.75)
    parser.add_argument("--s-max", type=float, default=1.25)
    parser.add_argument("--tau", type=float, default=0.25)
    parser.add_argument("--target", choices=["inverse", "swap"], default="inverse")
    parser.add_argument("--restarts", type=int, default=3)
    parser.add_argument("--maxiter", type=int, default=1500)
    parser.add_argument("--seed", type=int, default=20260723)
    parser.add_argument("--mask-scale", type=float, default=1.25)
    parser.add_argument("--check-gradient", action="store_true")
    args = parser.parse_args()

    samples = np.linspace(args.s_min, args.s_max, args.samples)
    if args.check_gradient:
        objective = GateObjective(
            args.grid,
            args.cells[0],
            args.modes,
            samples,
            args.tau,
            args.target,
        )
        rng = np.random.default_rng(args.seed)
        parameters = rng.normal(
            scale=0.1,
            size=args.grid * args.cells[0] + args.cells[0],
        )
        print(
            json.dumps(
                {"gradient_relative_error": gradient_check(objective, parameters)}
            )
        )

    results = [
        optimize_case(
            n_grid=args.grid,
            n_cells=n_cells,
            selected_modes=args.modes,
            samples=samples,
            tau=args.tau,
            target_kind=args.target,
            restarts=args.restarts,
            maxiter=args.maxiter,
            seed=args.seed + n_cells,
            mask_scale=args.mask_scale,
        )
        for n_cells in args.cells
    ]
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
