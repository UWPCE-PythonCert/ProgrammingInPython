#!/usr/bin/env python

"""
test code for the "trigrams" exercise

NOTE: This is NOT a complete set of tests! You will want to add more of
      your own to get complete coverage.

As you develop your code, if you are about to add a feature, or think
of an edge case:

    Write a new test for that first!

Also note that you may want to do some different things with processing
the text -- if so, then update the tests (and add more) to reflect how you want your code to work.
"""

# this is expecting a "trigrams.py" file with your code in it.

import trigrams

IWISH = ["I", "wish", "I", "may", "I", "wish", "I", "might"]


def test_trigrams_keys():
    """
    test that the build_trigram function creates the right pairs of words
    """
    tris = trigrams.build_trigram(IWISH)

    pairs = list(tris.keys())

    pairs = pairs.sort()

    assert pairs == {("I", "wish"),
                    ("wish", "I"),
                    ("may", "I"),
                    ("I", "may"),
                    }


