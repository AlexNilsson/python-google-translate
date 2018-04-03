"""A python wrapper for google translate
See
https://github.com/AlexNilsson/python-google-translate
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='multrans',
    version='1.0.0',

    description='Translate multiple strings to multiple languages using Google Translate',

    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/AlexNilsson/python-google-translate',

    author='Alexander Nilsson',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='google translate multiple languages',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[],

    python_requires='>=3',
)
