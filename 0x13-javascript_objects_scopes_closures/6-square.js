#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let counter = 0; counter < this.height; counter++) console.log(c.repeat(this.width));
    }
  }
};
