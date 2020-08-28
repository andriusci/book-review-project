
`<addr>` 
``` text in gray ```


 # Best Reads - Code Institute. Milestone 3
 ![Main picture](/static/images/main.png)

https://book-review-app-ci.herokuapp.com/


### Table of contents:

- [Description](#Description)
- [UX](#UX)
    - [Business Goals](#Business-goals)
    - [User need](#User-needs)
- [Features](#Features)
- [Features Left to Implement](#Features-Left-to-Implement)
- [Mockups](#Mockups)
- [Technologies used](#Technologies-used)
- [Data structure](#Data-structure)
- [Testing](#Testing)
     - [Validation](#Validation)
     - [Responsiveness](#Responsiveness)
     - [Manual testing](#Manual-testing)
- [Bugs](#Bugs)
- [Deployment](#Deployment)
- [Credits](#Credits)
    
## Description
The Best Reads project is focused around people who are looking for the books via the Internet. The project aims to help people making crowdsource-based decisions about their next good read and attempts to help the owner making a few bucks. Therefore, it takes shape of a database backed website that not only allows the users to search, rate, recommend and review books, but also enables the site owner to participate in the Amazon’s affiliate program.

## UX
In order to build good UX it is necessary to identify business goals and to determine user needs. Therefore, this section gives an insight into the aforementioned aspects, which in turn helps to specify features for this project.

#### Business goals
* increase business value by allowing the owner to earn money via an affiliate program.
* increase earning potential by encouraging the users to upload more books.

#### User needs
As a book hunter, I would like to:
* be able to search for the books.
* find the information about the books such as the book format.
* know what other people think about the particular book.
* be able to buy a book directly from the site or be redirected to an e-shop via a link from the site.

As a user who read a particular book and found it on the site, I would like to:
* let others know about my opinion regarding the book.
* know what others think about the book.

As a user who read a particular book, searched for it and did not find it on the website, I would like to:
* share the book with others and let others know what I think about the book.

As a user who has submitted a review or a book, I would like to:
* be able to edit or delete my submission, in case I have changed my mind.

As a user who has questions I would like to contact someone.

As a site owner, I would like to: 
* allow the website users to contact me,in case they have any queries.
* be able to obtain information such as the most popular search titles or genres, so I could analyse data in order to improve the UX.

## Features
This section describes features that satisfy the requirements for the current version release. Also the section briefly outlines additional features for the subsequent versions of this project.

### Existing Features

* **Search form.** Enables the website users to search for the books by allowing them to choose a category and enter the book title, as shown in Figure 1. The form is accessible throughout the site. It appears in the middle of the index page and is available at the top of other pages. 

     <kbd>
      <img src="/static/images/features/search-form.png" width="450" alt="Search Form">
    </kbd>
  
  ***Figure 1.*** *Shows the search form.*
 
 
* **Search result page.** Displays up to ten search results matching a search criteria, as shown in Figure 2. If a query returns more than ten items, a pagination is displayed at the bottom of the page.

   <kbd>
   <img src="/static/images/features/search-result.png" alt="Search results">
   </kbd>
   
   ***Figure 2.*** *Shows a fragment of the result page.* 
  
   
* **Pagination.**  Allows the website users to move forward and backward between the the search result pages. Also enables users to get to a particular page by allowing them to enter a page number. As mentioned in the Search result page section, every search query is limited to return up to ten items. Moving between the pages simply performs a new search with the same query but, with a number of items skipped depending on the user action. For example, if a search returns thirty books only first ten books are requested from the database and displayed on the page. Moving to a next page would perform the same query with the first ten books excluded.

    <kbd>
    <img src="/static/images/features/pagination.png"  alt="Pagination">
    </kbd>
 
    ***Figure 3.*** *Shows the pagination at the bottom of the search result page.*


* **Book page.** Displays all the relevant information for a particular book. Shows the book's title, description, cover image and if available, a link to the affiliate website. Also contains a drop-down panel that if clicked reveals more information such as the book's ISBN, as shown in Figure 4.
   
    <kbd>
    <img src="/static/images/features/dropdown.png" alt="Dropdown information panel">
    </kbd>
    
     ***Figure 4.*** *Shows a fragment of the drop-down panel from the book page.*
     
     
  The page also contains additional three features namely Rating Chart, Recommend and Rate.
  
     * **Rating Chart**
      Shows the book's average rating in the form of a pie chart. Also displays the bar chart that represents the number of ratings per each star category as      shown in Figure 5.
    
     <kbd>
          <img src="/static/images/features/rating-chart.png"  alt="The rating chart">
         </kbd>
   
     ***Figure 5.*** *The rating chart.*
     
     
     * **Recommend** Allows the users to either positively or negatively recommend a book. Also shows a pie chart that represents a percentage of the recommendation as shown in Figure 6.
     
     <kbd>
     <img src="/static/images/features/recommend.png"  alt="Recommend">
     </kbd>
    
     ***Figure 6.*** *The recommend feature.*    
     
     * **Rate** Allows the users to rate a book by choosing the number of stars and clicking the Rate button as shown in Figure 7. 
    
     <kbd>
     <img src="/static/images/features/rate.png"  alt="the rate feature">
     </kbd>
     
     ***Figure 7.*** *The rate feature.*  
    
     All three aforementioned features are interactive. Therefore, in order to eliminate page reload with every interaction, each feature is embedded in a separate iframe. 
     Just bellow the three iframes the users are presented with the review section.
     
     
     * **Reviews** Displays all the user submitted reviews related to a specific book, as shown in Figure 8.
     
     <kbd>
     <img src="/static/images/features/reviews.png"  alt="the review section">
     </kbd>
     
     ***Figure 8.*** *The review section.*  
     
* **Log in** As specified in the Project Recuirements, no authentication is expected for this project. Therefore, the login functionality in this project is simply an imitation. Once a user name with a password is submitted, the application checks whether a user with that name exist regardless of the given password.  

* **Add book page.** Enables the logged in users to add a new book to the database by allowing them to fill in the form. 

* **User account.** Allows the logged in users to edit or delete previously submitted books and reviews.

* **Contact form.** Allows users to contact the owner by having them fill out three compulsory fields namely, name, email and message text. For the ease of access the form is embedded in the Bootstrap pop-up dialog and is available throughout the site.

### Features left to implement.

## Mockups

* [Home page](/static/images/mockups/homePage.png)
* [Home page mobile](/static/images/mockups/homePageMobile.png)
* [Search result page](/static/images/mockups/resultPage.png)
* [Search result mobile](/static/images/mockups/resultPageMobile.png)
* [Book page](/static/images/mockups/bookPage.png)
* [Book page mobile](/static/images/mockups/bookPageMobile.png)
* [Add book page](/static/images/mockups/addBook.png)
* [Add book page mobile](/static/images/mockups/addBookMobile.png)



## Data structure:

The main focus of the project – the data, is managed by a document-oriented database called MongoDB. The database behind this project consist of four collections of documents namely Books, Recommend, Reviews and Users, as shown in Figure 9.

   <kbd>
   <img src="/static/images/database.png"  width="550" alt="the data structure">
   </kbd>
     
   ***Figure 9.*** *The data structure.*  
   
   Each ``` Book ``` document in the ``` Books ``` collection has One-to-Many relationship with the ``` recommend ``` and the ``` review ``` documents in the ``` Recommend ``` and the ``` Review ``` collections, respectively. The relationship is achieved through the automatically assigned primary key field called ``` _id ```. Similarly the ``` user ``` documents are related to the ``` Recommend ```, the ``` Review ``` and the ``` Book ``` documents through the ``` user_name ``` fields. However, since the user names in this project are unique, the ``` user_name ``` fields in the ``` User ``` documents are not defined as primary keys. The relationship between the documents remains One-to-many even if the ``` user_name ``` fields are secondary keys.
   
Such relationship between the collections allows each book to have many reviews and recommendations but, only one owner. Similarly, the owner might have many reviews, recommendations and books all of whom might only belong to one user.

## Technologies used:

* **Languages:**
    * **HTML5**
    * **CSS3**
    * **JavaScript** Used for the front end functionality such as the form errors.
    * **Python** Used in the Flask framework for the back end code.
    
 * **Frameworks:**
     * **Bootstrap (4.3.1**. Enables collapsible panel in the book page
     * **Flask** The project is build using the Flask web framework.
     
 * **Libraries:**
     * **JQuery** Enables Bootstrap functionality.
* **Database:**
    * **MongoDB** The project is backed by a document-oriented database called MongoDB.
    
    
## Testing

   ##### Validation
   
   * **HTML** The website has passed 3w.org markup validation with the exeptions explained in the [Bugs](#Bugs) section.
   * **CSS** The website has passed 3w.org css validation. <p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
       </a>
    </p>
           
   * **JavaScript** Chrome developer tools have showed no errors.
   *
   
   ##### Responsiveness
   ##### [Manual testing](/ManualTesting.md)
   
## Bugs

* **Rating chart** Once the star rating is submitted the rating chart iframe reloads in order to show the result immediately. However, sometimes it reloads faster than the information gets to the database, therefore the results are not shown right away. This could be fixed by delaying the page reload with JavaScript.

* **select genre box** The select genre box does not appear as intended in the Mozilla Firefox browser as shown in the image bellow:

   <kbd>
   <img src="/static/images/testing/selectBug.png"  width="300" alt="select genre bug">
   </kbd>

* **HTML Validation**  

    * **Book page** 
    1. The ``` scrolling ``` attribute on the ``` iframe ``` element is obsolete as shown in the image bellow:
    
     <kbd>
       <img src="/static/images/testing/iframeBug.png"  width="300" alt="iframe bug">
     </kbd>
     
     According to James Donnelly on [Stack Overflow](https://stackoverflow.com/questions/15494568/html-iframe-disable-scroll) the ``` iframe```  ``` scrolling```      attribute was removed from the HTML5 specification. Therefore, it is recommended to use the CSS  ``` overflow ``` equivalent instead. However, for unkmown        reason it does not seem to work. Hence, this version release will use the ``` iframe```  ``` scrolling```  attribute.
     
   2. The ``` modal ``` element is not alowed as child of ``` main ``` element as shown in the screenshot bellow:
   
      <kbd>
       <img src="/static/images/testing/iframeBug.png"  width="300" alt="iframe bug">
     </kbd>
     
     There is no further errors white testing without the ``` modal ``` element.

## Deployment

The app is deployed on Heroku apps.

**Prerequisites:**

* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Free Heroku account](https://www.heroku.com/)
* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
* [Free MongoDB Atlas database](https://www.mongodb.com/cloud/atlas) Please refer to the - [Data structure](#Data-structure) section for the database structure.

**Deployment procedure:**

* If you haven’t already, download the project files from the [Github repositoy]( https://github.com/andriusci/book-review-project)

   <kbd>
   <img src="/static/images/deploy/download.png"  alt="download project files">
   </kbd>

* From your Heroku dashboard click create new app:

   <kbd>
   <img src="/static/images/deploy/newApp.png"  alt="click new app">
   </kbd>
   
* Choose a name and click create app button:
   
   <kbd>
   <img src="/static/images/deploy/createApp.png"  alt="click create app">
   </kbd>
   
* Provide your MongoDB [connection string](https://docs.mongodb.com/manual/reference/connection-string/):
  
  * From the setting tab in your Heroku account click reveal config vars and enter your connection string with DB_URI set as key:
  
     <kbd>
   <img src="/static/images/deploy/configVar.png">
   </kbd>
   
* Chose a deployment method (HerokuGit in this case):
    
     <kbd>
   <img src="/static/images/deploy/method.png">
   </kbd>
   
* From the terminal, log in to your Heroku account:

     ``` $ heroku login ```
     
* When prompted press any but q key to open a login window in your browser. After successful log in, create a new Git repository:

     ``` $ cd your-project ```
     
     ``` $ git init ```
     
     ``` $ heroku git:remote -a your-new-app-name ```
     
 * Commit the code and push it to Heroku using Git:
  
     ```   $ git add *  ``` 
     
     ```  $ git commit -am "deployment"  ``` 
     
     ```  $ git push heroku master  ``` 
     
   
Let the Heroku do the magic and your app should be ready at your-new-app-name.herokuapp.com.
    
## Credits

* **Collapsable panel** – contains book details in the book page.
[https://www.w3schools.com/bootstrap/bootstrap_collapse.asp](https://www.w3schools.com/bootstrap/bootstrap_collapse.asp)

* **Tabs** - in the account page
[https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_tabs_open](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_tabs_open)

* **Pure CSS Percentage Circle** - 
[http://circle.firchow.net/](http://circle.firchow.net/)

* **Rating stars**
[https://codepen.io/zellwk/pen/YwjZQv](https://codepen.io/zellwk/pen/YwjZQv)

* **Flask Tutorial in Visual Studio Code**
[https://code.visualstudio.com/docs/python/tutorial-flask](https://code.visualstudio.com/docs/python/tutorial-flask)
