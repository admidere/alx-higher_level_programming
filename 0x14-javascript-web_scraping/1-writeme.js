#!/usr/bin/node

const fs = require('fs');

function writeContent (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    } else {
      console.log('secussefuly added content to file: $(filePath)');
    }
  });
}

const filePath = process.argv[2];
const content = process.argv[3];
writeContent(filePath, content);
