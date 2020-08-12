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

import random
import trigrams

IWISH = words = "I wish I may I wish I might".split()

def test_trigrams_pairs():
    """
    test that the build_trigram function creates the right pairs of words
    """
    tris = trigrams.build_trigram(IWISH)

    pairs = tris.keys()

    # using a set here, as the dict_keys object is a set as well
    # And keys are always unique and hashable
    # and the order does not matter, so perfect for a set
    assert pairs == {("I", "wish"),
                     ("wish", "I"),
                     ("may", "I"),
                     ("I", "may"),
                     }


def test_trigrams_following_words():
    """
    test that the following words are correct
    """
    tris = trigrams.build_trigram(IWISH)

    # this will only print if the test fails
    # but if if does, you can see what's going on to try to fix it.
    print(tris)

    # a separate assert for each pair:
    assert tris[("I", "wish")] == ["I", "I"]
    assert tris[("wish", "I")] == ["may", "might"]
    assert tris[("may", "I")] == ["wish"]
    assert tris[("I", "may")] == ["I"]


def test_pick_random_pair():
    test_pairs = {("one", "two"): [],
                  ("one", "three"): [],
                  ("four", "five"): [],
                  ("six", "seven"): [],
                  ("eight", "nine"): [],
                  }
    # set the seed so we'll always get the same one
    random.seed(1234)
    pair = trigrams.pick_random_pair(test_pairs)

    assert pair == ('six', 'seven')



