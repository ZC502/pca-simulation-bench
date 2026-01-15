import matplotlib.pyplot as plt

def plot_pca_scores(df, out_path="results/plots/pca_scores.png"):
    systems = df["system"]
    scores = df["PCA_score"]

    plt.figure(figsize=(6, 4))
    plt.bar(systems, scores)
    plt.ylim(0, 100)
    plt.ylabel("PCA Score (0–100)")
    plt.title("Physical Consistency Audit (PCA)")

    for i, v in enumerate(scores):
        plt.text(i, v + 2, str(v), ha="center", fontsize=10)

    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
