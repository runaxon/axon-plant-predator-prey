"""
Generate a cohort of predator-prey scenarios.

Each scenario is a dict with:
  - initial conditions (x0, y0)
  - model parameters (alpha, beta, delta, gamma)

We vary initial conditions around a nominal point with small random perturbations
to simulate a diverse population of starting states.
"""

import random


# Nominal Lotka-Volterra parameters (classic textbook values)
NOMINAL_PARAMS = {
    'alpha': 0.6,   # prey growth rate
    'beta':  0.02,  # predation rate
    'delta': 0.01,  # predator growth from predation
    'gamma': 0.4,   # predator death rate
}

# Nominal initial conditions
NOMINAL_X0 = 40.0   # prey
NOMINAL_Y0 = 9.0    # predators

# Controller target — maintain prey at this level
PREY_TARGET = 40.0


def generate_cohort(n=200, seed=42):
    """
    Return a list of n scenario dicts with perturbed initial conditions
    and slightly varied parameters.
    """
    rng = random.Random(seed)
    cohort = []
    for _ in range(n):
        scenario = {
            'x0':    NOMINAL_X0 * (1.0 + rng.uniform(-0.2, 0.2)),
            'y0':    NOMINAL_Y0 * (1.0 + rng.uniform(-0.2, 0.2)),
            'alpha': NOMINAL_PARAMS['alpha'] * (1.0 + rng.uniform(-0.1, 0.1)),
            'beta':  NOMINAL_PARAMS['beta']  * (1.0 + rng.uniform(-0.1, 0.1)),
            'delta': NOMINAL_PARAMS['delta'] * (1.0 + rng.uniform(-0.1, 0.1)),
            'gamma': NOMINAL_PARAMS['gamma'] * (1.0 + rng.uniform(-0.1, 0.1)),
        }
        cohort.append(scenario)
    return cohort


def scenario_to_params(scenario):
    """Convert scenario dict to (state0, params) tuples Myelin expects."""
    state0 = (scenario['x0'], scenario['y0'])
    params = (
        scenario['alpha'],
        scenario['beta'],
        scenario['delta'],
        scenario['gamma'],
    )
    return state0, params
