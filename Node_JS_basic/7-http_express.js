const express = require('express');
const app = express();
const countStudents = require('./3-read_file_async');

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.write('This is the list of our students');
  countStudents(dataBase)
});

app.listen(1245);
module.exports = app;
