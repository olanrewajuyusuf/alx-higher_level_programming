#!/usr/bin/node

const {writeFile, readFile} = require('fs');
const args = process.argv;

if (args.length === 5) {
  const fileA = readFile(args[2], 'utf8');
  const fileB = readFile(args[3], 'utf8');

  writeFile(args[4], `${fileA}\n${fileB}`);
  console.log(readFileSync(args[4], "utf8"));
}
