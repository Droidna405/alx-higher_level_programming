#!/usr/bin/node

// Define the function that will be exported
exports.callMeMoby = function (x, theFunction) {
  // Loop x times
  for (let i = 0; i < x; i++) {
    // Call the provided function
    theFunction();
  }
};
