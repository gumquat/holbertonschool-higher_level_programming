#!/usr/bin/node
const fs = require('fs');

function readFile (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}

// if no filepath is provided this looks for one
// and then reads the file as normal using the readFile func
const filePath = process.argv[2];

if (!filePath) {
  console.error(err);
} else {
  readFile(filePath);
}
