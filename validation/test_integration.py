def test_full_pipeline():  
    simulator = ProteinSimulator(length=50)  
    kappa = simulator.run()  
    assert curvature_energy(kappa) < 100.0  # Valor baseado em dados reais
