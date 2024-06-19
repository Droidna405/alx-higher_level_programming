#!/usr/bin/node

// Function that adds two numbers
function add (a, b) {
  return a + b;
}

// Retrieve the arguments, skipping the first two elements
const args = process.argv.slice(2);

// Convert the arguments to integers
const firstInt = parseInt(args[0], 10);
const secondInt = parseInt(args[1], 10);

// Check if the arguments are valid numbers and perform addition
if (isNaN(firstInt) || isNaN(secondInt)) {
  console.log('NaN');
} else {
  console.log(add(firstInt, secondInt));
}
