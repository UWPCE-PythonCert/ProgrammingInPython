#!/usr/bin/env python

"""
This is about as simple a setup.py as you can have

But its enough to support the mailroom app

"""

import os

from setuptools import setup


def get_version():
    """
    Reads the version string from the package __init__ and returns it
    """
    with open(os.path.join("mailroom", "__init__.py")) as init_file:
        for line in init_file:
            parts = line.strip().partition("=")
            if parts[0].strip() == "__version__":
                return parts[2].strip().strip("'").strip('"')
    return None


setup(
    name='mailroom',
    version=get_version(),
    author='Chris Barker',
    author_email='PythonCHB@gmail.com',
    packages=['mailroom',
              'mailroom/test'],
    scripts=['bin/mailroom'],
    package_data={'mailroom': ['data/sample_data.json']},
    license='LICENSE.txt',
    description='Simple app for managing donations for a non-profit',
    long_description=open('README.txt').read(),
)
