#!/usr/bin/node
const i = process.argv[2];
if (isNaN(parseInt(i))) {
  console.log('Not a number');
}
else {
  console.log(i);}
