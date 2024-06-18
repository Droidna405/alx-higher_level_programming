#!/usr/bin/node
const { dict } = require('./101-data');

// Initialize an empty object to store the new dictionary
const occurrencesDict = {};

// Iterate over the original dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  // Check if the occurrences key exists in the new dictionary
  if (occurrences in occurrencesDict) {
    occurrencesDict[occurrences].push(userId);
  } else {
    occurrencesDict[occurrences] = [userId];
  }
}

// Print the new dictionary
console.log(occurrencesDict);
