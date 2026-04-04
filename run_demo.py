"""
Quick demo — run a single closed-loop simulation and plot the result.
Verifies the ODE and PID are behaving before handing off to Myelin.

Usage:
    python run_demo.py
"""

import matplotlib.pyplot as plt

from predator_prey import observe
from simulation import rk4_step, run_simulation
from controller.pid import PIDController
from cohort import generate_cohort, scenario_to_params, PREY_TARGET

# --- simulation settings ---
DT = 0.05
DURATION = 50.0
KP, KI, KD = 1.0, 0.1, 0.1

# --- single scenario ---
cohort = generate_cohort(n=1, seed=42)
state0, params = scenario_to_params(cohort[0])

loss = run_simulation(state0, params, kp=KP, ki=KI, kd=KD)
print(f'loss: {loss:.6f}')

# --- run trajectory ---
controller = PIDController(kp=KP, ki=KI, kd=KD,
                           setpoint=PREY_TARGET, dt=DT,
                           max_rate=10.0, min_rate=0.0)
state = state0
t = 0.0
n_steps = int(round(DURATION / DT))

times, prey, predators, harvest = [], [], [], []

for _ in range(n_steps):
    x = observe(state, params)
    u = controller.step(x)
    times.append(t)
    prey.append(state[0])
    predators.append(state[1])
    harvest.append(u)
    state = rk4_step(state, (u,), params, DT)
    t += DT

# --- plot ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle('Predator-Prey: PID Harvest Control', fontsize=13)

ax1.plot(times, prey,      label='Prey',      color='#57c4b8', linewidth=1.8)
ax1.plot(times, predators, label='Predators', color='#d3869b', linewidth=1.8)
ax1.axhline(PREY_TARGET, color='white', linestyle='--', linewidth=1, alpha=0.5, label=f'Target ({PREY_TARGET})')
ax1.set_ylabel('Population')
ax1.legend(loc='upper right', fontsize=9)
ax1.set_facecolor('#1e1e1e')
ax1.tick_params(colors='#aaa')

ax2.plot(times, harvest, color='#e6b450', linewidth=1.5, label='Harvest rate')
ax2.set_ylabel('Harvest rate (u)')
ax2.set_xlabel('Time')
ax2.legend(loc='upper right', fontsize=9)
ax2.set_facecolor('#1e1e1e')
ax2.tick_params(colors='#aaa')

fig.patch.set_facecolor('#141414')
for ax in (ax1, ax2):
    for spine in ax.spines.values():
        spine.set_edgecolor('#444')
    ax.yaxis.label.set_color('#aaa')
    ax.xaxis.label.set_color('#aaa')

plt.tight_layout()
plt.show()
