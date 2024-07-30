#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes('/18/')) {
          count++;
        }
      });
    });

    console.log(count);
  }
});
