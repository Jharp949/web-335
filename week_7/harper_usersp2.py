"""
  Title: harper_usersp2.py
  Author: James Harper
  Date: 24 September 2023
  Description: Python with MongoDB
"""

""" import the MongoClient """
from pymongo import MongoClient
import datetime

""" build a connection string to connect to """
client = MongoClient("mongodb+srv://web335_user:s3cret@users.bdi2lit.mongodb.net/web335DBretryWrites=true&w=majority")

""" configure a variable to access the web335DB """
db = client['web335DB']

""" Create a new user document in MongoDB """
db.users.insert_one({
    "firstName": "Igor",
    "lastName": "Stravinsky",
    "employeeId": "1014",
    "email": "stravi@me.com",
    "dateCreated": datetime.datetime.now()
})

""" Shows the new document has been created """
print(db.users.find_one({"employeeId": "1014"}))

""" Modify the e-mail address in the newly created document """
db.users.update_one(
    {"email": "stravi@me.com"},
    {"$set": {"email": "stravinsky@me.com"}}
)

""" Shows that the e-mail address has been modified """
print(db.users.find_one({"email": "stravinsky@me.com"}))

""" Deletes the created document """
db.users.delete_one({"employeeId": "1014"})

""" Shows that the document has been deleted """
print(db.users.find_one({"employeeId": "1014"}))