# Physical Consistency Audit (PCA)

This repository provides a reproducible benchmark for auditing
physical consistency in robotics simulation platforms.


🚨 **Critical Diagnostic Result: What if your PCA score is low?**

If your audit shows a **Hamiltonian Drift > 10%** or a **Physical Consistency Score < 60**, your simulation is currently in **"Physical Default."** > AI models trained on this data are inheriting **"Physical Debt"** that cannot be fixed by Reinforcement Learning (RL) fine-tuning or increasing GPU compute.

**The Solution: Bridging the Reality Gap**

To mitigate the structural drift identified by this benchmark, you must implement a **Non-Associative Temporal Layer**.
Click here to access the Fix: https://github.com/ZC502/Isaac-Sim-Physical-consistency-plugin.git


**How to Load the Plugin for Audit-Repair Cycle**:

1. **Clone the Plugin** into your exts/ directory.
2. **Enable the Octonion Layer** in your simulation configuration:

```
from isaac_plugin.octonion_layer import OctonionTemporalSemantics
# Wrap your existing stepper
simulation_context.add_physics_callback("octonion_bridge", octonion_semantics.step)
```
3. **Re-run this PCA Benchmark**. You will observe a significant convergence in energy residuals and a reduction in the Associator-driven causality breaks.

## What is PCA?

PCA evaluates:
- Perturbation robustness
- Energy consistency
- Numerical convergence

independently of task success or solver stability.

## Requirements

- Python ≥ 3.9
- numpy, pandas, matplotlib
- Isaac Sim (for Isaac benchmarks)

## How to Run

### Isaac Sim + Octonion system

To evaluate the "Isaac+Oct" system, you must first enable the
Octonion Temporal Semantics extension:

https://github.com/ZC502/Isaac-Sim-Physical-consistency-plugin

Steps:
1. Clone the extension into your Isaac Sim `exts/` directory
2. Enable `octonion_time` in the Extension Manager
3. Restart Isaac Sim
4. Run `pca_runner.py`

If the extension is not enabled, the "Isaac+Oct" score will be identical
to the baseline Isaac Sim score.

Note:
You do NOT need to run `octonion.py` manually.

Once the `octonion_time` extension is enabled, its temporal update logic
is automatically applied during each PhysX simulation step.

The PCA runner (`pca_runner.py`) only launches simulations and measures
physical consistency metrics.


```bash
python runners/pca_runner.py

Outputs:

-results/raw/pca_results.csv

-results/plots/energy_jitter.png

-results/plots/pca_score.png

Interpretation

Higher PCA scores indicate closer adherence to physically expected
numerical behavior under perturbation and dynamic coupling.


Scope

PCA does not claim simulator correctness.
It audits numerical and architectural consistency.

Extending PCA

New simulators can be added by implementing compatible benchmark scripts
and registering them in pca_runner.py.
