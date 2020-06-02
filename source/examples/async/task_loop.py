#!/usr/bin/env python3

"""
Example code for making the very simplest event loop possible

Inspired by Brett Cannon's "How the heck does async/await work in Python 3.5?":

https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5

and André Caron's "A tale of event loops":

https://github.com/AndreLouisCaron/a-tale-of-event-loops

I'm calling this a "task loop" rather than an event loop, because it really is
only designed to run a bunch of tasks asynchronously, wohtout the other
machinery required to support proper events -- like a way to generate a new
event, for instance.
"""



