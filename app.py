from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
import math
import builtins

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bookSiteDB'
app.config["MONGO_URI"] = "mongodb+srv://dbAdmin:temporaryDevPassword@cluster0-9ekrc.mongodb.net/bookSiteDB?retryWrites=true&w=majority"

mongo = PyMongo(app)








@app.route("/searchAll",  methods=['GET', 'POST'])
def initialise():
   if request.method == "POST":
      search_term = request.form['search term']
      genre = request.form['genre']
      if search_term == None or search_term == "":
         search_term = "All_books"
   else:
      search_term = "All_books"
      genre = "All genres"
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
     if search_term == "All_books" and genre == "All genres":
        books=mongo.db.books.find().skip(n).limit(10)
     elif search_term == "All_books" and genre != "All genres":
        books=mongo.db.books.find({"genre": genre}).skip(n).limit(10)
     elif search_term != "All_books" and genre == "All genres":
        mongo.db.books.create_index([('title', 'text')])
        books=mongo.db.books.find({"$text": {"$search": search_term }}).skip(n).limit(10)
     else:
        mongo.db.books.create_index([('title', 'text')])
        books=mongo.db.books.find({"$text": {"$search": search_term }, "genre" : genre}).skip(n).limit(10) 
  #Return a page with search results
     total_pages = math.ceil(books.count()/10.1)
     return render_template("search_results.html", books = books, 
                                              search_term = search_term, 
                                              genre = genre,
                                              current_page = page_number,
                                              total_pages = total_pages)








@app.route("/", methods=['GET', 'POST'])
def test():
   if request.method == "POST":
      search_term = request.form['search']
      genre = request.form['genre']
      go_to_page = request.form['go to']
      return redirect(url_for('searchResults', search_term = search_term, genre = genre, page_number = go_to_page ))
   else:
      return render_template("home_page.html")





@app.route("/Book_title:<title>/book_id:<book_id>")
def create_book_page(title, book_id):
   book=mongo.db.books.find_one({"_id": ObjectId(book_id)})
   if (book):
      #Determine how many ratings the book has per each star category.
      fiveStars =  mongo.db.reviews.find({"rating": "5", "book_ID" : ObjectId(book_id)}).count()
      fourStars = mongo.db.reviews.find({"rating": "4", "book_ID" : ObjectId(book_id)}).count()
      threeStars =  mongo.db.reviews.find({"rating": "3", "book_ID" : ObjectId(book_id)}).count()
      twoStars = mongo.db.reviews.find({"rating": "2", "book_ID" : ObjectId(book_id)}).count()
      oneStar =  mongo.db.reviews.find({"rating": "1", "book_ID" : ObjectId(book_id)}).count()
      numOfRatings = [fiveStars,fourStars, threeStars, twoStars, oneStar]
      #Determine which star category has most of the ratings and 
      #set the widths of the rating chart bars (in relation to the biggest bar)
      ratingList = [fiveStars,fourStars,threeStars,twoStars,oneStar]
      mostRatingIndex = ratingList.index(max(ratingList))
      totalRatings = sum(ratingList)
      #Set the widths of the rating chart bars (in relation to the biggest bar)
      if ratingList[mostRatingIndex] < 300:
         factor = 300/ratingList[mostRatingIndex]
         i = 0
         while i < len(ratingList):
          ratingList[i] = ratingList[i] * factor
          ratingList[i] = int(ratingList[i])
          i += 1
      else:
         factor = ratingList[mostRatingIndex] / 300 
         i = 0
         while i < len(ratingList):
          ratingList[i] = ratingList[i] / factor
          ratingList[i] = int(ratingList[i])
          i += 1
         ratingList[mostRatingIndex] = 300
      return render_template("book_page.html", book = book, ratingList = ratingList, numOfRatings = numOfRatings, totalRatings= totalRatings)


@app.route("/test.html")
def test1():
     return render_template("test.html")