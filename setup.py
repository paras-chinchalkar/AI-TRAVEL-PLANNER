from setuptools import setup, find_packages
with open('requirements.txt') as f:
    requirements=f.read().splitlines()

setup(
    name="AI TRAVEL AGENT",
    version="0.1",
    packages=find_packages(),
    author="Paras Chinchalkar",
    install_requires=requirements, 
    
)