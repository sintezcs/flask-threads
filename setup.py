from setuptools import find_packages
from setuptools import setup

setup(
    name='Flask-Threads',
    version='0.0.1',
    url='https://github.com/sintezcs/flask-threads.git',
    author='Alexey Minakov',
    author_email='a@spb.host',
    description='A helper library to work with threads'
                ' within Flask applications.',
    packages=find_packages(exclude=['tests']),
    install_requires=['Flask >= 0.9'],
)
