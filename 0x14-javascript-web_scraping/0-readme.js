#!/usr/bin/node

const { readFile } = require('fs');

readFile(process.argv[2], 'utf8', (err, result) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(result);
});
