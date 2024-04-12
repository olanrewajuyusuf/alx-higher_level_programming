#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += 'X';
      }
      console.log(x);
    }
  }
  
  double () {
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    const width = this.height;
    const height = this.width;
    this.height = height;
    this.width = width;
  }
}

module.exports = Rectangle;
