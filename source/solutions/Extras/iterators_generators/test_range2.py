"""
test code for range2.py

It should act just like the built-in range object
"""

import pytest

# from range2 import range2
from range3 import range3 as range2


def test_just_stop():
    assert list(range(5)) == list(range2(5))


def test_negative_stop():
    assert list(range2(-1)) == []


def test_start_stop_same():
    assert list(range2(3, 3)) == []


def test_start_negative():
    assert list(range(-3, 4)) == list(range2(-3, 4))


def test_start_stop_negative():
    assert list(range(3, 8)) == list(range2(3, 8))


def test_start_stop_step():
    assert list(range(2, 10, 2)) == list(range2(2, 10, 2))


def test_start_stop_negative_step():
    # careful -- this one could never terminate if done wrong!
    assert list(range(10, 2, -2)) == list(range2(10, 2, -2))


def test_start_stop_negative_step_invalid():
    # careful -- this one could never terminate if done wrong!
    assert list(range(2, 10, -2)) == list(range2(2, 10, -2))


def test_restart():
    r2 = range2(10)
    for i in r2:
        if i > 5:
            break
    assert [i for i in r2] == list(range2(10))


def test_non_int():
    with pytest.raises(TypeError):
        range2(5.5)
    with pytest.raises(TypeError):
        range2("5")
    with pytest.raises(TypeError):
        range2(5, 6.5)


def test_zero_step():
    with pytest.raises(ValueError):
        range2(2, 10, 0)


def test_not_call_iter():
    """
    If you try to call next directly it should raise an error.
    """
    with pytest.raises(TypeError):
        next(range2(3))



