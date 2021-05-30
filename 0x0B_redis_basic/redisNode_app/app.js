const express = require('express');
const path = require('path')
const logger = require('morgan')
const bodyParser = require('body-parser');
const redis = require('redis');
const fs = require('fs');

const redisClient = require('./redis')

const app = express()
app.set('strict routing', false);
const dirPath = path.join(__dirname, '..', '..', 'directoryX');
/* /home/vagrant/holbertonschool-web_back_end/directoryX -> 2 directories up  */
console.log(dirPath)

const HOMEDIR = path.join(__dirname, '..', '..');
console.log(HOMEDIR)

/*fs.mkdirSync(dirPath);*/

const client = new redisClient();
// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

/* serve static file  */
app.use('/static', express.static('public'))

app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.get('/', function (req, res) {
    var title = 'Task List';
    client.getList('taskList').then(data => {
        console.log(data)
        res.render('1', { tasks: data })
    }).catch((error) => res.end(error))

});
app.get('/vv', (req, res) => {
    res.render('2', { title: 'myvariable2' })
    res.end()
})
app.post('/task/delete', (req, res) => {
    if (!req.body) res.redirect('/')

    if (!req.body.tasksToRemove) {
        res.redirect('/');
    }

    if (!Array.isArray(req.body.tasksToRemove) && req.body.tasksToRemove) {
        client.removeItemFromList('taskList', 1, req.body.tasksToRemove);
        res.redirect('/');
    }
    req.body.tasksToRemove.forEach((item) => {
        client.removeItemFromList('taskList', 1, item)
    })

    console.log(req.body);
    res.redirect('/');
});
app.post('/addNewTask', (req, res) => {
    const { task } = req.body;
    console.log(task)

    if(task) {
        client.addItemToList('taskList', task);
    }
    res.redirect('/');

})


app.listen(3000, () => {
    console.log('server is running on port 3000');
});
module.exports = app;