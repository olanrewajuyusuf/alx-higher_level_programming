#!/usr/bin/node
exports.esrever = function (list) {
  let res = [];
  let len = list.length - 1;
  while (let i = len; i >= 0; i--) {
    res.push(list[i]);
  }
  return res;
};
