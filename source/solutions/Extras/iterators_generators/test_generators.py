#!/usr/bin/env python
"""
Test code for generator assignments

Designed to be run with py.test
"""

import generators as gs


def test_intsum():
    g = gs.intsum()
    for val in [0, 1, 3, 6, 10]:
        assert next(g) == val


def test_intsum2():
    g = gs.intsum2()
    for val in [0, 1, 3, 6, 10]:
        assert next(g) == val


def test_doubler():
    g = gs.doubler()
    for val in [1, 2, 4, 8, 16, 32, 64]:
        assert next(g) == val


def test_fib():
    g = gs.fib()
    assert [next(g) for i in range(9)] == [1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_prime():
    g = gs.prime()
    for val in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        assert next(g) == val


def test_prime2():
    """ same test as above, but a better algorithm """
    g = gs.prime2()
    for val in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        p = next(g)
        print("p is:", p)
        assert p == val
#    assert False


def test_squares():
    g = gs.squares(10)
    assert list(g) == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


def test_squares2():
    g = gs.squares2(10)
    assert list(g) == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
