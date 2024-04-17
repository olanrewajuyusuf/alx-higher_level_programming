#!/usr/bin/node

const {writeFile, readFileSync} = require('fs');
const {argv} = require('process');

const getContent = (file) => {
  return readFileSync(file, 'utf8');
};

const concat = getContent(argv[2]) + '' + getContent(argv[3]);

writeFile(argv[4], concat, 'utf8', err => {
  if (err) throw err;
});
