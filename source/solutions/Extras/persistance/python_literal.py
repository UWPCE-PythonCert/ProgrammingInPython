#!/usr/bin/env python

"""
Example of how to save data as python literals in a py file

"""

import pprint
from ast import literal_eval

# get the data from the py file
from add_book_data import AddressBook

outfilename = "add_book_data.pyliteral"


# save the data as python literals:
with open(outfilename, 'w') as outfile:
    outfile.write(repr(AddressBook))

# see if we can re-load it
data = open(outfilename, 'r').read()

# Warning, warning! danger Will Robinson!
# eval() is very dangerous!
AddressBook2 = eval(data)

if AddressBook2 == AddressBook:
    print("they are the same")

# try again with the pretty print version:

outfilename = "add_book_data.pyliteral_pretty"

with open(outfilename, 'w') as outfile:
    outfile.write(pprint.pformat(AddressBook))

# see if we can re-load it
data = open(outfilename, 'r').read()

# let's use literal_eval() this time:
AddressBook2 = literal_eval(data)

if AddressBook2 == AddressBook:
    print("pretty printed version is the same as well")
