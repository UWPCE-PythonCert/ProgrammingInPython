#!/usr/bin/env python

"""
String formatting lab:

This version using "old style" formatting

Still pretty handy, and while less flexible, also a bit simpler
"""

# Write a format string that will take the tuple:
#     (2, 123.4567, 10000, 12345.67)
#     and produce:
#     'file_002 :   123.46, 1.00e+04, 1.23e+04'


t = (2, 123.4567, 10000, 12345.67)
print("file_%03i : %10.2f, %.2e, %.3g" % t)
print()

# Note the subtle differnce between the 'e' and 'g' formatting strings.
#      I like 'g' -- it does significant figures.


# Rewrite: "the first 3 numbers are: %i, %i, %i"%(1,2,3)
#          for an arbitrary number of numbers...

# solution 1
# the goal was to demonstrate dynamic building of format strings:

# create the numbers
numbers = [32, 56, 34, 12, 48, 18]

# build the format string for the numbers:
formatter = ("%i, " * len(numbers))[:-2]  # take the extra comma and space off the end

# or use join():
#formatter = ", ".join(["%i"] * len(numbers))

# put it together with the rest of the string
formatter = "the first %i numbers are: %s" % (len(numbers), formatter)

# use it:
# the format operator needs a tuple
# tuple(seq) will make a tuple out of any sequence
print(formatter % tuple(numbers))

