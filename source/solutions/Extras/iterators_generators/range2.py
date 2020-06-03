#!/usr/bin/env python

"""
a re-implementation of the built-in range object

Not that there is any reason to do so, but it is a good
exercise in understanding the iterator protocol
"""

from operator import index

class range2:
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

    def __iter__(self):
        # reset when __iter__ is called
        print("iter called", self.start, self.stop, self.step)
        if self.step < 0:
            self.current = self.start - self.step
        else:
            self.current = self.start - self.step
        print(self.current)
        return self

    def __next__(self):
        try:
            self.current += self.step
        except AttributeError:
            raise TypeError('MyRange object is not an iterator -- it is an "iterable"\n'
                            'That is, iter() needs to be called on it to obtain an iterator')
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.current <= self.stop:
            raise StopIteration
        else:
            return self.current
