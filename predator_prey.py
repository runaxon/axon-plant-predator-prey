"""
Lotka-Volterra predator-prey model with harvesting.

State:
  x — prey population   (e.g. rabbits, normalized)
  y — predator population (e.g. foxes, normalized)

Parameters:
  alpha  — prey natural growth rate
  beta   — predation rate
  delta  — predator growth rate from predation
  gamma  — predator natural death rate

Input:
  u — harvest rate applied to prey (the control input)

ODE:
  dx/dt = alpha*x - beta*x*y - u
  dy/dt = delta*x*y - gamma*y
"""


def derivatives(state, inputs, params):
    """
    Pure arithmetic. No imports, no function calls.
    This is the function Myelin will translate to C.
    """
    x, y = state
    u_t, = inputs
    alpha, beta, delta, gamma = params

    dx = alpha * x - beta * x * y - u_t
    dy = delta * x * y - gamma * y

    return (dx, dy)


def observe(state, params):
    """
    Scalar measurement the controller sees — prey population.
    """
    x, y = state
    return x
