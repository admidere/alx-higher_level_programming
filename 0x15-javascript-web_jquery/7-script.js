$(document).ready(function() {
    // Send a GET request to the API endpoint
    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
      // Update the text of the #character element with the character name
      $('#character').text(data.name);
    });
  });
  