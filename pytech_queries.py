"""
    Title: pytech_queries.py
    Author: Keegan Jones
    Date: 2/7/2021
    Description: Test program for querying the students collection.
"""

# import pymongo so that python and mongo can talk to eachother
import pymongo 

# use this to access the database get this url from mongodb "connect your application"
myclient = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.jzgv5.mongodb.net/csd?retryWrites=true&w=majority')

# access the database titled "pytech" and the collection called "students"
mydb = myclient["pytech"]
students = mydb["students"]

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# MongoDB: find() method to display all documents in the collection 
student_list = mydb.students.find({})
for doc in student_list:

    print("Student ID: " + doc["student_id"])
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc["last_name"])
    print("\n")

# display message 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() Query --")

# MongoDB: find_one() method to display a single document by student_id
jones = mydb.students.find_one({"student_id": "1007"})

print("Student ID: " + doc["student_id"])
print("First Name: " + doc["first_name"])
print("Last Name: " + doc["last_name"])
print("\n")

# exit message
input("\n\n End of program, press any key to continue... ")