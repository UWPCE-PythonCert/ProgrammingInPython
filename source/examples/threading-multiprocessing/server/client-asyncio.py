#!/usr/bin/env python3

# TODO: update this with async / await

import os
import sys
from urllib.request import urlopen
import asyncio

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# from decorators.decorators import timer

# @timer

results = asyncio.Queue()

url = "http://localhost:37337"


@asyncio.coroutine
def producer():
    conn = urlopen(url)
    result = conn.read()
    return result


@asyncio.coroutine
def worker():
    result = yield from producer()
    results.put(result)


loop = asyncio.get_event_loop()

number_of_requests = 100

for i in range(number_of_requests):
    loop.run_until_complete(worker())

print("made %d requests" % number_of_requests)
