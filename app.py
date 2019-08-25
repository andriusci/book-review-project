from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bookSiteDB'
app.config["MONGO_URI"] = "mongodb+srv://dbAdmin:temporaryDevPassword@cluster0-9ekrc.mongodb.net/bookSiteDB?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/")
def home_page():
   return render_template("home_page.html", books=mongo.db.books.find().limit(10))


#testing function**************************************
@app.route("/", methods=['GET', 'POST'])
def searchResult():
   searchTerm = request.form.get('searchBox')
   mongo.db.books.create_index([('title', 'text')])
   books=mongo.db.books.find({"$text": {"$search": searchTerm } }) 
   return render_template("home_page.html", books = books, value = searchTerm )
