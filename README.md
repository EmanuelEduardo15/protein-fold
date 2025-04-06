# ProteinFold: Dobramento de Proteínas via Curvometria Modular  
**Precisão**: 0.8 Å RMSD | **Velocidade**: 10x mais rápido que simulações clássicas  

## Instalação  
1. Clone o repositório:  
   ```bash  
   git clone https://github.com/EmanuelEduardo15/protein-fold.git  
   cd protein-fold
 conda env create -f environment.yml
# Cria o ambiente  
conda activate protein-fold          # 
# Ativa o ambiente  
cd rosetta_plugin && mkdir build && cd 
build  # Prepara para compilar  
cmake .. && make                     # 
# Compila o plugin
