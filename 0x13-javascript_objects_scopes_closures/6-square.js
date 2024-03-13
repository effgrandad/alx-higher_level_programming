#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (z) {
    if (z === undefined) {
      z = 'X';
    }
    for (let f = 0; f < this.height; f++) {
      let a = '';
      for (let g = 0; g < this.width; g++) {
        a += z;
      }
      console.log(a);
    }
  }
}

module.exports = Square;
