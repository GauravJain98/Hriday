const express = require('express');
const hbs = require('hbs');
const bodyParser = require('body-parser');
const { hashGen } = require('./ipfsHashGeneration');
const axios  = require('axios');

const port = process.env.PORT || 3000;

const app = express();

app.set('view engine', 'hbs');

app.use(express.static(`${__dirname}/`));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

obj = {
    a: 1,
    b: 2
};

app.get('/', (req, res) => {
    res.send(obj);
});


// app.post('/home', (req, res) => {
// });

app.listen(port, () => {
    console.log(`Server is up on port ${port}`);
});
