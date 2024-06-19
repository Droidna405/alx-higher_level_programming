#!/usr/bin/node

// Retrieve the first argument after the script name
const arg = process.argv[2];

// Convert the argument to an integer
const num = parseInt(arg);

// Check if the conversion result is a number and print accordingly
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}
