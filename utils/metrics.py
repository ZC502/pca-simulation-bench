import numpy as np

def compute_pca_metrics(raw):
    return raw

def compute_pca_score(m):
    PRS = min(m["PRS"] / 0.95, 1.0)
    RMS = np.exp(-m["RMS"] / 0.1)
    MRED = np.exp(-m["MRED"] / 0.02)
    EJI = np.exp(-m["EJI"] / 0.005)
    TVA = np.exp(-m["TVA"] / 0.01)

    score = (
        0.25 * PRS +
        0.20 * RMS +
        0.20 * MRED +
        0.20 * EJI +
        0.15 * TVA
    )

    if not m["bounded"]:
        score *= 0.7

    return int(100 * score)
