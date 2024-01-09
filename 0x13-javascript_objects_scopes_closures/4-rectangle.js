#!/usr/bin/node
class Rectangle{
  constructor (w, h) {
  if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
  return this;
    }
  }
  print() {
    for (let j = 0; j < this.height; j++) {
    console.log('X'.repeat(this.width))
    }
  }
  rotate() {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  double() {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
