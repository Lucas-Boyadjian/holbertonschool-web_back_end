const http = require('http');
const querystring = require('querystring');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  }
  if (req.url === '/')
});



app.listen(1245)

module.exports = app;
