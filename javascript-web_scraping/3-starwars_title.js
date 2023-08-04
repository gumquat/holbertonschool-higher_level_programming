#!/usr/bin/node
const request = require('request');

function getMovieTitle (movieId) {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  request.get(url, (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      const movie = JSON.parse(body);
      console.log(`${movie.title}`);
    }
  });
}

const movieId = process.argv[2];

getMovieTitle(movieId);
