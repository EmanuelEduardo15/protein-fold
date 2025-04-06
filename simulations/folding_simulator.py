# simulations/folding_simulator.py  
import numpy as np  
from core.curvature_energy import optimize_folding  

class ProteinSimulator:  
    def __init__(self, length: int = 100):  
        self.kappa = np.random.uniform(0.1, 0.5, length)  

    def run(self) -> np.ndarray:  
        return optimize_folding(self.kappa)
