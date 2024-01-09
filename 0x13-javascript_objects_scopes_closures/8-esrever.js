#!/usr/bin/node
exports.esrever = function (list) {
  let j = list.length - 1;
  const n = [];
  while (j >= 0) {
    n.push(list[j]);
    j--;
  }
  return n;
};
