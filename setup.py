'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from pathlib import Path
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    req_file = Path(__file__).parent / 'requirements.txt'
    try:
        with open(req_file,'r') as file:
            for line in file:
                requirement=line.strip()
                ## ignore empty lines and pip options such as -e .
                if requirement and not requirement.startswith('-'):
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Amit Pawar",
    author_email="amitpawar16902@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)