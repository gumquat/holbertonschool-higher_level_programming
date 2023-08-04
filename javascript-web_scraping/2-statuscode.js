#!/usr/bin/node
const request = require('request');

function getRequestStatusCode (url) {
  request.get(url, (err, response, body) => {
    if (err) {
      console.log(err);
    }
    console.log('code: ' + response.statusCode);
  });
}

const url = process.argv[2];

getRequestStatusCode(url);
