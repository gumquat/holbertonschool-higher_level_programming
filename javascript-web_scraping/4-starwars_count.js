#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  if (response.statusCode !== 200) {
    console.log(err);
    const counter = JSON.parse(body).results.reduce((count, film) =>
      count + film.characters.filter(character => character.includes('/18/')).length, 0);
  }
  console.log(counter);
});
