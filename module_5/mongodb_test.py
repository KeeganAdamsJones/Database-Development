# Title: mongodb_test.py
# Author: Keegan Jones
# Date: 2/15/2021
# Description: Test program for connecting to a MongoDB Atlas Cluster



# Import statement
from pymongo import MongoClient

# MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.jzgv5.mongodb.net/pytech?retryWrites=true&w=majority"

# Connect to the MongoDB cluster
client = MongoClient(url)

# Connect to the PyTech database
db = client.pytech

# Display the connected collections
print("--Pytech Collection List--")
print(db.list_collection_names())

# Display exit message
input("\n\n  End of program, press any key to exit... ")