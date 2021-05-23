import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response, filename) {
    readDatabase(filename).then(({ cs, swe }) => {
      response.status(200).send(`This is the list of our students
Number of students in CS: ${cs.length}. List: ${cs.join(', ')}
Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
    }).catch(() => {
      response.status(500).send('Cannot load the database');
    });
  }

  static getAllStudentsByMajor(request, response, filename) {
    readDatabase(filename).then(({ cs, swe }) => {
      if (request.params.major === 'CS' || request.params.major === 'SWE') {
        if (request.params.major === 'SWE') response.status(200).send(`List: ${swe.join(', ')}`);
        else response.status(200).send(`List: ${cs.join(', ')}`);
      } else {
        response.status(500).send('Major parameter must be CS or SWE');
      }
    }).catch(() => {
      response.status(500).send('Cannot load the database');
    });
  }
}
module.exports = StudentsController;
export default StudentsController;
