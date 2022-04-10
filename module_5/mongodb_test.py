"""
    Title: mongodb_test.py
    Author: Tristan Boetcher
    Date 4/10/22
    Description: Test program for connecting to a 
                 MongoDB Atlas Cluster
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.qxtd6.mongodb.net/pytech"

# connect to the MongoDB cluster
client = MongoClient(url)

# connect pytech database
db = client.pytech

# show the connected collections
print("\n -- Pytech COllection List --")
print(db.list_collection_names())

# show an exit message
input("\n\n  End of program, press any key to exit... ")
