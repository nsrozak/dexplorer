# global imports
from setuptools import setup, find_packages

# library specifications
setup(name='dexplorer',
      version='0.0.0',
      packages=find_packages(exclude=['examples', 'dexplorer_tests']),
      install_requires=['matplotlib==3.7.2', 
                        'numpy==1.24.4', 
                        'pandas==2.0.3', 
                        'scipy==1.10.1'
                       ]
      )
