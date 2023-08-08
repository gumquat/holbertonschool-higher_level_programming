#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Request failed with status:', response.statusCode);
    return;
  }

  fs.writeFile(filePath, body, { encoding: 'utf8' }, (err) => {
    if (err) {
      console.error(err);
      return;
    }

    console.log('Webpage content saved to file:', filePath);
  });
});
