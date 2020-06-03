#!/usr/bin/env python

"""
Solution to the generator homework
"""

import math


def intsum():  # 1 + 2 + 3 + 4 + 5...
    """
    simplest solution
    """
    a = b = 0
    while True:
        yield b
        a += 1
        b = b + a


def intsum2():  # 1 + 2 + 3 + 4 + 5...
    """
    takes advantage of some clever math
    """
    a = 0
    while True:
        yield (a * (a + 1)) / 2
        a += 1


def doubler():  # 1, 2, 4, 8, 16, 32, 64...
    a = 1
    while True:
        yield a
        a = a * 2


def fib():  # 1, 1, 2, 3, 5, 8, 13, 21, 34...
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def prime():  # 2, 3, 5, 7, 11, 13, 17, 19, 23...
    """ note that this is NOT a very efficient way to compute primes!"""
    a = 2
    while True:
        yield a
        p = False
        while not p:   # while not prime
            a += 1     # try the next integer
            p = True   # assume it is prime...
            for x in range(2, int(math.floor(math.sqrt(a))) + 1):
                if a % x == 0:
                    p = False           # ...unless it isn't
                    break

def prime():  # 2, 3, 5, 7, 11, 13, 17, 19, 23...
    """ note that this is NOT a very efficient way to compute primes!"""
    n = 0
    a = 2
    while True:
        yield a
        p = False
        while not p:   # while not prime
            a += 1     # try the next integer
            p = True   # assume it is prime...
            for x in range(2, int(math.floor(math.sqrt(a))) + 1):
                if a % x == 0:
                    p = False           # ...unless it isn't
                    break

def prime2():  # 2, 3, 5, 7, 11, 13, 17, 19, 23...
    """ This is a bit more efficient"""
    # keep a list of the primes already generated
    primes = []
    a = 2
    while True:
        # print("adding %s to the list"%a)
        primes.append(a)
        yield a
        p = False
        while not p:   # while not prime
            # try the next non-even integer
            a += (2 if (a % 2) else 1)
            p = True   # assume it is prime...
            # test if it is divisible by any of the smaller primes
            for x in primes:
                if a % x == 0:
                    p = False           # ...unless it isn't
                    break


def squares(n):
    count = 0
    while count < n:
        yield count ** 2
        count += 1


def squares2(n):
    for count in range(n):
        yield count ** 2





