"""
   Title: pytech_update.py
   Author: Keegan Jones
   Date: 2/7/2021
   Description: Test program for updating a document in the pytech collection
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
    

    print("\nStudent ID: " + doc["student_id"])
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc["last_name"])

result = mydb.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Adams"}})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

doc = mydb.students.find_one({"student_id": "1007"})

print("Student ID: " + doc["student_id"])
print("First Name: " + doc["first_name"])
print("Last Name: " + doc["last_name"])

#exit message
input("\n\n End of program, press any key to continue... ")