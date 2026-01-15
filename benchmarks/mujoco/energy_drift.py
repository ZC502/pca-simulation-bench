import mujoco
import numpy as np

def run_energy_test(xml_path, steps=2000):
    model = mujoco.MjModel.from_xml_path(xml_path)
    data = mujoco.MjData(model)

    energies = []

    for _ in range(steps):
        mujoco.mj_step(model, data)
        energies.append(data.energy[0])

    E = np.array(energies)
    dE = np.diff(E)

    results = {
        "MRED": np.max(np.abs((E - E[0]) / (E[0] + 1e-9))),
        "EJI": np.std(dE) / (np.mean(np.abs(E)) + 1e-9),
        "bounded": not (np.any(np.isnan(E)) or np.any(np.abs(E) > 1e6))
    }
    return results
