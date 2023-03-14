#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurr = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurr += 1;
    }
  }
  return occurr;
};
