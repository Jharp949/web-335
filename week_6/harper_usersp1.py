"""
  Title: harper_usersp1.py
  Author: James Harper
  Date: 16 September 2023
  Description: Python with MongoDB
"""

""" import the MongoClient """
from pymongo import MongoClient

""" build a connection string to connect to """
client = MongoClient("mongodb+srv://web335_user:s3cret@users.bdi2lit.mongodb.net/web335DBretryWrites=true&w=majority")

""" configure a variable to access the web335DB """
db = client['web335DB']

""" call the find function to display all user documents """
users = (db.users.find({}))

for user in users:
  print(user)
  
print(users)

""" call the find_one function to display a user document by employeeId """
print(db.users.find_one({"employeeId": "1011"}))

""" call the find_one function to display a user document by lastName """
print(db.users.find_one({"lastName": "Mozart"}))