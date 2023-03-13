#!/usr/bin/node

const index = Number.parseInt(process.argv[2], 10);
if (!isNaN(index)) {
  for (let i = 0; i < index; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
