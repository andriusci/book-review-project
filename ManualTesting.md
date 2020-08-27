## Manual Testing

### Table of contents:
- [Navigation](#Navigation)
- [Search form](#Search-form)
- [Search result page](#Search-result-page)
- [Book page](#Book-page)

## Navigation.
The navigation bar displays all the relevant links, namely Logo, Contact, Account and Add a Book button as shown in Figure 1.

  <kbd>
   <img src="/static/images/testing/navigation.png" width="550" alt="navigation bar">
  </kbd>
  
  ***Figure 1.*** *Shows the navigation bar.*


* **Logo.** If clicked, restarts the page or redirects to the index page.
* **Contact.** If clicked, brings up a pop-up dialog box that conatains the [contact form](#contact-form).
* **Account** If clicked, redirect to either the user account or the [login page](#login-page).
* **Add book button.** If clicked, redirects to either, the [add book page](#Add-book-page) or the [login page](#login-page).

## Search form.
The search form is displayed in the middle of the index page and is available at the top of the other pages. The form if submitted empty, returns all the books from the database. If a search term and a genre is provided the form returns all the relevant search results. If a book title does not exist within the chosen genre or does not exist in the database at all, the feedback is displayed, as shown in Figure 2.

 <kbd>
   <img src="/static/images/testing/searchForm.png" width="550" alt="Search form with feedback">
  </kbd>
  
  ***Figure 2.*** *Shows the search form with feedback.*

## Search result page.

Displays the books which are relevant to the search criterion. If the criterion returns more than ten books then the [pagination](#Pagination) is displayed bellow the search results. In order to fit the search result container, each book description is reduced to 300 caracters and the "read more" link is displayed. If available, the link to Amazon and the author's name are displayed, as shown in Figure 3.

 <kbd>
   <img src="/static/images/testing/results.png" width="450" alt="Search results">
  </kbd>
  
  ***Figure 3.*** *Shows the search result page.*

## Pagination.
Initially, the pagination shows the "number box" and the "next" button, as shown in Figure 4.
  
  <kbd>
   <img src="/static/images/testing/initPagination.png" width="75" alt="Initial pagination">
  </kbd>
  
  ***Figure 4.*** *Shows the inital pagination.*
  
  
  Once the "Next" button is clicked the pagination displays the "previous" button as shown in Figure 5, that if clicked brings back the previous ten results. 
  
   <kbd>
   <img src="/static/images/testing/prevPagination.png" width="75" alt="The pagination with the previous button">
  </kbd>
  
  ***Figure 5.*** *Shows the pagination whith the "previous" button.*
  
  
  If more results are available the pagination displays both the "previous" and the "next" buttons, together with the number box, as shown in Figure 6.
  
   <kbd>
   <img src="/static/images/testing/prevNextPagination.png" width="120" alt="The pagination with the previous and the next button"s>
  </kbd>
  
  ***Figure 6.*** *Shows the pagination whith the "previous" and the "next" buttons displayed.*
  
The number box responds to the user input. If a valid page number is provided then the relevant results are displayed in the [search result page](#Search-resul-page). If the page doesn't exist then the feedback is given as shown in Figure 7.

   <kbd>
   <img src="/static/images/testing/feedbackPagination.png" width="550" alt="The pagination feedback">
  </kbd>
  
  ***Figure 7.*** *Shows the feedback if the page number doesn't exist.*
  
  
  
  ## Book page
  
  The book page shows all relevant information about the book and the dropdown panel with the book details works as intended.
  
  The recommed iframe displays the percentage pie chart and two buttons namely, Yes and No. The buttons change their appearance on mouse over as intended and if clicked manipulates the recommend pie chart accordingly, as shown in Figure 8. The percentage calculations were manually tested with the correct results each time. The results and the feedback are shown immediately. 

  <kbd>
   <img src="/static/images/testing/recommend.png" width="550" alt="The "Recommend" testing>
  </kbd>
  
  ***Figure 8.*** *Shows the "Recommend" iframe testing.*
  
  The "Rate" iframe displays a pie chart that contains five stars. The stars on mouse over, change the appearance and if clicked, enables the "Rate it" button and manipulates the pie chart accordingly. Once the button is clicked, the rating is submitted and a feedback is given, as shown in Figure 9.
  
  <kbd>
   <img src="/static/images/testing/rate.png" width="550" alt="The "Rating" testing>
  </kbd>
  
  ***Figure 8.*** *Shows the "Rating" iframe testing.*
