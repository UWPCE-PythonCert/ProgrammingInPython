#!/usr/bin/env python

"""
Example of how to save (and reload) data as json
"""

import json

# get the data from the py file
from add_book_data import AddressBook

outfilename = "add_book_data.json"

# dump it as json (it's really this simple)
json.dump(AddressBook, open(outfilename, 'w'))

# specifying indent pretty-prints the json
# json.dump(AddressBook, open(outfilename, 'w'), indent=4)

# see if we can re-load it
AddressBook2 = json.load(open(outfilename, 'r'))

if AddressBook2 == AddressBook:
    print("json version is the same as the original")
