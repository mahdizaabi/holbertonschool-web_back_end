const express = require('express');
const dataQuery = require('./3-read_file_async');

const filename = process.argv[2];

const app = express();
app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});
app.get('/students', (req, response, next) => {
  dataQuery(filename).then(({
    listCs, nCs, listSwe, nSwe,
  }) => {
    const studentsCount = nCs + nSwe;
    response.send(`This is the list of our students\n
    Number of students: ${studentsCount}\n
    Number of students in CS: ${nCs}. List: ${listCs}\n
    Number of students in SWE: ${nSwe}. List: ${listSwe}
    `);
  }).catch((error) => next(error));
});
const port = 1245;
app.listen(port);
module.exports = app;
