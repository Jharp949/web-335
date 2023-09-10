/*
    Title: harper-projections
    Author: James Harper
    Date: 10 September 2023
    Description: MongoDB shell to build and execute queries
*/

//Write a query to display all objects stored in the users collection
db.users.find()

//Adds a new composer object to the database
db.users.insertOne({"firstName": "Joseph", "lastName": "Hayden", "employeeId": "1013", "email": "jhayden@me.com", "dateCreated": new Date() })

//Updates the email address of the composer with the matching last name
db.users.updateOne({"lastName": "Mozart"}, {$set: {"email": "mozart@me.com"}})

//Displays the changes that have occurred during the session
db.users.aggregate( [ { $project : { "_id": 0, "firstName": 1 , "lastName": 1, "email": 1 } } ] )