const express = require('express');

const app = express();
const port = 7865;
const onListen = `API available on localhost port ${port}`;
const welcomeMessage = 'Welcome to the payment system';
app.get('/', (req, res) => {
    res.send(welcomeMessage);
});

app.get('/cart/:id', (req, res) => {
    const { id } = req.params;
    if (!isNaN(id))
        res.send(`Payment methods for cart ${id}`);
    else
        res.status(404).send();
});

app.listen(port, () => { console.log(onListen) });
module.exports = app;