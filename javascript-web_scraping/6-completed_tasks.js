#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let counter = 0;
const dictionary = {};
let user = 0;

request.get(url, (err, response, body) => {
  if (err) return console.log(err);
  if (response.statusCode !== 200){
    console.log(err);
}
  const data = JSON.parse(body);
  data.reduce((acc, task) => {
    if (user !== task.userId) {
      user = task.userId;
      counter = 0;
    }
    if (task.completed) {
      counter++;
    }
    if (counter !== 0) {
      dictionary[user] = counter;
    }
    return acc;
  }, {});
  
  console.log(dictionary);
});