# validation/test_accuracy.py  
def test_ubiquitin():  
    # Dados fictícios (exemplo)  
    kappa_exp = np.load("data/ubiquitin_kappa.npy")  # ✅ Use dados anônimos  
    kappa_pred = ProteinSimulator().run()  
    assert calculate_rmsd(kappa_pred, kappa_exp) < 1.0  # 0.8 Å no paper
