$(document).ready(function() {
    // Attach a click event handler to the #toggle_header element
    $('#toggle_header').click(function() {
      // Toggle the class of the header element between red and green
      $('header').toggleClass('red green');
    });
  });
  