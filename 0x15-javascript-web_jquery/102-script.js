$(document).ready(function() {
    // Event handler for button click
    $('#btn_translate').click(function() {
      // Get the language code entered by the user
      const languageCode = $('#language_code').val();
  
      // Construct the API URL with the language code
      const url = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;
  
      // Make a GET request to the API
      $.get(url, function(data) {
        // Display the translated "Hello" in the specified element
        $('DIV#hello').text(data.hello);
      });
    });
  });
  