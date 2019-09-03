from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bookSiteDB'
app.config["MONGO_URI"] = "mongodb+srv://dbAdmin:temporaryDevPassword@cluster0-9ekrc.mongodb.net/bookSiteDB?retryWrites=true&w=majority"

mongo = PyMongo(app)




@app.route("/")
def initResult():
   books=mongo.db.books.find().limit(10) 
   return render_template("home_page.html", books = books)


@app.route("/searchResult", methods=['GET', 'POST'])
def searchResult():
   searchTerm = request.args.get('search term')
   genre = request.args.get('genre')
   if searchTerm == "" and genre == "All genres":
      books=mongo.db.books.find().limit(7)
   elif searchTerm == "" and genre != "All genres":
      books=mongo.db.books.find({"Genre": genre}) 
   elif searchTerm != "" and genre == "All genres":
       mongo.db.books.create_index([('title', 'text')])
       books=mongo.db.books.find({"$text": {"$search": searchTerm }}) 
   else:
      mongo.db.books.create_index([('title', 'text')])
      books=mongo.db.books.find({"$text": {"$search": searchTerm }, "Genre" : genre}) 
   return render_template("home_page.html", books = books, searchTerm = searchTerm, genre = genre )
