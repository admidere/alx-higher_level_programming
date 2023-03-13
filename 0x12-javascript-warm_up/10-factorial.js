#!/usr/bin/node

function factorize(num) {
  if (!num || num < 0 || num == 0) {
    return (1);
  } else {
    return (num * factorize(num - 1));
  }
}

console.log(factorize(process.argv[2]));
