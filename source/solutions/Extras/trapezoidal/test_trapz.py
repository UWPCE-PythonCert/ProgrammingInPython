#!/usr/bin/env python3

"""
test code for the trapezoidal rule exercise
"""
import pytest

from trapz import trapz, frange, quadratic, curry_quadratic

# need a function for testing approximate equality
import math
from math import isclose


# you need to compute a bunch of evenly spaced numbers from a to b
#  kind of like range() but for floating point numbers
# I did it as a separate function so I could test it
def test_frange():
    '''
    tests the floating point range function
    '''
    r = list(frange(10, 20, 100))
    assert len(r) == 101
    assert r[0] == 10
    assert r[-1] == 20
    assert r[1] == 10.1
    assert r[-2] == 19.9


def test_simple_line():
    ''' a simple horizontal line at y = 5'''
    def line(x):
        return 5

    assert trapz(line, 0, 10) == 50


def test_sloping_line():
    ''' a simple linear function '''
    def line(x):
        return 2 + 3*x

    # I got 159.99999999999 rather than 160
    #   hence the need for isclose()
    assert isclose(trapz(line, 2, 10), 160)
    m, B = 3, 2
    a, b = 0, 5
    assert isclose(trapz(line, a, b), 1/2*m*(b**2 - a**2) + B*(b-a))

    a, b = 5, 10
    assert isclose(trapz(line, a, b), 1/2*m*(b**2 - a**2) + B*(b-a))

    a, b = -10, 5
    assert isclose(trapz(line, a, b), 1/2*m*(b**2 - a**2) + B*(b-a))


def test_sine():
    #  a sine curve from zero to pi -- should be 2
    # with a hundred points, only correct to about 4 figures
    assert isclose(trapz(math.sin, 0, math.pi), 2.0, rel_tol=1e-04)


def test_sine2():
    #  a sine curve from zero to 2pi -- should be 0.0
    # need to set an absolute tolerance when comparing to zero
    assert isclose(trapz(math.sin, 0, 2*math.pi), 0.0, abs_tol=1e-8)


# test the quadratic function itself
#   this is pytest's way to test a bunch of input and output values
#   it creates a separate test for each case.
@pytest.mark.parametrize(("x", "y"), [(0, 1),
                                      (1, 3),
                                      (2, 7),
                                      (-2, 3)
                                      ])
def test_quadratic_1(x, y):
    """
    one set of coefficients
    """
    assert quadratic(x, A=1, B=1, C=1) == y


# this is a nifty trick to write multiple tests at once:
# this will generate a test for each tuple passed in:
#   each tuple is an x, and the expected y result
@pytest.mark.parametrize(("x", "y"), [(0, 2),
                                      (1, 3),
                                      (2, 0),
                                      (-2, -12)
                                      ])
def test_quadratic_2(x, y):
    """
    different coefficients
    """
    assert quadratic(x, A=-2, B=3, C=2) == y


def quad_solution(a, b, A, B, C):
    """
    Analytical solution to the area under a quadratic
    used for testing
    """
    return A/3*(b**3 - a**3) + B/2*(b**2 - a**2) + C*(b - a)


def test_quadratic_trapz_1():
    """
    simplest case -- horizontal line
    """
    A, B, C = 0, 0, 5
    a, b = 0, 10
    assert trapz(quadratic, a, b, A=A, B=B, C=C) == quad_solution(a, b, A, B, C)


def test_quadratic_trapz_2():
    """
    one case: A=-1/3, B=0, C=4
    """
    A, B, C = -1/3, 0, 4
    a, b = -2, 2
    assert isclose(trapz(quadratic, a, b, A=A, B=B, C=C),
                   quad_solution(a, b, A, B, C),
                   rel_tol=1e-3)  # not a great tolerance -- maybe should try more samples!


def test_quadratic_trapz_args_kwargs():
    """
    Testing if you can pass a combination of positional and keyword arguments
    one case: A=2, B=-4, C=3
    """
    A, B, C = 2, -4, 3
    a, b = -2, 2
    assert isclose(trapz(quadratic, a, b, A, B, C=C),
                   quad_solution(a, b, A, B, C),
                   rel_tol=1e-3)  # not a great tolerance -- maybe should try more samples!


def test_curry_quadratic():
    # tests if the quadratic currying function

    # create a specific quadratic function:
    quad234 = curry_quadratic(2, 3, 4)
    # quad234 is now a function that can take one argument, x
    # and will evaluate quadratic for those particular values of A,B,C

    # try it for a few values
    for x in range(5):
        assert quad234(x) == quadratic(x, 2, 3, 4)


def test_curry_quadratic_trapz():
    # tests if the quadratic currying function

    # create a specific quadratic function:
    quad234 = curry_quadratic(-2, 2, 3)
    # quad234 is now a function that can take one argument, x
    # and will evaluate quadratic for those particular values of A,B,C

    # try it with the trapz function
    assert trapz(quad234, -5, 5) == trapz(quadratic, -5, 5, -2, 2, 3)


# testing the functools.partial version:
from trapz import quad_partial_123


def test_partial():
    a = 4
    b = 10
    # quad_partial_123 is the quadratic function with A,B,C = 1,2,3
    assert trapz(quad_partial_123, a, b) == trapz(quadratic, a, b, 1, 2, 3)


# testing trapz with another function with multiple parameters.
def sine_freq_amp(t, amp, freq):
    "the sine function with a frequency and amplitude specified"
    return amp * math.sin(freq * t)


def solution_freq_amp(a, b, amp, freq):
    " the solution to the definite integral of the general sin function"
    return amp / freq * (math.cos(freq * a) - math.cos(freq * b))


def test_sine_freq_amp():
    a = 0
    b = 5
    omega = 0.5
    amp = 10
    assert isclose(trapz(sine_freq_amp, a, b, amp=amp, freq=omega),
                   solution_freq_amp(a, b, amp, omega),
                   rel_tol=1e-04)
