#!/usr/bin/node

const number = Number.parseInt(process.argv[2], 10);
if (!isNaN(number)) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
