#!/usr/bin/env python

"""
Example of how to save data using the anydbm package
"""

# get the data from the py file
# csv format really only holds flat data well.
from add_book_data_flat import AddressBook

import dbm

outfilename = "add_book_data.dbm"


# Note that dbm files are really only good for simple key-value storage
#   so let's just do one record:
person = AddressBook[0]

# create a dbm  file writing object
db = dbm.open(outfilename, 'n')

# write the data:
for key, value in person.items():
    db[key] = value

# close the file
db.close()

# see if it can be re-loaded.

# open an existing dbm file
db = dbm.open(outfilename, 'r')

# read the data:
person = {}
for key in db.keys():
    # note: pretty ugly -- dbm only stores bytes!
    person[key.decode()] = db.get(key).decode()

# Check if they are the same
if person == AddressBook[0]:
    print("db version is the same as the original")
else:
    print("db version didn't match!")
    print(person)

# Storing multiple people:
#    building up a key

# left as an exercise for the reader....
