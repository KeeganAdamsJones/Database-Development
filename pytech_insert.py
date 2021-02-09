"""
    Title: pytech_insert.py
    Author: Keegan Jones
    Date: 2/7/2021
    Description: Test program for inserting new documents into the students collection.
"""

# Import pymongo so that Python and MongoDB can talk
import pymongo

# use this to access the database get this url from mongodb "connect your application"
myclient = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.jzgv5.mongodb.net/csd?retryWrites=true&w=majority')

# access the database titled "pytech" and the collection called "students"
mydb = myclient["pytech"]
students = mydb["students"]

#### Three students documents ###
# MongoDB: insert_one() method to insert document data into a collection

# Keegan Jones' data document
keegan = {
    "student_id": "1007",
    "first_name": "Keegan",
    "last_name": "Jones",
    "enrollments": [
      {
        "term": "fall 2020",
        "gpa": "3.8",
        "start_date": "8/15/2020",
        "end_date": "12/15/2020",
        "courses": [
          {
            "course_id": "csd210",
            "description": "intro to programming",
            "instructor": "joe professional",
            "grade": "A"
          },
          {
            "course_id": "csd220",
            "description": "programming with python",
            "instructor": "jane smart",
            "grade": "A"
          }
        ]
      },
      {
        "term": "spring 2021",
        "gpa": "4.0",
        "start_date": "1/7/2021",
        "end_date": "5/15/2021",
        "courses": [
          {
            "course_id": "csd310",
            "description": "intro to databases",
            "instructor": "joe professional",
            "grade": "A"
          },
          {
            "course_id": "csd320",
            "description": "programming with java",
            "instructor": "jane smart",
            "grade": "A"
          }
        ]
      }
    ]

}


# William Adams' data document #
william = {
    "student_id": "1008",
    "first_name": "William",
    "last_name": "Adams",
    "enrollments": [
      {
        "term": "fall 2020",
        "gpa": "3.2",
        "start_date": "8/15/2020",
        "end_date": "12/15/2020",
        "courses": [
          {
            "course_id": "csd210",
            "description": "intro to programming",
            "instructor": "joe professional",
            "grade": "B"
          },
          {
            "course_id": "csd220",
            "description": "programming with python",
            "instructor": "jane smart",
            "grade": "A"
          }
        ]
      },
      {
        "term": "spring 2021",
        "gpa": "3.9",
        "start_date": "1/7/2021",
        "end_date": "5/15/2021",
        "courses": [
          {
            "course_id": "csd310",
            "description": "intro to databases",
            "instructor": "joe professional",
            "grade": "A"
          },
          {
            "course_id": "csd320",
            "description": "programming with java",
            "instructor": "jane smart",
            "grade": "A"
          }
        ]
      }
    ]
}
 

# Amber Andrasek's Data Document #
amber = {
    "student_id": "1009",
    "first_name": "Amber",
    "last_name": "Andrasek",
    "enrollments": [
      {
        "term": "fall 2020",
        "gpa": "3.9",
        "start_date": "8/15/2020",
        "end_date": "12/15/2020",
        "courses": [
          {
            "course_id": "csd210",
            "description": "intro to programming",
            "instructor": "joe professional",
            "grade": "A"
          },
          {
            "course_id": "csd220",
            "description": "programming with python",
            "instructor": "jane smart",
            "grade": "A"
          }
        ]
      },
      {
        "term": "spring 2021",
        "gpa": "3.7",
        "start_date": "1/7/2021",
        "end_date": "5/15/2021",
        "courses": [
          {
            "course_id": "csd310",
            "description": "intro to databases",
            "instructor": "joe professional",
            "grade": "B"
          },
          {
            "course_id": "csd320",
            "description": "programming with java",
            "instructor": "jane smart",
            "grade": "A"
          }
        ]
      }
    ] 
}

# insert statements with output
print("\n  -- INSERT STATEMENTS --") 

keegan_student_id = students.insert_one(keegan).inserted_id
print("Inserted student record Keegan Jones into the student collection with document id",keegan_student_id);

william_student_id = students.insert_one(william).inserted_id
print("Inserted student record William Adams into the student collection with document id",william_student_id);

amber_student_id = students.insert_one(amber).inserted_id
print("Inserted student record Amber Andrasek into the student collection with document id",amber_student_id);

input("\n\n End of program, press any key to exit... ")
