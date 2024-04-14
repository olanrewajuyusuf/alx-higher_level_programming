#!/usr/bin/node
const list = require('./100-data.js').list;

const newArr = list.map((ele, ind) => ele * ind);
console.log(list);
console.log(newArr);
