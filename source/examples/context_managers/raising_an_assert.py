#!/usr/bin/env python

"""
examples of forcing and an AssertionError
"""


def test_raise_assertion():
    raise AssertionError("this was done with a direct raise")


def test_trasditional_assert():
    assert False, "this was done with a forced assert"
