"""
    Title: pytech_delete.py
    Author: Keegan Jones
    Date: 2/7/2021
    Description: Test program for deleting documents from the pytech collection
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

# MongoDB: insert_one() method to insert document data into a collection
test_doc = {
    "student_id": "1010",
    "first_name": "Nellie",
    "last_name": "Jones",
}
test_doc_id = students.insert_one(test_doc).inserted_id

# display message 
print("\n  -- DISPLAYING STUDENT TEST DOC --")

# MongoDB: find_one() method to display a single document by student_id
student_test_doc = mydb.students.find_one({"student_id": "1010"})

print("\nStudent ID: " + student_test_doc["student_id"])
print("First Name: " + student_test_doc["first_name"])
print("Last Name: " + student_test_doc["last_name"])

# MongoDB: delete_one() method to delete a single document by student_id
deleted_student_test_doc = mydb.students.delete_one({"student_id": "1010"})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# MongoDB: find() method to display all documents in the collection 
new_student_list = mydb.students.find({})
for doc in new_student_list:
    

    print("\nStudent ID: " + doc["student_id"])
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc["last_name"])

# exit message
input("\n End of program, press any key to continue... ")



