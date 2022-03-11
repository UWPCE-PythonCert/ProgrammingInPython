#!/usr/bin/env python

import pathlib


def file_yielder(dir=".", pattern="*"):
    """
    iterate over all the files that match the pattern

    pattern us a "glob" pattern, like: *.py
    """
    for filename in pathlib.Path(dir).glob(pattern):
        with open(filename) as file_obj:
            yield file_obj
