#!/usr/bin/node

const args = process.argv.slice(2); // Get command-line arguments starting from index 2
const x = parseInt(args[0], 10); // Convert the first argument to an integer

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
