#!/usr/bin/node
const fa = require('fs');

const fArg = fs.readFileSync(process.argv[2]).toString();
const sArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fArg + sArg);
