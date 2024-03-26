#!/usr/bin/node
const fs = require('fs');
const reqUrl = process.argv[2];
const filePath = process.argv[3];
const request = require('request');
request(reqUrl).pipe(fs.createWriteStream(filePath));
