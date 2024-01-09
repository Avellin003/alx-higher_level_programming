#!/usr/bin/node
function fac (i) {
  return i === 0 || isNaN(i) ? 1 : i * fac(i - 1);
}
console.log(fac(Number(process.argv[2])));
