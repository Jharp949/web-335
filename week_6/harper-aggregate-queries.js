/*
    Title: harper-aggregate-queries
    Author: James Harper
    Date: 16 September 2023
    Description: MongoDB shell to build and execute queries
*/

    //Query to find all documents within houses.js
    db.houses.find({})

    //Query for a list of documents within the students collection
    db.students.find({})

    //Query to add a documents to the students collection
    db.students.insertOne({"firstName": "Hermoine", "lastName": "Granger", "studentId": "s1019", "houseId": "h1007"})

    //Query to find the document that was added
    db.students.find({"lastName": "Granger"})

    //Query to delete the document that was added
    db.students.deleteOne({"lastName": "Granger"})

    //Query to verify the document was deleted
    db.students.find({"lastName": "Granger"})

    //Query to find documents for students base on house
    db.houses.aggregate( [ { $lookup : { from: "students", localField: "houseId", foreignField: "houseId", as: "students" } } ] )

    //Query to find all students in house Gryffindor
    db.houses.aggregate( [ { $lookup : { from: "students", localField: "houseId", foreignField: "houseId", as: "students" } },
    { $match: {"mascot": "Lion"}} ] )

    //Query to find all students with an Eagle mascot
    db.houses.aggregate( [ { $lookup : { from: "students", localField: "houseId", foreignField: "houseId", as: "students" } },
    { $match: {"mascot": "Eagle"}} ] )
