# myelin_adapters.py
from myelin import Plant

class MyelinPredatorPreyPlant(Plant):
    """
    This code should look identical to what exists in the 'non-myelin' version
    of the plant.
    """
    state_size  = 2   # x, y
    input_size  = 1   # harvest rate u(t)
    params_size = 4   # alpha, beta, delta, gamma

    def derivatives(self, state, inputs, params):
        x, y = state
        u_t, = inputs
        alpha, beta, delta, gamma = params
        dx = alpha * x - beta * x * y - u_t
        dy = delta * x * y - gamma * y
        return (dx, dy)

    def observe(self, state, params):
        x, y = state
        return x