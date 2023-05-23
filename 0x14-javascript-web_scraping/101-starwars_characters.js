#!/usr/bin/node
const request = require('request');

function printCharacters (characters, index) {
  if (index === characters.length) {
    return;
  }
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
    }
    printCharacters(characters, index + 1);
  });
}

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
