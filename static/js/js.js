   
   
   /*Check if the necesary form fields are filled,
    if not filled show an error next to the field and scroll to the top of the page - (needed for mobile screens)
    if filled submit the form */
    /*validation is used by the "add new book" form in order to play around the text area validation*/
    function validate() {
      var title = document.getElementById('title').value;

      var description = document.getElementById('description').value;
      var genre = document.getElementById('add_genre').value;
      if (title == "") {
        document.getElementById("titleError").innerHTML = "Please fill in this field";
      }
      else {
        document.getElementById("titleError").innerHTML = ""
      }
      if (description == "") {
        document.getElementById("descriptionError").innerHTML = "Please fill in this field";
      }
      else {
        document.getElementById("descriptionError").innerHTML = ""
      }
      if (genre == "Choose genre") {
        document.getElementById("genreError").innerHTML = "Please choose genre";
      }
      else {
        document.getElementById("genreError").innerHTML = ""
      }
      if (title != "" && description != "" && genre != "Choose genre") { document.getElementById("add_book_form").submit(); }
      else {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
      }
    }


    /*Tab function for account page, code from https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_tabs_open*/

    function openTab(evt, tabName) {
      var i, tabcontent, tablinks;
      tabcontent = document.getElementsByClassName("tabcontent");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
      }
      tablinks = document.getElementsByClassName("tablinks");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
      }
      document.getElementById(tabName).style.display = "block";
      evt.currentTarget.className += " active";
    }
    
    // Get the element with id="defaultOpen" and click on it
    //document.getElementById("defaultOpen").click();