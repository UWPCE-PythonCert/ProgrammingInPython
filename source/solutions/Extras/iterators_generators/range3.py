#!/usr/bin/env python

"""
a re-implementation of the built-in range object

range is also a sequence -- it can be indexed, so we could implement it
that way.

remember that a sequence that indexes from 0 is also a iterable

This is that version
"""

# the index method takes an object and returns its index equivalent.
from operator import index


class range3:
    def __init__(self, start, stop=None, step=1):
        # some logic to handle the optional parameters
        # if stop is None and step is None:
        if step == 0:
            raise ValueError("range() arg 3 must not be zero")
        if stop is None:
            stop = start
            start = 0
        self.start = index(start)
        self.stop = index(stop)
        self.step = index(step)

    def __getitem__(self, ind):
        ind = index(ind)
        val = self.start + (self.step * ind)
        if self.step > 0 and val < self.stop:
            return val
        elif self.step < 0 and val > self.stop:
            return val
        raise IndexError
