#!/usr/bin/env python

"""
Example of how to save data as an CSV file with the CSV module
"""

# get the data from the py file
# csv format really only holds flat data well.
from add_book_data_flat import AddressBook

import csv

outfilename = "add_book_data.csv"

# create a csv file writing object
writer = csv.writer(open(outfilename, 'w'))

# write the headers
# assume all data have the same keys
headers = AddressBook[0].keys()
writer.writerow(headers)

for person in AddressBook:
    row = [person[key] for key in headers]
    writer.writerow(row)

del writer  # to make sure the file gets closed

# see if it can be re-loaded.

# create a csv file reading object
reader = csv.reader(open(outfilename, 'r'))

# read  the headers
# it's an iterator -- so next() gives us the next row -- in this case, the first row
headers = next(reader)

# build up the new version:
AddressBook2 = []
for row in reader:
    AddressBook2.append(dict(zip(headers, row)))

del reader  # to make sure the file is closed

# Check if they are the same
if AddressBook2 == AddressBook:
    print("csv reader version is the same as the original")
else:
    print("csv read version is NOT the same")

# or use the built-in "DictReader":
# create a DictReader file reading object
reader = csv.DictReader(open(outfilename, 'r'))
# no need to read  the headers -- it will use the first row

# build up the new version:
AddressBook3 = []
for row in reader:
    print("row:", row)
    AddressBook3.append(row)

del reader  # to make sure the file is closed

# Check if they are the same
if AddressBook3 == AddressBook:
    print("The DictReader one is the the same")
else:
    print("The DictReader one is NOT the same!")
