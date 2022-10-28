(function($){
    $(function(){
  
      $('.sidenav').sidenav();
      $('.parallax').parallax();
      $('.carousel').carousel({
        fullWidth: true,
      });
      $('.materialboxed').materialbox();
      $('#year').text(new Date().getFullYear());
  
    }); // end of document ready
  })(jQuery); // end of jQuery name space
  