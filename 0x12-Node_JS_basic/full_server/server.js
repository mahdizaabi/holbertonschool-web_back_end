import router from './routes/index';

const express = require('express');

const app = express();
app.use('/', router);

const port = 1245;
app.listen(port);

export default app;
