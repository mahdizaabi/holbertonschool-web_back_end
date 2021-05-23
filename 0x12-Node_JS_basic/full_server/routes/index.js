const express = require('express');

const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

const router = express.Router();
router.get('/', AppController.getHomepage);

router.get('/students', (req, res) => StudentsController.getAllStudents(req, res, process.argv[2]));
router.get('/students/:major', (req, res) => StudentsController.getAllStudentsByMajor(req, res, process.argv[2]));

export default router;
