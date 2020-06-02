#!usr/bin/env python

"""
simple test file for mongoDB
remember to start database: 
$ mongod --dbpath=mongo_data/

"""

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.test_database

collection = db.test_collection

chris = {'last_name':'Barker',
         'first_name':'Chris',
         'middle_name':'H',
         'cell_phone':'(123) 555-7890',
         'email':'PythonCHB@gmail.com',
         }

collection.insert(chris)

print("all the collections")
print(db.collection_names())

print(collection.find_one())
