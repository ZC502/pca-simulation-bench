# runners/pca_runner.py
import pandas as pd
from utils.metrics import compute_pca_metrics, compute_pca_score
from utils.plotting import plot_energy_jitter, plot_pca_scores

SYSTEMS = [
    "isaac_baseline",
    "isaac_plugin",
]

def run_benchmarks(system):
    """
    Placeholder: call external benchmark scripts
    Expected to return a dict with raw metrics
    """
    # In practice, load CSV or JSON produced by benchmarks
    return {
        "PRS": 0.72 if system == "isaac_baseline" else 0.94,
        "RMS": 0.11 if system == "isaac_baseline" else 0.021,
        "MRED": 0.14 if system == "isaac_baseline" else 0.019,
        "EJI": 0.018 if system == "isaac_baseline" else 0.0021,
        "TVA": 0.022 if system == "isaac_baseline" else 0.003,
        "bounded": True,
    }

def main():
    rows = []

    for system in SYSTEMS:
        raw = run_benchmarks(system)
        metrics = compute_pca_metrics(raw)
        score = compute_pca_score(metrics)

        metrics["system"] = system
        metrics["PCA_score"] = score
        rows.append(metrics)

    df = pd.DataFrame(rows)
    df.to_csv("results/raw/pca_results.csv", index=False)

    plot_energy_jitter(df)
    plot_pca_scores(df)

if __name__ == "__main__":
    main()
