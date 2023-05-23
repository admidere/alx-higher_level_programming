#!/usr/bin/node

const request = require('request');

function printMovieCharacters (movieId) {
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request.get(filmUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    } else {
      const film = JSON.parse(body);
      const characters = film.characters;

      if (characters.length === 0) {
        console.log('No characters found for this movie.');
      } else {
        let count = 0;

        function fetchCharacter (characterUrl) {
          request.get(characterUrl, (error, response, body) => {
            if (error) {
              console.error(error);
            } else if (response.statusCode !== 200) {
              console.error(`Failed to fetch character data. Status code: ${response.statusCode}`);
            } else {
              const character = JSON.parse(body);
              console.log(character.name);
            }

            count++;

            if (count === characters.length) {
              process.exit();
            }
          });
        }

        characters.forEach((characterUrl) => {
          fetchCharacter(characterUrl);
        });
      }
    }
  });
}

// Usage: node script.js <movie_id>
const movieId = process.argv[2];
printMovieCharacters(movieId);
