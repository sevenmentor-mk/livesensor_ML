from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    
    requirement_list :List[str] = []

    return requirement_list

setup(
    name='sensor',
    version="1.0.1",
    author="Mahesh Kankrale",
    author_email="mkankrale@sevenmentor.com",
    packages=find_packages(),
    install_requires = get_requirements(),
)