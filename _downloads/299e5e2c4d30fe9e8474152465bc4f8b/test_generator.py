"""
test_generator.py

tests the solution to the generator lab

can be run with pytest
"""

import generator_solution as gen


def test_intsum():

    g = gen.intsum()

    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 3
    assert next(g) == 6
    assert next(g) == 10
    assert next(g) == 15


def test_intsum2():

    g = gen.intsum2()

    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 3
    assert next(g) == 6
    assert next(g) == 10
    assert next(g) == 15


def test_doubler():

    g = gen.doubler()

    assert next(g) == 1
    assert next(g) == 2
    assert next(g) == 4
    assert next(g) == 8
    assert next(g) == 16
    assert next(g) == 32

    for i in range(10):
        j = next(g)

    assert j == 2**15


def test_fib():
    g = gen.fib()
    assert [next(g) for i in range(9)] == [1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_prime():
    g = gen.prime()
    for val in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        assert next(g) == val
