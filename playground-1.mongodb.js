/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("sample_restaurants");

// Find a document in a collection.
db.getCollection("restaurants").findOne({

});

//This query is giving the collection of restaurants with all of its properties.
db.restaurants.find();

// Here we are looking for some specific documents of the restuarant that we need to know.
db.restaurants.find({},{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1});

db.restaurants.find({},{"restaurant_id" : 1,"name":1,"borough":1,"cuisine" :1,"_id":0});
