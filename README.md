# axon-plant-predator-prey

Reference implementation of a Myelin simulation project. Demonstrates the full workflow — blocks, loaders, scenarios, cohorts, and jobs — using a Lotka-Volterra predator-prey system as the model.

## The Model

A two-state ODE with prey `x` and predator `y`. A PID controller adjusts harvest rate `u` to maintain the prey-to-total ratio at a target value.

```
dx/dt = alpha*x - beta*x*y - u    (prey: growth - predation - harvest)
dy/dt = delta*x*y - gamma*y       (predators: growth from predation - death)
```

Textbook parameters (`alpha=0.1, beta=0.02, delta=0.01, gamma=0.1`) give a natural equilibrium at `x=10, y=5`, ratio `≈ 0.667`.

## Project Structure

```
axon-plant-predator-prey/
  src/
    blocks/
      plant.py          ← Lotka-Volterra ODE
      measurement.py    ← prey ratio sensor (± 5% noise)
      controller.py     ← PID controller wrapping pid.py
      evaluator.py      ← MSE loss over measurement vector
    loaders/
      scenario_loader.py   ← loads dt, duration, state0 from scenarios/
      patient_loader.py    ← loads alpha, beta, delta, gamma from cohorts/
  cohorts/
    lion-gazelle/
      1.json            ← textbook Lotka-Volterra parameters
  scenarios/
    100_time_units.json ← dt=0.1, duration=100, state0=[10, 5]
  jobs/
    job.json            ← sweep kp/ki/kd, fixed setpoint and limits
```

## Quickstart

Install Myelin into your venv:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install setuptools
pip install -e ../myelin-engine
pip install anthropic python-dotenv
```

Compile all blocks:

```bash
python ../myelin-engine/main.py --target . --adapter plant
python ../myelin-engine/main.py --target . --adapter measurement
python ../myelin-engine/main.py --target . --adapter controller
python ../myelin-engine/main.py --target . --adapter evaluator
python ../myelin-engine/main.py --target . --adapter scenario_loader
python ../myelin-engine/main.py --target . --adapter patient_loader
python ../myelin-engine/main.py --target . --adapter simulator
```

Find the best PID gains over the lion-gazelle cohort:

```bash
python ../myelin-engine/main.py --target . --optimize jobs/job.json
```

Run the best params and save traces:

```bash
python ../myelin-engine/main.py --target . --run jobs/job.json --save-traces traces/
```

Debug with specific params:

```bash
python ../myelin-engine/main.py --target . --run jobs/job.json \
  --params '{"kp": 0.0, "ki": 0.22, "kd": 0.0}' --save-traces traces/
```

Each trace is a CSV with `measurement` and `action` columns — one row per timestep.

## Check build status

```bash
python ../myelin-engine/main.py --target . --status
```
