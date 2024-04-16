#!/usr/bin/node

const {writeFile, readFile} = require('fs');
const {argv} = require('process');

const fileA = readFile(argv[2], 'utf8');
const fileB = readFile(argv[3], 'utf8');

writeFile(argv[4], `${fileA} ${fileB}`, 'utf8', err => {
  if (err) throw err;
});
