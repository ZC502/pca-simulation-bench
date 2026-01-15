import pandas as pd

from benchmarks.mujoco.run_mujoco import run as run_mujoco
from benchmarks.isaac.run_isaac import run as run_isaac
from utils.metrics import compute_pca_score
from utils.plotting import plot_pca_scores

SYSTEMS = {
    "MuJoCo": run_mujoco,
    "Isaac Sim": run_isaac,
    "Isaac+Oct": run_isaac_octonion,
}

def main():
    rows = []

    for name, runner in SYSTEMS.items():
        metrics = runner()
        score = compute_pca_score(metrics)

        metrics["system"] = name
        metrics["PCA_score"] = score
        rows.append(metrics)

    df = pd.DataFrame(rows)
    df.to_csv("results/raw/pca_results.csv", index=False)

    plot_pca_scores(df)

if __name__ == "__main__":
    main()
