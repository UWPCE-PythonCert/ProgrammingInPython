#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class

class Element:
    """
    Base class for all HTML elements

    This is an "abstract" base class, it is not intended
    to be used by itself, but only used as a template for
    specific element subclasses
    """

    def __init__(self, content=None):
        pass

    def append(self, new_content):
        pass

    def render(self, out_file):
        out_file.write("Just something as a place holder...")
