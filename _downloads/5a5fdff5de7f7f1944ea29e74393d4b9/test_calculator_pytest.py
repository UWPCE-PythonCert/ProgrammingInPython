#!/use/bin/env python

"""
tests for the calculator module

designed to be run with pytest
"""

import pytest

import calculator_functions as calc


# a very simple test
def test_add():
    assert calc.add(2, 3) == 5


# testing with a variety of parameters:
def test_multiply_ugly():
    """
    the ugly, not very robust way....
    """
    assert calc.multiply(2, 2) == 4
    assert calc.multiply(2, -1) == -2
    assert calc.multiply(-2, -3) == 6
    assert calc.multiply(3, 0) == 0
    assert calc.multiply(0, 3) == 0


param_names = "arg1, arg2, result"
params = [(2, 2, 4),
          (2, -1, -2),
          (-2, -2, 4),
          (3, 0, 0),
          ]
@pytest.mark.parametrize(param_names, params)
def test_multiply(arg1, arg2, result):
    assert calc.multiply(arg1, arg2) == result
