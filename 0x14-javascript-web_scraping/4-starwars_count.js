#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (!err) {
    const results = JSON.parse(body).results;
    const total = results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/')) ? count + 1 : count;
    }, 0);
    console.log(total);
  }
});
