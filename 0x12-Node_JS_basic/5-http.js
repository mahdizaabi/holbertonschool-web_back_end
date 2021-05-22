const http = require('http');
const fs = require('fs');

const filename = process.argv[2];
const app = http.createServer();
app.on('request', (request, response) => {
  const csList = [];
  const sweList = [];
  if (request.method === 'GET' && request.url === '/students') {
    response.writeHead(200, { 'Content-Type': 'text/plain' });
    fs.readFile(filename, 'utf8', (err, data) => {
      const lines = data.split(/\r?\n/);
      lines.forEach((line) => {
        if (line.includes('CS')) {
          csList.push(line.split(',')[0]);
        } else if (line.includes('SWE')) {
          sweList.push(line.split(',')[0]);
        }
      });
      const studentsCount = csList.length + sweList.length;
      response.write('this is the list of the students\n');
      response.write(`Number of students: ${studentsCount}\n`);
      response.write(`Number of students in CS: ${csList.length}. List: ${csList.join(', ')}\n`);
      response.write(`Number of students in SWE: ${sweList.length}. List: ${sweList.join(', ')}`);
      response.end();

      response.on('error', (err) => {
        console.log(err);
      });
    });
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
