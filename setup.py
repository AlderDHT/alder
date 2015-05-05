#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setup.py

Basic setup file to enable pip install
See:
    http://pythonhosted.org//setuptools/setuptools.html
    https://pypi.python.org/pypi/setuptools

python setup.py register sdist upload

"""
# Import python libs
import os
import sys
from setuptools import setup, find_packages



# Change to Alders's source's directory prior to running any command
try:
    SETUP_DIRNAME = os.path.dirname(__file__)
except NameError:
    # We're most likely being frozen and __file__ triggered this NameError
    # Let's work around that
    SETUP_DIRNAME = os.path.dirname(sys.argv[0])

if SETUP_DIRNAME != '':
    os.chdir(SETUP_DIRNAME)

SETUP_DIRNAME = os.path.abspath(SETUP_DIRNAME)

ALDER_METADATA = os.path.join(SETUP_DIRNAME, 'alder', '__metadata__.py')

# Load the metadata using exec() in order not to trigger alder.__init__ import
exec(compile(open(ALDER_METADATA).read(), ALDER_METADATA, 'exec'))

REQUIREMENTS = ['libnacl>=1.4.0' ]

if sys.version_info < (2, 7): #tuple comparison element by element
    # Under Python 2.6, also install
    REQUIREMENTS.extend([
        'importlib>=1.0.3',
        'argparse>=1.2.1'
    ])

if sys.version_info < (3, 4): #tuple comparison element by element
    REQUIREMENTS.extend([
        'enum34>=1.0.4',
    ])

setup(
    name='alder',
    version=__version__,
    description='Asynchrounous Lexical Distributed Event Roster',
    long_description=' Consensus DHT database. Nested key value store.'
                     ' ',
    url='https://github.com/AlderDHT/alder.git',
    download_url='https://github.com/AlderDHT/alder/archive/master.zip',
    author=__author__,
    author_email='smith.samuel.m@gmail.com',
    license=__license__,
    keywords=('Asynchrounous Lexical Distributed Event Roster Consensus DHT Key Value Store'),
    packages=find_packages(exclude=['test', 'test.*',
                                      'docs', 'docs*',
                                      'log', 'log*']),
    package_data={
                   '':       ['*.txt',  '*.md', '*.rst', '*.json', '*.conf', '*.html',
                              '*.css', '*.ico', '*.png', 'LICENSE', 'LEGAL'],
                   },
    install_requires=REQUIREMENTS,
    extras_require={},
    #scripts=['scripts/alder'],
    )
