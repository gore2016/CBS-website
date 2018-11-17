$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.modal').modal();
  	$('.carousel.carousel-slider').carousel({
    fullWidth: true});
});

//favourite button

function myFunction(x) {
    x.classList.toggle("yellow-text");
}
