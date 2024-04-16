#!/usr/bin/node

const {writeFile, readFile} = require('fs');
const args = process.argv;

if (args.length === 4) {
  const fileA = readFile(args[1], 'utf8');
  const fileB = readFile(args[2], 'utf8');

  writeFile(args[4], `${fileA}\n${fileB}`);
  console.log(readFileSync(args[3], "utf8"));
}
