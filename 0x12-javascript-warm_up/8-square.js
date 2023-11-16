#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing x');
} else {
  for (let r = 0; r < x; r++) {
    let raid = '';
    for (let i = 0; i < x; i++) raid += 'X';
    console.log(raid);
  }
}
