import numpy as np  
from core.curvature_energy import curvature_energy  
from simulations.folding_simulator import ProteinSimulator  

# Simula dobramento da ubiquitina (76 resíduos)  
simulator = ProteinSimulator(length=76)  
kappa_final = simulator.run()  
np.save("examples/ubiquitin_kappa.npy", kappa_final)
