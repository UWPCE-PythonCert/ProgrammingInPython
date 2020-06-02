#!/usr/bin/env python

"""
test of gather()

adapted from:

https://docs.python.org/3/library/asyncio-task.html

"""

import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(1)  # to simulate a longer process...
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(factorial("A", 2),
                                       factorial("B", 3),
                                       factorial("C", 4),
                                       ))
loop.close()
