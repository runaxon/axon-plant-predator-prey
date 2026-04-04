"""
Pure Python simulation loop — the reference implementation.
Myelin validates its C kernel against this output.
"""

from predator_prey import derivatives, observe


def rk4_step(state, inputs, params, dt):
    s = state
    k1 = derivatives(s, inputs, params)
    k2 = derivatives(
        tuple(s[i] + 0.5*dt*k1[i] for i in range(len(s))),
        inputs, params
    )
    k3 = derivatives(
        tuple(s[i] + 0.5*dt*k2[i] for i in range(len(s))),
        inputs, params
    )
    k4 = derivatives(
        tuple(s[i] + dt*k3[i] for i in range(len(s))),
        inputs, params
    )
    return tuple(
        s[i] + (dt/6.0) * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i])
        for i in range(len(s))
    )


def run_simulation(
    state0,
    params,
    kp,
    ki,
    kd,
    duration=50.0,
    dt=0.05,
    t_start=5.0,
    t_end=45.0,
    target=40.0
):
    """
    Run closed-loop simulation. Returns scalar ISE loss.

    t_start / t_end define the window over which ISE is accumulated
    (ignore transient startup).
    """
    from controller.pid import PIDController

    controller = PIDController(kp=kp, ki=ki, kd=kd,
                               setpoint=target, dt=dt,
                               max_rate=10.0, min_rate=0.0)
    state = state0
    t = 0.0
    ise = 0.0
    ise_ref = target ** 2 * (t_end - t_start)
    n_steps = int(round(duration / dt))

    for _ in range(n_steps):
        measurement = observe(state, params)
        u = controller.step(measurement)

        if t_start <= t <= t_end:
            err = measurement - target
            ise += err * err * dt

        state = rk4_step(state, (u,), params, dt)
        t += dt

    return ise / ise_ref
