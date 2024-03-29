from setuptools import setup, find_packages

setup(
    name='mypackage',
    version= '0.2',
    packages= find_packages(exclude=['tests*']),
    license= 'MIT',
    description= 'EDSA python packages example',
    long_description= open('README.md').read(),
    install_requires = ['numpy'],
    url= 'https://github.com/Stephen-Kansanga/mypackage',
    author= 'Stephen Kansanga',
    author_email= 'stephenkansanga@gmail.com'
)