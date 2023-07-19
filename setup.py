# if i want to concept my project into package ,then setup.py is needed
from setuptools import find_packages,setup
from typing import List #this will be the return type of the packages we are specifically reading

HYPEN_E_DOT= 'e .'

def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
## we should give requirements.txt a chance to build all the packages 
# whenwver we install new library we should give our setup.py to build a package 
# whenever we installing requirements.txt , then setup.py is going to trigger


setup(
    name = 'RegressionProject',
    version = '0.0.1',
    author = 'Anil Kamat',
    author_email= 'anilkamat@gmail.com',
    install_requires = get_requirements("requirements.txt"),
    packages = find_packages()
)