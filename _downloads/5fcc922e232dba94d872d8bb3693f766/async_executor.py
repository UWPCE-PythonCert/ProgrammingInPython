#!/usr/bin/env python

"""
An example of runing a blocking task in an Executor:
"""

import asyncio
import time
import datetime
import random


async def small_task(num):
    """
    Just something to give us little tasks that run at random intervals
    These will go on forever
    """
    while True:  # keep doing this until break
        print("task: {} run".format(num))
        # pause for a random amount of time between 0 and 2 seconds
        await asyncio.sleep(random.random() * 2)

async def slow_task():
    while True:  # keep going forever
        print("running the slow task- blocking!")
        # This will block for 2-10 seconds!
        # result = slow_function(random.random() * 8 + 2)
        # uncomment to put it on a different thread:
        # result = slow_function(random.random() * 8 + 2)
        result = await loop.run_in_executor(None,
                                           slow_function,
                                           random.random() * 8 + 2)
        print("slow function done: result", result)
        # await asyncio.sleep(0.0)  # to release the loop


def slow_function(duration):
    """
    this is a fake function that takes a long time, and blocks
    """
    time.sleep(duration)
    print("slow task complete")
    return duration


# get a loop going:
loop = asyncio.get_event_loop()

# or add tasks to the loop like this:
loop.create_task(small_task(1))
loop.create_task(small_task(2))
loop.create_task(small_task(3))
loop.create_task(small_task(4))

# Add the slow one
loop.create_task(slow_task())

print("about to run loop")
# this is a blocking call
# we will need to hit ^C to stop it...
loop.run_forever()
print("loop exited")
