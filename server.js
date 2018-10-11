const express = require('express');
const bodyParser = require('body-parser');

const port = process.env.PORT || 5000;

const app = express();

app.use(express.static(`${__dirname}/`));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.redirect('/home');
});

app.get('/home', (req, res) => {
});

app.post('/home', (req, res) => {
    console.log(req.body);
    res.redirect('/home');
});

app.listen(port, () => {
    console.log(`Server is up on port ${port}`);
});
