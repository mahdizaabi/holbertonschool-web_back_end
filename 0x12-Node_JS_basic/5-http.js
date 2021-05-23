const http = require('http');
const databaQuery = require('./3-read_file_async');

const filename = process.argv[2];
const app = http.createServer();
app.on('request', (request, response) => {
  if (request.method === 'GET' && request.url === '/students') {
    databaQuery(filename).then(({ httpResponse }) => {
      response.writeHead(200, { 'Content-Type': 'text/plain' });
      response.end(`This is the list of our students\n${httpResponse.join('\n')}`);
    }).catch((e) => {
      response.write('This is the list of our students\n');
      response.end(e.message);
    });
  } else {
    const body = 'Hello Holberton School!';
    response
      .writeHead(200, {
        'Content-Type': 'text/plain',
      });
    response.write(body);
    response.end();
  }
});
app.listen(1245);
module.exports = app;
