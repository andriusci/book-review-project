function parent_reload(){
    /* reloads the rating chart iframe in the book page, so that the reluts shown immediately */
    parent.ratingChart.location.reload();
  }
  
  /*modified code from https://codepen.io/zellwk/pen/YwjZQv*/
  /*Initilise variables*/
  var rate_btn = document.getElementById("rate-btn");                
  var starContainer = document.getElementById('stars')
  var stars = Array.prototype.slice.call(starContainer.children)
  var totalStars = stars.length
  var rated = document.getElementById('rated')
  
  rate_btn.disabled = true; 
  
  /*the function enables star ratnigs */
  starContainer.addEventListener('click', function(e) {
    var index = stars.indexOf(e.target)
    var count = totalStars - index;
    stars.forEach(el => el.classList.remove('is-selected'))
    e.target.classList.add('is-selected')
    document.getElementById("rating").value = count;
    document.getElementById("ratingChart").className = "c100"+" "+"p"+count*20+" "+"center";
    if (document.getElementById("rate-btn") != 'Null'){
    rate_btn.disabled = false;
    rate_btn.classList.add("rate-btn-after","rate-btn-after:hover")};
  })