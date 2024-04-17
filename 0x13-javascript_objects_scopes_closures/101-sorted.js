#!/usr/bin/node
const dict = require('./101-data.js').dict;

const vals = Object.values(dict);
const keys = Object.keys(dict);
let res = {};
for (let i = 0; i < vals.length; i++) {
 res[vals[i]] = keys.filter(key => dict[key] === vals[i]);
}
console.log(res);
