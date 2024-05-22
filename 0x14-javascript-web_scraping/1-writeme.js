#!/usr/bin/node

const { writeFile } = require('fs');
const file = process.argv[2];
const text = process.argv[3];

writeFile(file, text, (err, result) => {
  if (err) {
    console.log(err);
    return;
  }
});
