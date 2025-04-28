# ProteinFold: Dobramento de Proteínas via Curvometria Modular  
**Precisão**: 0.8 Å RMSD | **Velocidade**: 10x mais rápido que simulações clássicas  

## Instalação  
1. Clone o repositório:  
   ```bash  
   git clone https://github.com/EmanuelEduardo15/protein-fold.git  
   cd protein-fold
### Crie o ambiente  Conda
conda env create -f environment.yml 
### Ative o ambiente
conda activate protein-fold         
### Compilar o plugin do Rosseta
cd rosetta_plugin 
mkdir build && cd build  
cmake .. && make                    
## Licença  
Leia os termos completos em [LICENSE.md](LICENSE.md).
