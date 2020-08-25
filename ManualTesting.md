## Manual Testing

### Table of contents:
- [Navigation](#Navigation)
- [Search form](#Search-form)
- [Index page](#index-page)
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
The search form is displayed in the middle of the index page and is available at the top of the other pages. The form if submitted empty, returns all the books from the database. If a search term and a genre is provided the form returns all the relevant search results. If a book title does not exist within the chosen genre or does not exist in the database at all, the feedback is displayed.
