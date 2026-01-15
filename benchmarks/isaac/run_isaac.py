from .perturbation_test import run_perturbation_test
from .energy_test import run_energy_test

def run():
    p = run_perturbation_test()
    e = run_energy_test()

    return {
        "PRS": p["PRS"],
        "RMS": p["RMS"],
        "MRED": e["MRED"],
        "EJI": e["EJI"],
        "TVA": e["TVA"],
        "bounded": p["bounded"] and e["bounded"]
    }
