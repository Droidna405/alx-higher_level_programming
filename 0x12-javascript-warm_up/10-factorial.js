#!/usr/bin/node

// Recursive function to compute factorial
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

// Get the argument from the command line
const args = process.argv.slice(2);
const number = parseInt(args[0]);

// Check if the input is NaN, if so, use 1
const result = isNaN(number) ? 1 : factorial(number);

// Print the result
console.log(result);
