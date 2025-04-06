# core/curvature_energy.py  
import numpy as np  

def curvature_energy(kappa: np.ndarray, beta: float = 1.0) -> float:  
    """  
    Calcula ΔG de dobramento via curvatura (Equação 5 em supp_application.pdf).  
    Entrada:  
        - kappa: Array de curvaturas locais (unidade: nm⁻¹).  
        - beta: Fator de acoplamento termodinâmico.  
    Saída:  
        - Energia em kT.  
    """  
    return beta * np.sum(kappa**2)  

def optimize_folding(kappa_init: np.ndarray, steps: int = 1000) -> np.ndarray:  
    """  
    Otimiza a curvatura para minimizar ΔG (Algoritmo S2.5 em supp_application.pdf).  
    """  
    kappa = kappa_init.copy()  
    learning_rate = 0.01  
    for _ in range(steps):  
        grad = 2 * kappa  # Derivada de κ²  
        kappa -= learning_rate * grad  
    return kappa
