// Wait for the document to be ready 
$(document).ready(function() {

    // Send an AJAX GET request to the API endpoint 
    $.get("https://fourtonfish.com/hellosalut/?lang=fr", function(data) {
  
      // When the request succeeds, select the DIV with ID "hello"
      // And set its text to the "hello" property of the returned data
      $("#hello").text(data.hello);  
    });
  });
  