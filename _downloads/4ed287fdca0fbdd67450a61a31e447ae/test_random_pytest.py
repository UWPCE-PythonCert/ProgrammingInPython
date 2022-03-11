#!/usr/bin/env python

"""
port of the random unit tests from the python docs to py.test
"""

import random
import pytest


example_seq = list(range(10))


def test_choice():
    """
    A choice selected should be in the sequence
    """
    element = random.choice(example_seq)
    assert (element in example_seq)


def test_sample():
    """
    All the items in a sample should be in the sequence
    """
    for element in random.sample(example_seq, 5):
        assert element in example_seq


def test_shuffle():
    """
    Make sure a shuffled sequence does not lose any elements
    """
    seq = list(range(10))
    random.shuffle(seq)
    seq.sort()  # If you comment this out, it will fail, so you can see output
    print("seq:", seq)  # only see output if it fails
    assert seq == list(range(10))


def test_shuffle_immutable():
    """
    Trying to shuffle an immutable sequence raises an Exception
    """
    with pytest.raises(TypeError):
        random.shuffle((1, 2, 3))


def test_sample_too_large():
    """
    Trying to sample more than exist should raise an error
    """
    with pytest.raises(ValueError):
        random.sample(example_seq, 20)
