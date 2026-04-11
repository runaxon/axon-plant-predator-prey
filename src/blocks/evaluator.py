from myelin import Evaluator

import numpy as np

class MyEval(Evaluator):
    
    def score(self, measurements, scenario):
        MSE = np.average(np.pow(np.array(measurements) - scenario['target'], 2))
        return MSE
    
    def aggregate(self, losses):
        return np.average(losses)