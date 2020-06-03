#!/usr/bin/env python

"""
String formatting lab:

This version using the format() method

"""

#####
# Write a format string that will take the tuple:
#     (2, 123.4567, 10000, 12345.67)
#     and produce:
#     'file_002 :   123.46, 1.00e+04, 1.23e+04'
#####

print("file_{:03d} : {:10.2f}, {:.2e}, {:.3g}".format(2, 123.4567, 10000, 12345.67))
print()
# Note the subtle differnce between the 'e' and 'g' formatting strings.
#      I like 'g' -- it does significant figures.

#######################
# Rewrite: "the 3 numbers are: %i, %i, %i"%(1,2,3)
#          for an arbitrary number of numbers...

# solution 1
# the goal was to demonstrate dynamic building of format strings:


def formatter(t):
    # The static part of the string
    fstring = "the {:d} numbers are: ".format(len(t))
    # This add the correct number of format specifiers:
    fstring += ", ".join(['{:d}'] * len(t))
    # The created string can be now applied to the tuple of numbers
    # * unpacks a sequence into the arguments of a function -- we'll get to that!
    return fstring.format(*t)


# call it with a couple different tuples of numbers:
print(formatter((2, 3, 5)))

print(formatter((2, 3, 5, 7, 9)))

# solution 2
# You may have realized that str() would make a nice string from
# a list or tuple
# perfectly OK to use that -- though it doesn't demonstrate how you can
# dynamically build up format strings, and then use them later...

numbers = (34, 12, 3, 56)

numbers_str = str(numbers)[1:-1]  # make a string, remove the brackets

# put it together with the rest of the string
print("the first {:d} numbers are: {}".format(len(numbers), numbers_str))

# answer to bonus question at the very end:
# And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly 
# print the tuple in columns that are 5 charaters wide? It can be done on one short line!
print(('{:<5}'*len(the_tuple)).format(*the_tuple))
