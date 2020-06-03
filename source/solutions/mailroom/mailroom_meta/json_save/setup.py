#!/usr/bin/env python

"""
This is about as simple a setup.py as you can have

But its enough to support the json_save package

"""

import os

from setuptools import setup, find_packages


def get_version():
    """
    Reads the version string from the package __init__ and returns it
    """
    with open(os.path.join("json_save", "__init__.py")) as init_file:
        for line in init_file:
            parts = line.strip().partition("=")
            if parts[0].strip() == "__version__":
                return parts[2].strip().strip("'").strip('"')
    return None


setup(
    name='json_save',
    version=get_version(),
    author='Chris Barker',
    author_email='PythonCHB@gmail.com',
    packages=find_packages(),
    # license='LICENSE.txt',
    description='Metaclass based system for saving object to JSON',
    long_description=open('README.txt').read(),
)
