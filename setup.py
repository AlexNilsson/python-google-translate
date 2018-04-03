"""A python wrapper for google translate
See
https://github.com/AlexNilsson/python-google-translate
"""

# Developers:
# Install with:
#   pip install -e .
# Distribute with:
# python setup.py bdist_wheel
# twine upload dist/*

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='multitrans',
    version='1.0.0',
    packages=find_packages(),

    install_requires=['setuptools>=28.8.0'],

    author='Alexander Nilsson',
    author_email='contact@alexnilsson.io',
    description='Translate multiple strings to multiple languages using Google Translate',
    license="MIT",
    keywords='google translate multiple languages',
    url='https://github.com/AlexNilsson/python-google-translate',


    long_description=long_description,
    long_description_content_type='text/markdown',

)
