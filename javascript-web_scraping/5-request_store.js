#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let counter = 0;

function promisify (fn) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      fn(...args, (err, res) => {
        if (err) return reject(err);
        resolve(res);
      });
    });
  };
}

async function processRequest () {
  try {
    const get = promisify(request.get);
    const { body, statusCode } = await get(url);

    if (statusCode !== 200) {
      console.error('Request failed with status:', statusCode);
      return;
    }

    const data = JSON.parse(body).results;
    for (const film of data) {
      for (const character of film.characters) {
        if (character.includes('/18/')) {
          counter += 1;
        }
      }
    }
    console.log(counter);
  } catch (err) {
    console.error(err);
  }
}

processRequest();
