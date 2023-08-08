#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let counter = 0;

function processResponse (err, response, body) {
  // handle error
  if (err) {
    console.error(err);
    return;
  }

  // handle non-200 status code
  if (response.statusCode !== 200) {
    console.error('Request failed with status: ', response.statusCode);
    return;
  }

  // process the body within this callback
  const data = JSON.parse(body).results;
  for (const film of data) {
    for (const character of film.characters) {
      if (character.includes('/18/')) {
        counter += 1;
      }
    }
  }
  console.log(counter);
}

request.get(url, processResponse);
