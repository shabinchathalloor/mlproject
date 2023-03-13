# Building our project as a package
from setuptools import find_packages,setup

setup(
name='mlproject',
version='0.0.1',
author='Shabin',
author_email='mailbox.shabin@gmail.com',
packages=find_packages(),
install_requires=['pandas','numpy','seaborn']   
)