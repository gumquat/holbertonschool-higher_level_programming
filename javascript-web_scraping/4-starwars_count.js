#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let counter = 0;

function get(url) {
  return new Promise((resolve, reject) => {
    request.get(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else if (res.statusCode !== 200) {
        reject(new Error(`Request failed with status: ${res.statusCode}`));
      } else {
        resolve(body);
      }
    });
  });
}

async function countCharacters() {
  try {
    const body = await get(url); // async operation
    const data = JSON.parse(body).results;
    
    for (const film of data) {
      for (const character of film.characters) {
        if (character.includes('/18/')) {
          counter++;
        }
      }
    }
    
    console.log(counter);
  } catch (error) {
    console.error(error.message);
  }
}

countCharacters();
