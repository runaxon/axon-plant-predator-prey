from myelin import Plant

from predator_prey import derivatives as _derivatives
from predator_prey import observe as _observe

class PredatorPreyPlant(Plant):
    """
    States: Predator size = X, Prey size = Y
    Input: Harvest rate
    Parameters: 
        - predator rate = alpha
        - predator growth rate from predation = beta
        - predator natural death rate = delta 
        - Prey natural growth rate = gamma
    """
    state_size = 2
    input_size = 1
    params_size = 4

    def derivatives(self, state, input, params):
        return _derivatives(state, input, params)
    
    def observe(self, state, params):
        return _observe(state, params)
