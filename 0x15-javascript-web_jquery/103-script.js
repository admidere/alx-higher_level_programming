$(document).ready(function() {
    // Event handler for button click
    $('#btn_translate').click(fetchTranslation);
  
    // Event handler for pressing Enter key
    $('#language_code').keypress(function(event) {
      if (event.keyCode === 13) {
        fetchTranslation();
      }
    });
  
    // Function to fetch and display translation
    function fetchTranslation() {
      // Get the language code entered by the user
      const languageCode = $('#language_code').val();
  
      // Construct the API URL with the language code
      const url = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;
  
      // Make a GET request to the API
      $.get(url, function(data) {
        // Display the translated "Hello" in the specified element
        $('#hello').text(data.hello);
      });
    }
  });
  