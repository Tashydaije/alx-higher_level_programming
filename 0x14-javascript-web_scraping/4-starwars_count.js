#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const film = JSON.parse(body).results;
  let count = 0;

  film.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      count++;
    }
  });

  console.log(count);
});
