#!/usr/bin/node
const fs = require('fs');

function writeFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  }
  );
}

const filePath = process.argv[2];
const content = process.argv[3];

writeFile(filePath, content);
