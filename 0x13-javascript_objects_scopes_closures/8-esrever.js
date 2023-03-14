#!/usr/bin/node

exports.esrever = function (list) {
  const rever = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    rever[i] = list[j];
    j++;
  }
  return (rever);
};
