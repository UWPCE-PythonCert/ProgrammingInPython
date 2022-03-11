#!/usr/bin/env python3

"""
examples / test code for __getindex__

Doesn't really do anything, but you can see what happens with different indexing.
"""

import operator


class IndexTest:

    def __getitem__(self, index):
        # print("In getindex, indexes is:", index)
        if isinstance(index, slice):
            print("it's a single slice:", index)
        elif isinstance(index, tuple):
            print("it's a multi-dimensional slice:", index)
        else:
            try:
                ind = operator.index(index)  # this converts arbitrary objects to an int.
                print("it's an index: ", ind)
            except TypeError:  # not a simple index
                raise
            print("It's a simple index")


if __name__ == "__main__":

    it = IndexTest()

    print("calling with simple index")
    it[4]

    print("calling with single slice")
    it[3:4]

    print("calling with two slices")
    it[3:4, 7:8]

    print("calling with an invalid index")
    it["this"]







