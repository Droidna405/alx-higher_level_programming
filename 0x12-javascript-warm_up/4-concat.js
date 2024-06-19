#!/usr/bin/node

const myArguments = process.argv.slice(2);
if (!myArguments[0]) {
    console.log("undefined is undefined");
}
else {
    console.log(myArguments[0], 'is', myArguments[1]);
}
