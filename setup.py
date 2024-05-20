from setuptools import setup, find_packages

# read the requirements.txt file and use it to install dependencies
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()


setup(
    name='checkdir',
    description='python CLI tool to list block devices',
    packages=find_packages(),
    author='Elminson De Oleo Baez',
    entry_points="""
    [console_scripts]
    checkdir=checkdir.main:main
    """,
    #install_requires=['click==7.1.2'],
    install_requires=install_requires,
    version='0.0.1',
    url='https://github.com/elminson/python-cli-01',
)
