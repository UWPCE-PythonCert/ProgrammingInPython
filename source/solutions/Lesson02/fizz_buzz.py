#!/usr/bin/env python

"""
Fizz Buzz examples -- from most straightforward, to most compact.
"""


# basic approach:
def fizzbuzz1(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def fizzbuzz1b(n):
    """
    Save one computation -- if it's a multiple of 3 and 5, it's a
    multiple of 15
    """
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def fizzbuzz2(n):
    """
    Why evaluate i%3 and i%5 twice?
    """
    for i in range(1, n + 1):
        msg = ''
        if not i % 3:
            msg += "Fizz"
        if not i % 5:
            msg += "Buzz"
        if msg:
            print(msg)
        else:
            print(i)


def fizzbuzz3(n):
    """
    Or print on one line...
    """
    for i in range(1, n + 1):
        if i % 3 == 0:
            print("Fizz", end="")
        if i % 5 == 0:
            print("Buzz", end="")
        elif i % 3: # have to somehow check if you need to print the number
            print(i, end="")
        print()


def fizzbuzz4(n):
    """
    use conditional expressions:
    """
    for i in range(1, n + 1):
        msg = "Fizz" if i % 3 == 0 else ''
        msg += "Buzz" if i % 5 == 0 else ''
        print(msg or i)


def fizzbuzz5(n):
    """
    a one liner
    """
    for i in range(1, n + 1): print (("Fizz" * (not (i % 3)) + "Buzz" * (not (i % 5))) or i)


if __name__ == "__main__":
    fizzbuzz1(16)
    print()
    fizzbuzz2(16)
    print()
    fizzbuzz3(16)
    print()
    fizzbuzz4(16)
    print()
    fizzbuzz4(16)
    print()
