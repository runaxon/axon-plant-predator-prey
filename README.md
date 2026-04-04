# axon-plant-predator-prey

Reference implementation of a Myelin-compatible simulation model.

A Lotka-Volterra predator-prey system with PID harvesting control,
used as the demo model for the Myelin quickstart guide.

## The Model

```
dx/dt = alpha*x - beta*x*y - u    (prey: growth - predation - harvest)
dy/dt = delta*x*y - gamma*y       (predators: growth from predation - death)
```

A PID controller adjusts harvest rate `u` to maintain prey population at a target level.
The evaluator sweeps 512 PID gain combinations over 200 randomized initial conditions.

## Quickstart

```bash
pip install myelin
python main.py --target .
python .myelin/run_parallel.py
```

## Files

| File | Purpose |
|---|---|
| `predator_prey.py` | ODE — `derivatives()` and `observe()` |
| `controller/pid.py` | Discrete-time PID controller |
| `cohort.py` | Generate cohort of randomized scenarios |
| `simulation.py` | Pure Python reference simulation loop |
| `myelin_adapters.py` | The three Myelin adapter classes |
