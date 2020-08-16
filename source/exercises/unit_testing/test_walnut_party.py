#!/usr/bin/env python

"""
test code for the walnut party example

Adapted from the "coding bat" site: https://codingbat.com/python

When squirrels get together for a party, they like to have walnuts.
A squirrel party is successful when the number of walnuts is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of walnuts.

Return True if the party with the given values is successful,
or False otherwise.
"""


# you can change this import to test different versions
from walnut_party import walnut_party
# from walnut_party import walnut_party2 as walnut_party
# from walnut_party import walnut_party3 as walnut_party


def test_1():
    assert walnut_party(30, False) is False


def test_2():
    assert walnut_party(50, False) is True


def test_3():
    assert walnut_party(70, True) is True


def test_4():
    assert walnut_party(30, True) is False


def test_5():
    assert walnut_party(50, True) is True


def test_6():
    assert walnut_party(60, False) is True


def test_7():
    assert walnut_party(61, False) is False


def test_8():
    assert walnut_party(40, False) is True


def test_9():
    assert walnut_party(39, False) is False


def test_10():
    assert walnut_party(40, True) is True


def test_11():
    assert walnut_party(39, True) is False
