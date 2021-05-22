const http = require('http');

const app = http.createServer();
app.on('request', (request, response) => {
  const body = 'Hello Holberton School!';
  response
    .writeHead(200, {
      'Content-Length': Buffer.byteLength(body),
      'Content-Type': 'text/plain',
    })
    .end(body);
});
app.listen(1245);
module.exports = app;
