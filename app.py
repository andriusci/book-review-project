from flask import Flask, render_template, redirect, request, url_for, make_response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
import math
import builtins

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bookSiteDB'
app.config["MONGO_URI"] = "mongodb+srv://dbAdmin:temporaryDevPassword@cluster0-9ekrc.mongodb.net/bookSiteDB?retryWrites=true&w=majority"

mongo = PyMongo(app)




@app.route("/")
def home():
      cookies = request.cookies  
      logged_user = cookies.get("logged_user")
      return render_template("index.html", logged_user= logged_user)


@app.route("/search_All",  methods=['GET', 'POST'])
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
   return redirect(url_for('searchResults', search_term = search_term, genre = genre, page_number = first_page))

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


@app.route("/Book_title:<title>/book_id:<book_id>")
def create_book_page(title, book_id):
   book=mongo.db.books.find_one({"_id": ObjectId(book_id)})
   reviews=mongo.db.reviews.find({"book_ID": ObjectId(book_id)} )
   if (book):
      return render_template("book_page.html", book = book, 
                                               reviews= reviews)
                                               




@app.route("/addBook", methods=['GET', 'POST'])
def addBook():
    if request.method == "POST":
       title = request.form['title']
       description = request.form['description']
       genre = request.form['genre']
       author = request.form['author']
       img = request.form['img']
       isbn10 = request.form['isbn10']
       isbn13 = request.form['isbn13']
       format1 = request.form['format']
       language = request.form['language']
       publisher = request.form['publisher']
       amazon = request.form['amazon']
       num_before = mongo.db.books.find().count()#number of books before an attempt to insert new book
       mongo.db.books.insert( { "title": title, 
                                "description": description, 
                                "genre" : genre,
                                "author": author,
                                "imgage" : img,
                                "isbn10": isbn10,
                                "isbn13" : isbn13,
                                "format" : format1,
                                "lang": language,
                                "publisher" : publisher,
                                "amazon" : amazon} )
       num_after = mongo.db.books.find().count()#number of books after insertion
       if num_after > num_before:#check if new book was added
          message= "success"
       else:
          message ="something went wrong"
       response = render_template("addBook.html", numberB = num_before, numberA = num_after, message = message)
    else:
        cookies = request.cookies  
        user = cookies.get("logged_user")
        if user != None:
          response = make_response(render_template("addBook.html"))
        else:
          response = make_response(render_template("log_in.html" ))
          response.set_cookie("destination", "addBook.html") 
    return response

@app.route("/review:bookID:<book_id>", methods=['GET', 'POST'])
def review(book_id):
  cookies = request.cookies  
  logged_user = cookies.get("logged_user")
  if logged_user != None:
     if request.method == "POST":
        #data insert...........and return feedback
        title = request.form['title']
        review = request.form['review']
        rating = int(request.form['rating'])
        book_id = request.form['book_id']
        logged_user = logged_user
        mongo.db.reviews.insert({"title": title,
                                 "review": review,
                                 "rating" : rating, 
                                 "user": logged_user, 
                                 "book_ID" : ObjectId(book_id)})
        submitted = True
        response = make_response(render_template("review.html", book_id =book_id, status = submitted ))
     else:
       #responce = review page
        response = make_response(render_template("review.html", book_id = book_id ))
  else:
      response = make_response(render_template("log_in.html" ))
      response.set_cookie("destination", "review.html") 
      response.set_cookie("book_id", book_id) 

  return response


@app.route("/rate:bookID:<book_id>", methods=['GET', 'POST'])
def rate(book_id):
   if request.method == "POST":
    book_id = request.form['book_id']
    rating = int(request.form['rating'])
    review = ""
    mongo.db.reviews.insert( { "review": review, "book_ID" : ObjectId(book_id), "rating" : rating})
    submitted = True
   else:
    submitted = False
   return render_template("iFrames/rate.html", book_id = book_id, submitted = submitted)

@app.route("/ratingChart:bookID:<book_id>", methods=['GET', 'POST'])
def ratinChart(book_id):
   #Determine how many ratings the book has per each star category.
      fiveStars =  mongo.db.reviews.find({"rating": 5, "book_ID" : ObjectId(book_id)}).count()
      fourStars = mongo.db.reviews.find({"rating": 4, "book_ID" : ObjectId(book_id)}).count()
      threeStars =  mongo.db.reviews.find({"rating": 3, "book_ID" : ObjectId(book_id)}).count()
      twoStars = mongo.db.reviews.find({"rating": 2, "book_ID" : ObjectId(book_id)}).count()
      oneStar =  mongo.db.reviews.find({"rating": 1, "book_ID" : ObjectId(book_id)}).count()
      numOfRatings = [fiveStars,fourStars, threeStars, twoStars, oneStar]
      #Determine which star category has most of the ratings and 
      #set the widths of the rating chart bars (in relation to the biggest bar)
      ratingList = [fiveStars,fourStars,threeStars,twoStars,oneStar]
      mostRatingIndex = ratingList.index(max(ratingList))
      totalRatings = sum(ratingList)
      #Set the widths of the rating chart bars (in relation to the biggest bar)
      if ratingList[mostRatingIndex] != 0:
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
      #calculate average rating (out of 5)
      if totalRatings != 0:
           average = (fiveStars * 5 + fourStars * 4 + threeStars * 3 + twoStars * 2 + oneStar * 1) / totalRatings  
           average = round(average,1)
           #calculate circle diameter
           d = round(average) * 20
      else:
         average = 0
         d=0
      return render_template("iFrames/ratingChart.html", 
                                               ratingList = ratingList, 
                                               numOfRatings = numOfRatings, 
                                               totalRatings= totalRatings,
                                               average= average,
                                               d = d )

@app.route("/my_account", methods=['GET', 'POST'])
def account():
      cookies = request.cookies  
      user = cookies.get("logged_user")
      if user != None:
        logged_user = mongo.db.users.find({"name": user})
        response = make_response(render_template("account.html", logged_user = logged_user))
      else:
        response = make_response(render_template("log_in.html" ))
        response.set_cookie("destination", "account.html") 
      return response

                                         

@app.route("/log_in", methods=['GET', 'POST'])
def log_in():
   if request.method == "POST":
       user = request.form['user_name']
      
       #check if the name exist in the users database
       exists = mongo.db.users.find_one({"name": user})
       if exists:
           cookies = request.cookies  
           dest = cookies.get("destination")
           if dest == "review.html":
              book_id = cookies.get("book_id")
           else:
              book_id ="NA"
           destination_page = dest
           response = make_response(render_template(destination_page, logged_user = user, book_id = book_id ))
           response.set_cookie("logged_user", user)  
       else:
           response = make_response(render_template("log_in.html", error = True ))
       return response

   else:

      return render_template("log_in.html")


@app.route("/recommend:bookID:<book_id>", methods=['GET', 'POST'])
def recomend(book_id):
   cookies = request.cookies  
   user = cookies.get("logged_user")
   if request.method == "POST":
      user = request.form['user']
      if user == "None":
         user = ""
      recommend = request.form['recommend']
      if recommend == "yes":
         mongo.db.recommend.insert({"recommend": True, "user": user, "book_id" : book_id })
      else:
          mongo.db.recommend.insert({"recommend": False, "user": user , "book_id" : book_id})
      total =  mongo.db.recommend.find({"book_id": book_id}).count()
      yes = mongo.db.recommend.find({"book_id": book_id, "recommend": True}).count()
      if yes != 0:
         recommend =  round(yes / (total/100)) 
      else:
         recommend = 0  
      return render_template("iFrames/recommend.html", recommend = recommend, 
                                                      total = total,
                                                      feedback = True)
      #Determine how many users would recomend the book.
   total =  mongo.db.recommend.find({"book_id":book_id}).count()
   yes = mongo.db.recommend.find({"recommend": True, "book_id":book_id}).count()
   if total and yes != 0:
      recommend =  round(yes / (total/100))
   else:
      recommend = 0
   return render_template("iFrames/recommend.html", recommend = recommend, total = total, book_id = book_id, logged_user = user) 
                                              
@app.route("/register", methods=['GET', 'POST'])
def register():
   if request.method == "POST":
      cookies = request.cookies  
      dest = cookies.get("destination")
      user = request.form['user_name']
      pass1 = request.form['password']
      pass2 = request.form['password2']
      email = request.form['email']
      #check if user name already exist. If not proceed with registration.
      exists = mongo.db.users.find_one({"name": user})
      if exists:
         return render_template("register.html", userError = True, email = email)
      elif pass1 != pass2:
         return render_template("register.html", userError = False, passError = True, email = email, user = user)
      else:
         mongo.db.users.insert({"name": user, "pasword": pass1, "email": email})
         response =  make_response(render_template("register.html", success = True, dest = dest, user = user))
         response.set_cookie("logged_user", user)
         return response
   else:
      return render_template("register.html")


@app.route("/delete")
def delete():
   mongo.db.recommend.remove()
   mongo.db.reviews.remove()
   return render_template("index.html")