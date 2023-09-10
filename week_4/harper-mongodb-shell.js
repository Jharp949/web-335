/*
    Title: harper-mongodb-shell
    Author: James Harper
    Date: 2 September 2023
    Description: MongoDB shell to build and execute queries
*/

//Write a query to display all objects stored in the users collection
db.users.find()

//Write a query to display a user with the email of jbach@me.com
db.users.findOne({"email": "jbach@me.com"})

//Write a query to display a user with the last name of Mozart
db.users.findOne({"lastName": "Mozart"})

//Write a query to display a user with the first name of Richard
db.users.findOne({"firstName": "Richard"})

//Write a query to display a user with the employeeId of 1010
db.users.findOne({"employeeId": "1010"})