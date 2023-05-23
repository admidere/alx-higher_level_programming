#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes('18/')) count++;
      }
    }

    console.log(count);
  }
});
