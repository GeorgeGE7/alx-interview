#!/usr/bin/node

const request = require("request");

const filmNumber = process.argv[2] + "/";
const baseUrl = "https://swapi-api.hbtn.io/api/films/";

// Get film data and information
request(baseUrl + filmNumber, async function (reqError, res, bodyData) {
  if (reqError) return console.error(reqError);

  // Parse the response data (JSON) to get the list of character URLs
  const cUrlList = JSON.parse(bodyData).characters;

  // Iterate through the character URLs and fetch character information
  // Make a request to each character URL
  for (const cUrl of cUrlList) {
    await new Promise(function (resolve, reject) {
      request(cUrl, function (err, res, body) {
        if (err) return console.error(err);

        // Parse the charcter nformation and print the character's name Resolve the promise to indicate completion
        console.log(JSON.parse(body).name);
        resolve();
      });
    }).catch(function (err) {
      console.error(err);
    });
  }
});
