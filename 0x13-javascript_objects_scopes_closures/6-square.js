#!/usr/bin/node
const Sq = require('./5-square.js');
class Square extends Sq {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(String(c).repeat(this.width));
      }
    } else {
      for (let j = 0; j < this.height; j++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
