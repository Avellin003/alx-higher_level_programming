#!/usr/bin/node
const i = process.argv[2];
if (isNaN(i)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < i; j++) {
  console.log('x'.repeat(i));
  }
}
