const express = require('express');

const app = express();
const countStudents = require('./3-read_file_async');

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const databaseCSV = process.argv[2];
  countStudents(databaseCSV)
    .then((data) => {
      res.send(`This is the list of our students\n${data}`);
    })
    .catch(() => {
      res.send('Cannot load the database');
    });
});

app.listen(1245);
module.exports = app;
