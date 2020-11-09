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


def test_too_few():
    assert not walnut_party(30, False)


def test_middle():
    assert walnut_party(50, False)


def test_too_many():
    assert walnut_party(70, True)


def test_middle50():
    assert walnut_party(50, True)


def test_upper_bound():
    assert walnut_party(60, False)


def test_just_too_big():
    assert not walnut_party(61, False)


def test_lower_bound():
    assert walnut_party(40, False)


def test_just_too_small():
    assert walnut_party(39, False) is False
