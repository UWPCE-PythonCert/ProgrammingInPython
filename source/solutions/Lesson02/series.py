#!/usr/bin/env python

"""
series.py

solutions to the Fibonacci Series, Lucas numbers and
generalized sum_series

These solutions use recursion
-- calling a funciton from within that function.

These series are defined "recusively", so it's a
really natural way to express the solution. However,
recursion can be substantially less efficient.n

See series_non_recursive.py for a more efficient way
to do it.
"""


def fibonacci(n):
    """ compute the nth Fibonacci number """

    if n < 0:  # check for negative number -- just in case.
        return None
    elif n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """ compute the nth Lucas number """

    if n < 0:
        return None
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, n0=0, n1=1):
    """
    Compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to fibonacci(n).
    And sum_series(n, 2, 1) should be equivalent to lucas(n).

    sum_series(n, 3, 2) should generate antoehr series with no specific name

    The defaults are set to 0, 1, so if you don't pass in any values, you'll
    get the fibonacci sercies
    """

    if n < 0:
        return None
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)

# Can you re-define fibonacci and lucas by using sum_series?


if __name__ == "__main__":
    # run some tests

    assert fibonacci(-1) is None
    assert fibonacci(-23) is None

    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(-1) is None
    assert lucas(-23) is None

    # do these with a loop:
    tests = [(0, 2),
             (1, 1),
             (2, 3),
             (3, 4),
             (4, 7),
             (5, 11),
             (6, 18),
             (7, 29),
             ]
    for input, output in tests:
        assert lucas(input) == output

    # test if sum_series matched Fibonacci
    for n in range(0, 10):
        assert sum_series(n) == fibonacci(n)

    # test if sum_series matched lucas
    for n in range(0, 10):
        assert sum_series(n, 2, 1) == lucas(n)

    # test if sum_series works for negative value
    # (it should return None)

    assert sum_series(-1, 3, 2) is None

    # test if sum_series works for arbitrary initial values
    assert sum_series(0, 3, 2) == 3
    assert sum_series(1, 3, 2) == 2
    assert sum_series(2, 3, 2) == 5
    assert sum_series(3, 3, 2) == 7
    assert sum_series(4, 3, 2) == 12
    assert sum_series(5, 3, 2) == 19

    print("tests passed")
