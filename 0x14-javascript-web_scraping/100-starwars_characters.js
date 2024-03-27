#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const movie = JSON.parse(body);
  movie.characters.forEach(characterUrl => {
    request(characterUrl, (err, res, body) => {
      if (err) {
        console.log(err);
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
