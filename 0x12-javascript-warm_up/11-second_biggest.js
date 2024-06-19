#!/usr/bin/node

// Retrieve command-line arguments and ignore the first two
const args = process.argv.slice(2);

// Handle cases where there are no or only one argument
if (args.length < 2) {
  console.log(0);
} else {
  // Convert arguments to integers and sort them in descending order
  const numbers = args.map(Number).sort((a, b) => b - a);

  // The second largest number is the second element in the sorted array
  console.log(numbers[1]);
}
