#!/usr/bin/env

"""
A couple nifty context managers
"""

import pytest

class Failed(AssertionError):
    pass

class Raises:
    def __init__(self, *args):
        print("initializing:", args)
        self.exceptions = args

    def __enter__(self):
        """nothing to be done here."""
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Here's where we check the exceptions """
        if exc_type in self.exceptions:
            # tests pass
            return True
        else:
            expected = ", ".join([e.__name__ for e in self.exceptions])
            if exc_type is None:
                msg = "No error was raised -- expected {}".format(expected)
            else:
                msg = "{} raised -- expected {}".format(exc_type.__name__,
                                                        expected)
            raise Failed(msg)



# putting the tests for raises
# Four are expected to fail
def test_one_exp_pass():
    """This test should pass"""
    with Raises(ZeroDivisionError):
        45 / 0


def test_multiple_exp_pass():
    """This test should pass"""
    with Raises(ZeroDivisionError, AttributeError, RuntimeError):
        45 / 0


def test_multiple_exp_pass2():
    """This test should pass"""
    with Raises(ZeroDivisionError, AttributeError, RuntimeError):
        x = 5
        x.something_not_there


def test_one_exp_fail():
    """This test should fail"""
    with Raises(ZeroDivisionError):
        45 / 5


def test_one_exp_fail_diff_exp():
    """This test should fail"""
    with Raises(AttributeError):
        45 / 0.0


def test_multiple_exp_fail():
    """This test should fail"""
    with Raises(ZeroDivisionError, AttributeError, RuntimeError):
        45 / 5

def test_multiple_exp_fail_diff_exp():
    """This test should fail"""
    with Raises(ZeroDivisionError, AttributeError, RuntimeError):
        float("not a number")

