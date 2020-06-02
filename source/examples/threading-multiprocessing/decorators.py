#!/usr/bin/env python

import time


def timer(func):
    def timer(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        print("-- executed in %.4f seconds :" % (time.time() - t1))
        return result
    return timer


def logger(func):
    def logger(*args, **kwargs):
        print("\n\n-- calling function\n\n")
        func(*args, **kwargs)
        print("\n\n-- function call succeeded\n\n")
    return logger


def exception_handler(func):
    def handle_exceptions(*args, **kwargs):
        try:
            print("handling exceptions..")
            func(*args, **kwargs)
        except Exception as e:
            print("\n\n-- Received exception, logging message: %s\n\n" % str(e))
    return handle_exceptions
