#!/usr/bin/env python

from circle import Circle, Sphere

import pytest

from math import pi
import random


def test_init():
    """
    tests that you can initilize a Circle
    """
    Circle(3)


def test_radius():
    """
    test that the radius is properly set and can be retrieved
    """
    c = Circle(3)

    assert c.radius == 3


def test_no_radius():
    """
    test that you get an Exception if you don't provide a radius
    """
    with pytest.raises(TypeError):
        c = Circle()


def test_set_radius():
    """
    test that changing the radius "stays"
    """
    c = Circle(3)
    c.radius = 5
    assert c.radius == 5


def test_diam():
    """
    can you retrieve the diameter?
    """
    c = Circle(3)

    assert c.diameter == 6


def test_radius_change():
    """
    does the diameter change after changing the radius?
    """
    c = Circle(3)
    c.radius = 4
    assert c.diameter == 8


def test_set_diameter():
    """
    can you set the diameter?
    """
    c = Circle(4)
    c.diameter = 10

    assert c.radius == 5
    assert c.diameter == 10


def test_set_diameter_float():
    """
    is floating point computation used for computing the diameter?
    """
    c = Circle(4)
    c.diameter = 11

    assert c.radius == 5.5
    assert c.diameter == 11


def test_area():
    """
    is the area computed correctly?
    """
    c = Circle(2)

    assert c.area == pi*4


def test_set_area():
    """
    you should not be able to set the area
    """
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area = 30


def test_from_diameter():
    """
    can we create a Circle from the diameter?
    """
    c = Circle.from_diameter(4)

    assert isinstance(c, Circle)
    assert c.radius == 2
    assert c.diameter == 4


def test_repr():
    """
    does it have a correct repr()?
    """
    c = Circle(6.0)

    assert repr(c) == 'Circle(6.0)'


def test_str():
    """
    does it have a correct str()?
    """
    c = Circle(3.0)

    assert str(c) == 'Circle with radius: 3'


def test_addition():
    """
    do two circles add up correctly
    """
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = c1 + c2

    assert c3.radius == 5


def test_multiplication():
    """
    Can you scale a circle my multiplying it?
    """
    c1 = Circle(2)
    c3 = c1 * 4

    assert c3.radius == 8


def test_equal():
    """
    Does equality work?
    """
    c1 = Circle(3)
    c2 = Circle(3.0)

    assert c1 == c2
    assert c1 <= c2
    assert c1 >= c2


def test_not_equal():
    """
    does not equal work?
    """
    c1 = Circle(2.9)
    c2 = Circle(3.0)

    assert c1 != c2


def test_greater():
    """
    comparison: greater than
    """
    c1 = Circle(2)
    c2 = Circle(3)

    assert c2 > c1
    assert c2 >= c1


def test_less():
    """
    comparison: less than
    """
    c1 = Circle(2)
    c2 = Circle(3)

    assert c1 < c2
    assert c1 <= c2


def test_reverse_multiply():
    """
    multiplication in the other order
    """
    c = Circle(3)

    c2 = 3 * c

    assert c2.radius == 9.0


def test_plus_equal():
    """
    in-place addition
    """
    c = Circle(3)
    c2 = c

    c += Circle(2)

    assert c.radius == 5
    assert c is c2
    assert c2.radius == 5


def test_times_equal():
    """
    in-place multiplication
    """
    c = Circle(3)
    c2 = c

    c *= 2

    assert c.radius == 6
    assert c is c2
    assert c2.radius == 6


def test_sort():
    """
    can circles be sorted?
    """
    a_list = [Circle(20), Circle(10), Circle(15), Circle(5)]

    a_list.sort()

    assert a_list[0] == Circle(5)
    assert a_list[3] == Circle(20)
    assert a_list[0] < a_list[1] < a_list[2] < a_list[3]


#############################
# Tests for the Sphere Object
#############################
def test_sphere_vol():
    """
    Is the volume correct?
    """
    s = Sphere(4)

    print(s.volume())
    assert s.volume() == 268.082573106329


def test_sphere_change_radius():
    """
    create from diameter, change the radius

    NOTE: if you subclassed Circlel then this all should "just work"!
    """
    s = Sphere.from_diameter(8)

    assert s.radius == 4

    s.radius = 3
    assert s.diameter == 6


def test_sphere_diameter():
    s = Sphere.from_diameter(8)

    # check that the classmethod got properly inherited
    assert type(s) == Sphere
    print(s.volume())
    assert s.volume() == 268.082573106329


def test_sphere_area():
    """
    sphere's don't really have an area in the same way
    """
    s = Sphere(4)

    with pytest.raises(NotImplementedError):
        s.area()


def test_sphere_repr():
    s = Sphere(12)

    assert repr(s) == "Sphere(12)"
    assert eval(repr(s)) == s


def test_sphere_str():
    s = Sphere(12)

    assert str(s) == "Sphere with radius: 12"
    assert eval(repr(s)) == s


def test_sphere_sort():
    list_o_spheres = [Sphere(random.randint(1, 20)) for i in range(10)]

    print(list_o_spheres)

    list_o_spheres.sort()

    print(list_o_spheres)

    for s1, s2 in zip(list_o_spheres, list_o_spheres[1:]):
        assert s1 <= s2



