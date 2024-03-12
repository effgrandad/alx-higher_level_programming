#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = height;
    }
  }

  print () {
    for (let f = 0; f < this.height; f++) {
      let s = '';
      for (let g = 0; g < this.width; g++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
