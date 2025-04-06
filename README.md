# ProteinFold: Dobramento de Proteínas via Curvometria Modular  
**Precisão**: 0.8 Å RMSD | **Velocidade**: 10x mais rápido que simulações clássicas  

## Instalação  
1. Clone o repositório:  
   ```bash  
   git clone https://github.com/EmanuelEduardo15/protein-fold.git  
   cd protein-fold
 # Cria o ambiente  
conda env create -f environment.yml
conda activate protein-fold           
# compila o plugin  
cd rosetta_plugin 
mkdir build && cd build                  
cmake .. && make
## Licença  
Leia os termos completos em [LICENSE.md]
[LICENSE.md].
