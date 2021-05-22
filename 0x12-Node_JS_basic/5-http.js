const http = require('http');
const fs = require('fs');

const filename = process.argv[2];
const app = http.createServer();
app.on('request', (request, response) => {
  request.on('error', (err) => {
    response.statusCode = 404;
    response.end(err.message);
  });
  const csList = [];
  const sweList = [];
  if (request.method === 'GET' && request.url === '/students') {
    fs.readFile(filename, 'utf8', (err, data) => {
      if (err) {
        response.statusCode = 404;
        response.end(err.message);
      }
      response.writeHead(200, { 'Content-Type': 'text/plain' });
      const lines = data.split(/\r?\n/);
      lines.forEach((line) => {
        if (line.includes('CS')) {
          csList.push(line.split(',')[0]);
        } else if (line.includes('SWE')) {
          sweList.push(line.split(',')[0]);
        }
      });
      const studentsCount = csList.length + sweList.length;
      response.write('This is the list of our students\n');
      response.write(`Number of students: ${studentsCount}\n`);
      response.write(`Number of students in CS: ${csList.length}. List: ${csList.join(', ')}\n`);
      response.write(`Number of students in SWE: ${sweList.length}. List: ${sweList.join(', ')}`);
      response.end();
    });
  } else {
    const body = 'Hello Holberton School!';
    response.writeHead(200, {
      'Content-Type': 'text/plain',
    });
    response.write(body);
    response.end();
  }
});
app.listen(1245);
module.exports = app;
