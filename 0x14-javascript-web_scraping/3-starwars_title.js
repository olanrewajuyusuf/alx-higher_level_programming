#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/:id', function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
