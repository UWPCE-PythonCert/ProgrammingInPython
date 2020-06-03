#!/usr/bin/env python

"""
Example of how to save data in a shelf

"""

import shelve


# get the data from the py file
from add_book_data import AddressBook

outfilename = "add_book_data.shelve"

# since we can put a whole dict on a shelf:
shelf = shelve.open(outfilename, 'n')

for person in AddressBook:
    # create a key:
    key = "%(first_name)s%(last_name)s" % person
    shelf[key] = person

shelf.close()

# see if we can re-load it
shelf2 = shelve.open(outfilename)

AddressBook2 = [person for person in shelf2.values()]
# note -- there could be an issue with order here.
#         so:
# These are lists of dicts -- and dicts are not orderable
#   so we stringify them to get something orderable
AddressBook.sort(key=str)
AddressBook2.sort(key=str)

if AddressBook2 == AddressBook:
    print("shelved/unshelved version is the same as the original")
