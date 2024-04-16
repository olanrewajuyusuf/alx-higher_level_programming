#!/usr/bin/node

const {writeFile, readFile} = require('fs');
const args = process.argv;

const fileA = readFile(args[2], 'utf8');
const fileB = readFile(args[3], 'utf8');

writeFile(args[4], `${fileA} ${fileB}`, 'utf8');
