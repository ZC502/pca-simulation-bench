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
