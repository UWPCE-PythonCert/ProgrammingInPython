#!/usr/bin/env python

"""
nifty Circle class

Used to demo propeties and "magic methods"
"""

from math import pi
import functools


# this is a trick to make all the greater than, less than, etc work.
# see: https://docs.python.org/3.6/library/functools.html#functools.total_ordering
@functools.total_ordering
class Circle(object):
    """
    simple class to represent a circle

    one you can do math with -- a bit odd...
    """

    def __init__(self, radius):
        self.radius = float(radius)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2.0)

    @property
    def diameter(self):
        return self.radius * 2.0
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property
    def area(self):
        return self.radius**2 * pi

    def __repr__(self):
        # usingthe repr attributes is a neat trick
        return "Circle({:s})".format(repr(self.radius))

    def __str__(self):
        return "Circle with radius: {:g}".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        """
        for "augmented assignment" -- can be used for in-place addition

        Generally used that way for mutable types. This approach returns
        self, so that the object is changed in place -- i.e. mutated
        """
        self.radius += other.radius
        return self

    def __mul__(self, factor):
        return Circle(self.radius * factor)

    def __imul__(self, factor):
        """see __iadd__"""
        self.radius *= factor
        return self

    def __rmul__(self, factor):
        return Circle(self.radius * factor)

    # You can define them all:
    #  Might be useful for odd situations (and better performance)
    # def __eq__(self, other):
    #     return self.radius == other.radius
    # def __ne__(self, other):
    #     return self.radius != other.radius
    # def __gt__(self, other):
    #     return self.radius > other.radius
    # def __ge__(self, other):
    #     return self.radius >= other.radius
    # def __lt__(self, other):
    #     return self.radius < other.radius
    # def __le__(self, other):
    #     return self.radius <= other.radius

    # Or you can put the @total_ordering decorator on the class definition
    # and do only these:
    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius


# This demostrates how you can
#  subclass and get everyhting -- even the alternate constructor!
class Sphere(Circle):
    """
    A simple Sphere object, which you can do math with...
    """

    def volume(self):
        return 4 / 3 * pi * self.radius ** 3

    def area(self):
        raise NotImplementedError("Spheres don't have an area")

    def __repr__(self):
        return "Sphere({:g})".format(self.radius)

    def __str__(self):
        return "Sphere with radius: {:g}".format(self.radius)

