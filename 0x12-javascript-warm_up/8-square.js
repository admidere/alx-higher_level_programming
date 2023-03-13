#!/usr/bin/node

const index = Number.parseInt(process.argv[2], 10);
if (isNaN(index)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < index; i++) {
    let row = '';
    for (let j = 0; j < index; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
