$(document).ready(function() {
    // Send a GET request to the API endpoint
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
      // Loop through each movie and add its title to the #list_movies element
      data.results.forEach(function(movie) {
        $('#list_movies').append($('<li>').text(movie.title));
      });
    });
  });
  