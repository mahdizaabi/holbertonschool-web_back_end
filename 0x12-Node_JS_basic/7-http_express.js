const express = require('express');
const dataQuery = require('./3-read_file_async');

const filename = process.argv[2];

const app = express();
app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});
app.get('/students', (req, response) => {
  dataQuery(filename).then(({ httpResponse }) => {
    response.send(`This is the list of our students\n${httpResponse.join('\n')}`);
  }).catch((error) => {
    response.send(`This is the list of our students\n${error.message}`);
  });
});
const port = 1245;
app.listen(port);
module.exports = app;
