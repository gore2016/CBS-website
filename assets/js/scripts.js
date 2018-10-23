  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, );
  });



  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.parallax');
    var instances = M.Parallax.init(elems, );
  });



document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.carousel');
    var instances = M.Carousel.init(elems,  );
  });
var instance = M.Carousel.init({
    fullWidth: true
  });


 document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems,);
  });

// document.ready('DOMContentLoaded',function(){
//   var navig = document.querySelectorAll('.navi');
//   if (window.scrollTop()>300) {navig.addClass('black')}
//     else(navig.remove('black'));
// });

// $(document).ready(function(){

//           $(window).scroll(function(){

//             if($(window).scrollTop()>300){
//               $('nav').addClass('black');
//             }else{
//               $('nav').removeClass('black');
//             }
//           });
//         });


  // document.addEventListener('DOMContentLoaded', function() {
  //   var elems = document.querySelectorAll('.parallax');
  //   var instances = M.Parallax.init(elems, options);
  // })