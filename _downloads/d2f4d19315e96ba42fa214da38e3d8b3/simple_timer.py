#!/usr/bin/env python

"""
Simple example of using a threading.Timer

NOTE: The docstring is out of sync with the __init__!
      I think it was inherited from the threading.Thread docstring.
"""

import threading
import time
import random


def called_once():
    """
    this function is designed to be be called once in the future
    """
    print("Hey! I just got called! It's now: {}".format(time.asctime()))


def called_later(count):
    """
    This function is designed to run, and then set up a timer to call
    itself at a random time in the future

    Note that it is limited to 10 invocations
    Otherwise, there will always be a background
    thread running that can not be easily killed
    (at least on *nix -- Windows may let ^C kill it)

    Try hitting ^C early in the run...
    """

    print("Hey! I just got called for {}th time! It's now: {}"
          .format(count, time.asctime()))
    # this can trigger another invocation
    interval = random.randint(1, 3)
    count += 1
    if count < 10:
        threading.Timer(interval=interval,
                        function=called_later,
                        args=(count,)).start()


if __name__ == "__main__":
    # use the timer...

    # threading.Timer(interval=3, function=called_once).start()
    # print("After starting the timer")
    # print("it's now: {}".format(time.asctime()))

    called_later(0)

    # do some stuff:
    for i in range(100):
        print("{}: nothing important...".format(i))
        time.sleep(0.5)




