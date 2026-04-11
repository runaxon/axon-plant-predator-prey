from myelin import Measurement

import numpy as np

class MyelinMeasurement(Measurement):
    def measure(self, state, params):
        true_x = state[0] / (state[0] + state[1])
        noise = -0.05 + 0.10 * np.random.uniform()  # +/- 5 percent
        observed_x = min(1.0, max(0, true_x + noise))
        return observed_x