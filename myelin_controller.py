from myelin import Controller
from controller.pid import PIDController

class MyelinController(Controller):
    def __init__(self, kp=1.0, ki=0.2, kd=0.4, setpoint=40.0, dt=0.05, 
                 max_rate=10.0, min_rate=0.0):
        self._pid = PIDController(
            kp=kp,
            ki=ki,
            kd=kd,
            setpoint=setpoint,
            dt=dt,
            max_rate=max_rate,
            min_rate=min_rate
        )
    
    def step(self, measurement):
        return self._pid.step(measurement)
    
    def reset(self):
        self._pid.reset()