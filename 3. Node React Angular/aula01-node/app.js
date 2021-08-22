const http = require('http')

http.createServer(function (req, res) {
  res.end('<h1>Hello, world!</h1>');
}).listen(3000);

console.log('Server up and runnig')