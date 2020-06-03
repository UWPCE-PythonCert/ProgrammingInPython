#!/usr/bin/env python

"""
Simple timing context manager

NOTE: this is only good for crude timing
-- use the timeit module for more accurate timing.
"""

import sys
import time


class Timer:
    def __init__(self, outfile=sys.stdout, name=""):
        self.outfile = outfile
        self.name = " for " + name if name else ""

    def __enter__(self):
        self.start = time.clock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.clock() - self.start
        self.outfile.write("Elapsed time{}: {:3g} seconds\n".format(self.name, elapsed))


if __name__ == "__main__":
    # Examples of how to use it

    # simplest
    with Timer():
        sum(range(100))

    # giving a name to your block of code:
    with Timer(name="very important code"):
        sum(range(30000))

    # sending it to a file:
    with open("log.txt", 'a') as log:
        with Timer(outfile=log, name="very important code"):
            sum(range(30000))

    # sending it to a file nested:
    with open("log.txt", 'a') as log, Timer(outfile=log, name="very important code"):
        sum(range(20000))
