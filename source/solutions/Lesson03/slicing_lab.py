#!/usr/bin/env python3

"""
One solution...
"""


def swap(seq):
    """with the first and last items exchanged"""
    return seq[-1:] + seq[1:-1] + seq[:1]


assert swap('something') == 'gomethins'
assert swap(tuple(range(10))) == (9, 1, 2, 3, 4, 5, 6, 7, 8, 0)


def rem(seq):
    """With every other item removed"""
    return seq[::2]


assert rem('a word') == 'awr'


def rem4(seq):
    """With the first and last 4 items removed, and every other item in between"""
    return seq[4:-4:2]


a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
print(rem4(a_tuple))
assert rem4(a_tuple) == (5, 7)


def reverse(seq):
    """With the elements reversed (just with slicing)"""
    return seq[::-1]


print(reverse('a string'))
assert reverse([3, 6, 1, 8, 3, 7]) == [7, 3, 8, 1, 6, 3]


def thirds(seq):
    """with the last third, then first third, then the middle third in the new order."""
    i = len(seq) // 3
    return seq[-i:] + seq[:i] + seq[i:-i]


print(thirds(tuple(range(12))))
assert thirds(tuple(range(12))) == (8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7)


