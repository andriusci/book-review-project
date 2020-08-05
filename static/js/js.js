   
   
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