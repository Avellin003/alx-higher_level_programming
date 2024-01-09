#!/usr/bin/node
const i = process.argv[2];
if (!i) {
  console.log('No argument');
} else if (i) {
  console.log(i);
}
