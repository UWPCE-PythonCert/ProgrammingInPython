#!/usr/bin/env python

"""
Simple async example derived from python docs.

Will only work on Python 3.5 and above
"""

import asyncio
import time
import datetime
import random


# using "async" makes this a coroutine:
# its code can be run by the event loop
async def display_date(num):
    end_time = time.time() + 10.0  # we want it to run for 10 seconds.
    while True:  # keep doing this until break
        print("instance: {} Time: {}".format(num, datetime.datetime.now()))
        if (time.time()) >= end_time:
            print("instance: {} is all done".format(num))
            break
        # pause for a random amount of time
        await asyncio.sleep(random.randint(0, 3))


def shutdown():
    print("shutdown called")
    # you can access the event loop this way:
    loop = asyncio.get_event_loop()
    loop.stop()


# You register "futures" on the loop this way:
asyncio.ensure_future(display_date(1))
asyncio.ensure_future(display_date(2))

loop = asyncio.get_event_loop()

# or add tasks to the loop like this:
loop.create_task(display_date(3))
loop.create_task(display_date(4))
for i in range(5, 20):
    loop.create_task(display_date(i))

# this will shut the event loop down in 15 seconds
loop.call_later(15, shutdown)

print("about to run loop")
# this is a blocking call
loop.run_forever()
print("loop exited")

