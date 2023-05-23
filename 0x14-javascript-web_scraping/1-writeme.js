#!/usr/bin/node

const fs = require('fs');

function writeToFile(filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    } else {
      console.log(`Successfully wrote to file: ${filePath}`);
    }
  });
}

// Usage: node script.js <file_path> <content>
const filePath = process.argv[2];
const content = process.argv[3];
writeToFile(filePath, content);
