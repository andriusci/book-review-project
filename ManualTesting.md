## Manual Testing

### Table of contents:
- [Navigation](#Navigation)
- [Search form](#Search-form)
- [Search result page](#Search-result-page)


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

Displays the books which are relevant to the search criterion. If the criterion returns more than ten books then the [pagination](#Pagination) is displayed bellow the search results.

## Pagination.
Initially, the pagination shows the "number box" and the "next" button, as shown in Figure 3.
  
  <kbd>
   <img src="/static/images/testing/initPagination.png" width="75" alt="Initial pagination">
  </kbd>
  
  ***Figure 3.*** *Shows the inital pagination.*
  
  Once the "Next" button is clicked the pagination displays the "previous" button as shown in Figure 4, that if clicked brings back the previous ten results. 
  
   <kbd>
   <img src="/static/images/testing/prevPagination.png" width="75" alt="The pagination with the previous button">
  </kbd>
  
  ***Figure 4.*** *Shows the pagination whith the "previous" button.*
  
  If more results are available the pagination displays both the "previous" and the "next" buttons, together with the number box, as shown in Figure 5.
  
   <kbd>
   <img src="/static/images/testing/prevNextPagination.png" width="75" alt="The pagination with the previous and the next button"s>
  </kbd>
  
  ***Figure 4.*** *Shows the pagination whith the "previous" and the "next" buttons displayed.*
  
