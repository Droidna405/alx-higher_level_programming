#!/usr/bin/node

const args = process.argv.slice(2); // Get the arguments excluding the node and script paths
const size = parseInt(args[0], 10); // Parse the first argument as an integer

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
