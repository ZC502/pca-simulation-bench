# utils/plotting.py
import matplotlib.pyplot as plt

def plot_energy_jitter(df):
    plt.figure()
    plt.bar(df["system"], df["EJI"])
    plt.ylabel("Energy Jitter Index")
    plt.title("Energy Jitter Comparison")
    plt.savefig("results/plots/energy_jitter.png")
    plt.close()

def plot_pca_scores(df):
    plt.figure()
    plt.bar(df["system"], df["PCA_score"])
    plt.ylabel("PCA Score (0–100)")
    plt.title("Physical Consistency Audit Score")
    plt.ylim(0, 100)
    plt.savefig("results/plots/pca_score.png")
    plt.close()
