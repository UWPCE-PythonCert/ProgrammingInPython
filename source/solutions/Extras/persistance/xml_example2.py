#!/usr/bin/env python

"""
Example of how to save data as xml, using the element tree module

This version uses the nested dataset, and does full-on nested XML
"""

import xml.etree.ElementTree as et
from indent_etree import indent  # for prettier output

# get the data from the py file
from add_book_data import AddressBook

outfilename = "add_book_data2.xml"

# build a tree structure
root = et.Element("address_book")

# add the elements:
for person in AddressBook:
    p = et.SubElement(root, "person")
    # This method stores everything as sub-elements
    for key, value in person.items():
        if type(value) == dict:
            address = et.SubElement(p, 'address')
            for sub_key, sub_value in value.items():
                sub_el = et.SubElement(address, sub_key)
                sub_el.text = sub_value
        else:
            el = et.SubElement(p, key)
            el.text = value

# wrap it in an ElementTree instance, and save as XML
tree = et.ElementTree(root)

indent(tree.getroot())  # to make it more pretty
tree.write(outfilename)

# See if we can re-load it
tree = et.parse(outfilename)
book = tree.getroot()
# re-build the original list:
AddressBook2 = []
for person in list(book):
    p = {}
    for sub_el in list(person):
        if sub_el.tag == "address":
            address = {}
            for sub_sub_el in sub_el.getchildren():
                t = sub_sub_el.text
                if t is None:  # etree returns None for empty tags!
                    address[sub_sub_el.tag] = ""
                else:
                    address[sub_sub_el.tag] = t
            p['address'] = address
        else:
            p[sub_el.tag] = sub_el.text
    AddressBook2.append(p)

if AddressBook2 == AddressBook:
    print("xml version is the same as the original")
else:
    print("xml version is not exactly the same as the original")
