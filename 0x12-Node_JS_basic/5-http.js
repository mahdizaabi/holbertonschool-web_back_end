const http = require('http');
const databaQuery = require('./3-read_file_async');

const filename = process.argv[2];
const app = http.createServer();
app.on('request', (request, response) => {
  if (request.method === 'GET' && request.url === '/students') {
    databaQuery(filename).then(({
      listCs, nCs, listSwe, nSwe,
    }) => {
      const studentsCount = nCs + nSwe;
      response.write('This is the list of our students\n');
      response.write(`Number of students: ${studentsCount}\n`);
      response.write(`Number of students in CS: ${nCs}. List: ${listCs}\n`);
      response.write(`Number of students in SWE: ${nSwe}. List: ${listSwe}\n`);
      response.end();
    });
    response.writeHead(200, { 'Content-Type': 'text/plain' });
  } else {
    const body = 'Hello Holberton School!';
    response
      .writeHead(200, {
        'Content-Length': Buffer.byteLength(body),
        'Content-Type': 'text/plain',
      })
      .end(body);
  }
});
app.listen(1245);
module.exports = app;
