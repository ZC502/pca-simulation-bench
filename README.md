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
