#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

try {
  // Read contents of fileA and fileB
  const contentA = fs.readFileSync(fileA, 'utf8');
  const contentB = fs.readFileSync(fileB, 'utf8');

  // Concatenate contents
  const concatenatedContent = contentA + contentB;

  // Write concatenated content to fileC
  fs.writeFileSync(fileC, concatenatedContent);

} catch (err) {
  console.error(`Error: ${err.message}`);
  process.exit(1);
}
