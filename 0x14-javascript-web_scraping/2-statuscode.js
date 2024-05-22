#!/usr/bin/node
const request = require('request');

request
  .get('http://google.com/img.png')
  .on('response', function(response) {
    console.log(response.statusCode);
  });
