#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const starWarsUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(starWarsUrl, 'utf-8', (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const movie = JSON.parse(body);
  console.log(movie.title);
});
