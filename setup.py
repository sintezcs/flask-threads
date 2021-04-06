from setuptools import find_packages
from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Flask-Threads',
    version='0.1.0',
    url='https://github.com/sintezcs/flask-threads.git',
    author='Alexey Minakov',
    author_email='a@spb.host',
    description='A helper library to work with threads'
                ' within Flask applications.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['tests']),
    install_requires=['Flask >= 0.9'],
)
