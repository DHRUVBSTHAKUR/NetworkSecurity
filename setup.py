from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    """
    this function will return list of requirements 
    """
    requirement_list:List[str]=[]
    try :
        with open('requirements.txt','r') as file:
            #Reaad lines formthe file 
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()
                ## ignore the empty lines and ignore -e.

                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found ")
    return requirement_list
print(get_requirements())

setup(
    name="Network Securiy",
    version="0.0.1",
    author="Dhruv",
    author_email="dhruvbsthakur@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)



