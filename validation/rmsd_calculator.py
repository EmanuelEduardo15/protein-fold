# validation/rmsd_calculator.py  
import numpy as np  

def calculate_rmsd(predicted: np.ndarray, experimental: np.ndarray) -> float:  
    """  
    Calcula RMSD entre estruturas previstas e experimentais.  
    """  
    return np.sqrt(np.mean((predicted - experimental)**2)
