# Physical Consistency Audit (PCA)

This repository provides a reproducible benchmark for auditing
physical consistency in robotics simulation platforms.

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
