"""
Discrete-time PID controller.
"""

class PIDController:
    def __init__(self, kp, ki, kd, setpoint, dt, max_rate=10.0, min_rate=0.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.dt = dt
        self.max_rate = max_rate
        self.min_rate = min_rate
        self._integral = 0.0
        self._prev = None

    def step(self, measurement):
        error = measurement - self.setpoint
        p = self.kp * error
        d = 0.0 if self._prev is None else self.kd * (measurement - self._prev) / self.dt
        i_out = self.ki * self._integral
        output = p + i_out + d
        saturated = output >= self.max_rate or output <= self.min_rate
        if not saturated:
            self._integral += error * self.dt
        self._prev = measurement
        return max(self.min_rate, min(self.max_rate, output))

    def reset(self):
        self._integral = 0.0
        self._prev = None
