#!/usr/bin/node

const request = require('request');
const { createWriteStream } = require('fs');

request(process.argv[2]).pipe(createWriteStream(process.argv[3]));
