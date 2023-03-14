#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let mat = '';
        for (let j = 0; j < this.width; j++) {
          mat += c;
        }
        console.log(mat);
      }
    }
  }
}
module.exports = Square;
