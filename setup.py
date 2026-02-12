from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    # Read the requirements from the specified file and return a list of requirements
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    packages=find_packages(),
    author='Sudhakar Mishra',
    author_email='sdhkr.mshr@gmail.com',
    description='A machine learning project template',
   # install_requires=['seaborn', 'matplotlib', 'scikit-learn', 'pandas', 'numpy'],
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.6'
)       