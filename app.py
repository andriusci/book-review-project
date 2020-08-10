from flask import Flask, render_template, redirect, request, url_for, make_response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import os
import math
import builtins

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bookSiteDB'
app.config["MONGO_URI"] = "mongodb+srv://dbAdmin:temporaryDevPassword@cluster0-9ekrc.mongodb.net/bookSiteDB?retryWrites=true&w=majority"

mongo = PyMongo(app)




@app.route("/")
def home():
      #returns the home page with simulated logged user.
      cookies = request.cookies  
      logged_user = cookies.get("logged_user")
      return render_template("index.html", logged_user= logged_user)


@app.route("/search_All",  methods=['GET', 'POST'])
def initialise():
   if request.method == "POST":
      search_term = request.form['search-term']
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
   #enables pagination
   if request.method == "POST":
      search_term = request.form['search']
      genre = request.form['genre']
      go_to_page = request.form['go to']
      return redirect(url_for('searchResults', search_term = search_term, genre = genre, page_number = go_to_page ))



@app.route("/Search:<search_term>/Genre:<genre>/Page:<int:page_number>", methods=['GET', 'POST'])
def searchResults(search_term, genre, page_number):
     n = page_number * 10 - 10
  #Create mongoDB query for the search criterion:
     if search_term == "All_books" and genre == "Choose genre":
        books=mongo.db.books.find().skip(n).limit(10)
     elif search_term == "All_books" and genre != "Chosoe genres":
        books=mongo.db.books.find({"genre": genre}).skip(n).limit(10)
     elif search_term != "All_books" and genre == "Choose genre":
        mongo.db.books.create_index([('title', 'text')])
        books=mongo.db.books.find({"$text": {"$search": search_term }}).skip(n).limit(10)
     else:
        mongo.db.books.create_index([('title', 'text')])
        books=mongo.db.books.find({"$text": {"$search": search_term }, "genre" : genre}).skip(n).limit(10) 
  #Return a page with the search results:
     total_results = books.count()
     total_pages = math.ceil(books.count()/10.1)       
     return render_template("search_results.html", books = books, 
                                              search_term = search_term, 
                                              genre = genre,
                                              current_page = page_number,
                                              total_pages = total_pages,
                                              total_results = total_results) 


@app.route("/Book_page/book_id:<book_id>")
#Finds a single book and returns the book page with the relevant information.
def create_book_page(book_id):
   book=mongo.db.books.find_one({"_id": ObjectId(book_id)})
   reviews=mongo.db.reviews.find({"book_ID": ObjectId(book_id)} )
   length = len(book.get('description'))
   if (book):
      return render_template("book_page.html", book = book, 
                                               reviews= reviews,
                                               length = length)
                                               

@app.route("/addBook", methods=['GET', 'POST'])
def addBook():
   #takes the user input and adds a new book to the database
    if request.method == "POST":
       title = request.form['title']
       description = request.form['description']
       genre = request.form['genre']
       author = request.form['author']
       img = request.form['img']
       if img == "":
          img = "/static/images/noImg.png"
       isbn10 = request.form['isbn10']
       isbn13 = request.form['isbn13']
       format1 = request.form['format']
       language = request.form['language']
       publisher = request.form['publisher']
       amazon = request.form['amazon']
       user_name = request.form['user-name']
       num_before = mongo.db.books.find().count()#number of books before an attempt to insert new book
       mongo.db.books.insert( { "title": title, 
                                "description": description, 
                                "genre" : genre,
                                "author": author,
                                "image" : img,
                                "isbn10": isbn10,
                                "isbn13" : isbn13,
                                "format" : format1,
                                "lang": language,
                                "publisher" : publisher,
                                "amazon" : amazon,
                                "added_by": user_name})
       num_after = mongo.db.books.find().count()#number of books after insertion
       if num_after > num_before:#check if new book was added
          submitted = True
       else:
          submitted = False
       response = render_template("addBook.html", numberB = num_before, numberA = num_after, submitted = submitted)
    else:
       #simulates login functionality:
        cookies = request.cookies  
        user = cookies.get("logged_user")
        if user != None:
          response = make_response(render_template("addBook.html", user = user))
        else:
          response = make_response(render_template("log_in.html", message = "add a book"))
          response.set_cookie("destination", "addBook.html") 
    return response


@app.route("/edit_book<book_id>", methods=['GET', 'POST'])
def editBook(book_id):
   #enables book editing
   book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
   if request.method == "POST":
      title = request.form['title']
      desc = request.form['description']
      genre = request.form['genre']
      author = request.form['author']
      img = request.form['img']
      isbn10 = request.form['isbn10']
      isbn13 = request.form['isbn13']
      format1 = request.form['format']
      lang = request.form['language']
      publ = request.form['publisher'] 
      amazon = request.form['amazon']
      mongo.db.books.update({"_id": ObjectId(book_id)}, {"$set": {"title": title, 
                                                                  "description" : desc,
                                                                  "genre": genre,
                                                                  "author": author,
                                                                  "image": img,
                                                                  "isbn10": isbn10,
                                                                  "isbn13": isbn13,
                                                                  "format": format1,
                                                                  "lang": lang,
                                                                  "publisher": publ,
                                                                  "amazon": amazon}})
      edit = True #passed to the template in order to provide feedback on successfull book edit.                                                          
      return render_template("iFrames/edit_book.html", book = book, edit = edit)
   else:
       edit = False 
       return render_template("iFrames/edit_book.html", book = book)



@app.route("/edit_review<review_id>", methods=['GET', 'POST'])
def editReview(review_id):
   #Enables review editing
     review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
     if request.method == "POST":
        title = request.form['title']
        comment = request.form['comment']
        rating = int(request.form['rating'])
        mongo.db.reviews.update(
                 {"_id": ObjectId(review_id)},
                 {"$set": {"title": title, "review": comment, "rating" : rating ,"dateTime": datetime.now().strftime("%:%M:%Y") }})
        review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
     return render_template("iFrames/edit_review.html", review = review) 
   

@app.route("/review:bookID:<book_id>", methods=['GET', 'POST'])
def review(book_id):
   #Takes user input, stores it in the database and returns a review page
  cookies = request.cookies  
  logged_user = cookies.get("logged_user")
  if logged_user != None:
     if request.method == "POST":
        #data insert...........and return feedback
        title = request.form['title']
        review = request.form['comment']
        rating = int(request.form['rating'])
        book_id = request.form['book_id']
        logged_user = logged_user
        dateTime = datetime.now().strftime("%D-%M-%Y")
        mongo.db.reviews.insert({"title": title,
                                 "review": review,
                                 "rating" : rating, 
                                 "user": logged_user, 
                                 "book_ID" : ObjectId(book_id),
                                 "dateTime": dateTime})
        submitted = True
        response = make_response(render_template("iFrames/review.html", book_id =book_id, status = submitted ))
     else:
        response = make_response(render_template("iFrames/review.html", book_id = book_id ))
  else:
      response = make_response(render_template("log_in.html" ))
      response.set_cookie("destination", "review.html") 
      response.set_cookie("book_id", book_id) 

  return response


@app.route("/rate:bookID:<book_id>", methods=['GET', 'POST'])
def rate(book_id):
   #enables the book rating functionality
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
      #Set the width of each rating chart bar (in relation to the biggest bar)
      if ratingList[mostRatingIndex] != 0:
       if ratingList[mostRatingIndex] < 230:
         factor = 230/ratingList[mostRatingIndex]
         i = 0
         while i < len(ratingList):
          ratingList[i] = ratingList[i] * factor
          ratingList[i] = int(ratingList[i])
          i += 1
       else:
         factor = ratingList[mostRatingIndex] / 230 
         i = 0
         while i < len(ratingList):
          ratingList[i] = ratingList[i] / factor 
          ratingList[i] = int(ratingList[i])
          i += 1
         ratingList[mostRatingIndex] = 230
      #calculate average rating (out of 5)
      if totalRatings != 0:
           average = (fiveStars * 5 + fourStars * 4 + threeStars * 3 + twoStars * 2 + oneStar * 1) / totalRatings  
           average = round(average,1)
           #calculate circle size
           size = round(average) * 20
      else:
         average = 0
         size=0
      return render_template("iFrames/rating_chart.html", 
                                               ratingList = ratingList, 
                                               numOfRatings = numOfRatings, 
                                               totalRatings= totalRatings,
                                               average= average,
                                               size = size )

@app.route("/my_account", methods=['GET', 'POST'])
def account():
      cookies = request.cookies  
      user = cookies.get("logged_user")
      if user != None:
        logged_user = mongo.db.users.find_one({"name": user})
        if request.method == "POST":
           form_id = request.form['id']
           if form_id == "delete_book":
             book_id = request.form['book_id']
             mongo.db.books.remove({"_id":ObjectId(book_id)})
           elif form_id == "delete_review":
             review_id = request.form['review_id']
             mongo.db.reviews.remove({"_id":ObjectId(review_id)})
        books = mongo.db.books.find({"added_by": logged_user['name'] })
        reviews = mongo.db.reviews.find({"user": logged_user['name'] })
        response = make_response(render_template("account.html", logged_user = logged_user, books = books, reviews = reviews))
      else:
        message = "accsess your account"
        response = make_response(render_template("log_in.html", message = message ))
        response.set_cookie("destination", "account.html") 
      return response

                                       
@app.route("/log_in", methods=['GET', 'POST'])
def log_in():
   #Log in simulation
   if request.method == "POST":
       user_name = request.form['user-name']
      
       #check if the name exist in the user database
       user = mongo.db.users.find_one({"name": user_name})
       if user:
           cookies = request.cookies  
           dest = cookies.get("destination")
           books = mongo.db.books.find({"added_by": user_name })
           if dest == "review.html":
              book_id = cookies.get("book_id")
           else:
              book_id ="NA"
           destination_page = dest
           response = make_response(render_template(destination_page, logged_user = user, book_id = book_id, books = books ))
           response.set_cookie("logged_user", user_name)  
       else:
           response = make_response(render_template("log_in.html", error = True ))
       return response
   else:
      return render_template("log_in.html")


@app.route("/recommend:bookID:<book_id>", methods=['GET', 'POST'])
def recommend(book_id):
   #enables book recommendations.
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
   #register a new user.
   if request.method == "POST":
      cookies = request.cookies  
      dest = cookies.get("destination")
      user = request.form['user-name']
      pass1 = request.form['password']
      pass2 = request.form['password2']
      email = request.form['email']
      #check if user name already exist. If not proceed with registration.
      exists = mongo.db.users.find_one({"name": user})
      if exists:
         return render_template("register.html", userError = True,user = user, email = email)
      elif pass1 != pass2:
         return render_template("register.html", userError = False, passError = True, email = email, user = user)
      else:
         mongo.db.users.insert({"name": user, "pasword": pass1, "email": email})
         response =  make_response(render_template("register.html", success = True, dest = dest, user = user))
         response.set_cookie("logged_user", user)
         return response
   else:
      return render_template("register.html")

@app.route("/del")
def delete():
   mongo.db.recommend.remove()
   mongo.db.reviews.remove()
  # mongo.db.books.remove()
   #mongo.db.users.remove()
   return render_template("index.html")