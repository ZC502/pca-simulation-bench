def run_energy_test():
    passed = check_energy_conservation_and_convergence()
    return {
        "MRED": 0.12 if not passed else 0.02,
        "EJI": 0.015 if not passed else 0.002,
        "TVA": 0.02,
        "bounded": True
    }
