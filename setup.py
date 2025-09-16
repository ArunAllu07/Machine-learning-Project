from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements,
    excluding editable install options like '-e .'
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]

    return requirements

setup(
    name='Machine Learning Project',
    version='0.0.1',
    author='Kethavath Arun',
    author_email='kethavatharun856@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
