#!/usr/bin/env python3

"""
doing all of fizzbuzz in a comprehension

Is this a good idea?
 -- probably not, but it's kind of cool

 Note that it uses a generator comprehension, so it won't actually get
 computed until the join() call
"""

fb = ([str(i), 'Fizz', 'Buzz', 'FizzBuzz'][(i % 3 == 0) + 2 * (i % 5 == 0)] for i in range(1, 101))

print('\n'.join(fb))
