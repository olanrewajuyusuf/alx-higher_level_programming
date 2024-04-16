#!/usr/bin/node

const {writeFile, readFileSync} = require('fs');
const {argv} = require('process');

const fileA = readFileSync(argv[2], 'utf8');
const fileB = readFileSync(argv[3], 'utf8');

writeFile(argv[4], `${fileA} ${fileB}`, 'utf8', err => {
  if (err) throw err;
});
