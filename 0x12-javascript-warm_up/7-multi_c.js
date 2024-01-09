#!/usr/bin/node
let i = 0;
const num = process.argv[2];
if (typeof num !== 'number') {
  console.log('Missing number of occurence');
} while (i < num) {
  console.log('C is fun');
  i++;
}
