const express = require('express');

const app = express();

app.get('/', function(req, res) {
  res.send('Hello world');
});

app.get('/test', function(req, res) {
  student = 'Gabriel'
  res.send('Hello, '+ student);
});

app.listen(3000)

console.log('Server runing')