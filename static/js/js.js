   
   
   /*Check if the form fields are filled,
    if not filled show an error next to the field and scroll to the top of the page - (needed for mobile screens)
    if filled submit the form */
    /*validation is used by the "add new book" form in order to play around the text area validation 
    since the text area doesnt have validatition by default*/
function validate_book() {
      var title = document.getElementById('title').value;

      var description = document.getElementById('description').value;
      var genre = document.getElementById('add-genre').value;
      if (title == "") {
        document.getElementById("title-error").innerHTML = "Please fill in this field";
      }
      else {
        document.getElementById("title-error").innerHTML = ""
      }
      if (description == "") {
        document.getElementById("description-error").innerHTML = "Please fill in this field";
      }
      else {
        document.getElementById("description-error").innerHTML = ""
      }
      if (genre == "Choose genre") {
        document.getElementById("genre-error").innerHTML = "Please choose genre";
      }
      else {
        document.getElementById("genre-error").innerHTML = ""
      }
      if (title != "" && description != "" && genre != "Choose genre") { document.getElementById("add-book-form").submit(); }
      else {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
      }
    }



 //Check if the review form fields are filled and submit the form.
 //Or give an error.
function validate_review() {
          var title =  document.getElementById('title').value;
         
         var review = document.getElementById('comment').value;
          var rating = document.getElementById('rating').value;
         if (title == ""){
          document.getElementById("title-error").innerHTML = "Please fill in this field";}
         else{
           document.getElementById("title-error").innerHTML =""
         }
         if (review == ""){
          document.getElementById("review-error").innerHTML = "Please fill in this field";}
         else{
           document.getElementById("review-error").innerHTML = ""
         }
         if (rating == "0"){
          document.getElementById("rating-error").innerHTML = "Please chose the number of stars";}
         else{
           document.getElementById("rating-error").innerHTML = ""
         }
         if(title != "" && review != "" && rating != "0"){document.getElementById("review-form").submit();}
}



   