from setuptools import setup  

setup(  
    name="proteinfold",  
    version="1.0.0",  
    packages=["core", "simulations", "validation"],  
    install_requires=["numpy>=1.21", "scipy>=1.7"],  
)
