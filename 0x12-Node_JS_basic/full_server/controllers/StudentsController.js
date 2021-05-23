const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(request, response, filename) {
    readDatabase(filename).then(({ cs, swe }) => {
      response.send(200, `This is the list of our students
Number of students in CS: ${cs.length}. List: ${cs.join(', ')}
Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
    }).catch((error) => {
      response.send(200, `This is the list of our students\n${error.message}`);
    });
  }

  static getAllStudentsByMajor(request, response, filename) {
    readDatabase(filename).then(({ cs, swe }) => {
      if (request.params.major === 'CS' || request.params.major === 'SWE') {
        if (request.path === 'SWE') response.send(`List: ${swe.join(', ')}`);
        else response.send(`List: ${cs.join(', ')}`);
      } else {
        response.send(500, 'Major parameter must be CS or SWE');
      }
    }).catch((error) => {
      response.send(500, `This is the list of our students\n${error.message}`);
    });
  }
}
module.exports = StudentsController;
