""" 
    Title: pytech_queries.py
    Author: Tristan Boetcher
    Date: 4/10/22
    Description: Test program for querying the students collection.
"""

"""import statements"""
from pymongo import MongoClient

# connection string
url = "mongodb+srv://admin:admin@cluster0.v9e5p.mongodb.net/pytech?retryWrites=true&w=majority";

# connect to cluster
client = MongoClient(url)

# connect pytech database
db = client.pytech

print('-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')

# loop over the collection and output all students
student_docs = db.students.find()
for s in student_docs:
    print('Student ID: {0}\nFirst Name: {1}\nLast Name: {2}\n'.format(s['student_id'],
        s['first_name'], s['last_name']))



print('\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --')

# find document and one student displayed
student_doc = db.students.find_one({'student_id': 1008})
print('Student ID: {0}\nFirst Name: {1}\nLast Name: {2}\n'.format(student_doc['student_id'],
        student_doc['first_name'], student_doc['last_name']))

# End program
input('\n\nEnd of program, press any key to exit... ')
