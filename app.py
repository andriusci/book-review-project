from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
import math

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bookSiteDB'
app.config["MONGO_URI"] = "mongodb+srv://dbAdmin:temporaryDevPassword@cluster0-9ekrc.mongodb.net/bookSiteDB?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/",  methods=['GET', 'POST'])
def initialise():
   if request.method == "POST":
      search_term = request.form['search term']
      genre = request.form['genre']
      if search_term == None or search_term == "":
         search_term = "All_books"
   else:
      search_term = "All_books"
      genre = "All"
   first_page = 1
   return redirect(url_for('searchResults', search_term = search_term, genre = genre, page_number = first_page ))

@app.route("/pagination", methods=['GET', 'POST'])
def pagination():
   if request.method == "POST":
      search_term = request.form['search']
      genre = request.form['genre']
      go_to_page = request.form['go to']
      return redirect(url_for('searchResults', search_term = search_term, genre = genre, page_number = go_to_page ))

@app.route("/Search:<search_term>/Genre:<genre>/Page:<int:page_number>", methods=['GET', 'POST'])
def searchResults(search_term, genre, page_number):
     n = page_number * 10 - 10
  #Create mongoDB query
     if search_term == "All_books" and genre == "All":
        books=mongo.db.books.find().skip(n).limit(10)
     elif search_term == "All_books" and genre != "All":
        books=mongo.db.books.find({"Genre": genre}).skip(n).limit(10)
     elif search_term != "All_books" and genre == "All":
        mongo.db.books.create_index([('title', 'text')])
        books=mongo.db.books.find({"$text": {"$search": search_term }}).skip(n).limit(10)
     else:
        mongo.db.books.create_index([('title', 'text')])
        books=mongo.db.books.find({"$text": {"$search": search_term }, "Genre" : genre}).skip(n).limit(10) 
  #Return a page with search results
     total_pages = math.ceil(books.count()/10.1)
     return render_template("home_page.html", books = books, 
                                              search_term = search_term, 
                                              genre = genre,
                                              current_page = page_number,
                                              total_pages = total_pages)

