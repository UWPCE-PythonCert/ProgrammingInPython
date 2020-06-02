#!/usr/bin/env python

"""
simplest possible example of using aiohttp client

from docs
"""

import asyncio
import aiohttp

async def get_events():
    async with aiohttp.ClientSession() as session:
        print("created a session")
        async with session.get('https://api.github.com/events',
                               ) as resp:
            print("status: resp.status")
            print(await resp.json())

loop = asyncio.get_event_loop()
loop.run_until_complete(get_events())
loop.close()




