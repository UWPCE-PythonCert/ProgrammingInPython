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

IWISH = "I wish I may I wish I might".split()

LONGER_TEXT = """I was seized with a keen desire to see Holmes
again and to know how he was employing his extraordinary powers
His rooms were brilliantly lit and even as I looked up I saw
his tall spare figure pass twice in a dark silhouette against
the blind""".split()


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
                  ("two", "three"): [],
                  ("four", "five"): [],
                  ("six", "seven"): [],
                  ("eight", "nine"): [],
                  }
    # set the seed so we'll always get the same one
    random.seed(1234)
    pair = trigrams.pick_random_pair(test_pairs)
    print("the pair is:", pair)
    assert pair == ('six', 'seven')


def test_get_last_pair():
    words = ["this", "that", "the", "other"]

    assert trigrams.get_last_pair(words) == ("the", "other")


def test_get_random_follower():
    """
    test getting a random word from the trigrams dict
    """
    # we only need one entry for this test
    tri_dict = {("one", "two"): ["four", "five", "six", "seven"]}

    # set the seed so the answer will be consistent
    random.seed(1234)
    word = trigrams.get_random_follower(tri_dict, ("one", "two"))
    print("got word:", word)
    assert word == "seven"


def test_get_random_follower_not_there():
    """
    test what happens when the word pair is not there
    """
    # we only need one entry for this test
    tri_dict = {("one", "two"): ["four", "five", "six", "seven"]}

    # here's a word pair that isn't there
    # make sure you get something back!
    word = trigrams.get_random_follower(tri_dict, ("one", "one"))
    print("got word:", word)
    assert word  # this asserts that you got a non-empty string


def test_make_sentence():
    """
    test making a trigrams sentence

    as it is supposed to be random, this tests for things other than
    the actual results.

    NOTE that this test relies on the build_trigram() function, so it
         will fail if that doesn't work.
    """

    # reset the seed, sop that we won't always get the same answer
    random.seed()

    # use the already tested build_trigram function to make the dict
    tri_dict = trigrams.build_trigram(LONGER_TEXT)


    # make a sentence of 6 words
    sentence = trigrams.make_sentence(tri_dict, 6)

    print(sentence)
    # check that it has 6 words
    assert len(sentence.split()) == 6
    # check that the first letter is a capital
    assert sentence[0] == sentence[0].upper()
    # check that it ends with a period
    assert sentence[-1] == "."
    # check that there is not a space between the period and the last word.
    assert not sentence[-2].isspace()

# the following tests are for the "make_words" function,
# which takes a text string, and returns a list of words
# It also cleans up the punctuation, while preserving things
# like apostrophes, and capitalized "I".
# you may choose to handle punctuation differently
# feel free to adapt the tests to your choices


TEXT_WITH_PUNC = """
One night--it was on the twentieth of March, 1888--I was
returning from a journey to a patient (for I had now returned to
civil practice), when my way led me through Baker Street. As I
passed the well-remembered door, which must always be associated
in my mind with my wooing, and with the dark incidents of the
Study in Scarlet, I was seized with a keen desire to see Holmes
again, and to know how he was employing his extraordinary powers.
His rooms were brilliantly lit, and, even as I looked up, I saw
his tall, spare figure pass twice in a dark silhouette against
the blind.
"""


def test_make_words_simple():
    """
    make sure the basics work!
    """
    all_words = trigrams.make_words("A really simple sentence.")

    assert len(all_words) == 4


def test_make_words_commas():
    """
    all commas should be removed
    """
    # put them all back together for easier checking
    all_words = " ".join(trigrams.make_words(TEXT_WITH_PUNC))

    assert "," not in all_words


def test_make_words_parentheses():
    """
    all parenthesis should be removed
    """
    # put them all back together for easier checking
    all_words = " ".join(trigrams.make_words(TEXT_WITH_PUNC))

    assert "(" not in all_words
    assert ")" not in all_words


def test_make_words_dashes():
    """
    all dashes should be removed
    """
    # put them all back together for easier checking
    all_words = " ".join(trigrams.make_words(TEXT_WITH_PUNC))

    assert "-" not in all_words


def test_make_words_I():
    """
    I should be capitalized
    """
    all_words = trigrams.make_words(TEXT_WITH_PUNC)

    assert "i" not in all_words
    assert "I" in all_words


def test_make_words_single_quote():
    """
    no double quotes
    no single quotes by themselves, but preserved when an apostrophe
    """
    # put them all back together for easier checking
    text = """
    "Not at all. The 'G' with the small 't' stands for
    'Gesellschaft,' which isn't the German for 'Company.'
    """
    all_words = trigrams.make_words(text)

    print(all_words)
    #  no double quotes
    assert '"' not in " ".join(all_words)
    # apostophe preserved
    assert "isn't" in all_words

    # none of the words should start or end with a single quote
    for word in all_words:
        assert not word.startswith("'")
        assert not word.endswith("'")

    assert False


