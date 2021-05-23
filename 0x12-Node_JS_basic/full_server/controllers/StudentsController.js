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
    if (request.params.major !== 'CS' && request.params.major !== 'SWE') {
      response.send(500, 'Major parameter must be CS or SWE');
    } else {
      readDatabase(filename).then(({ cs, swe }) => {
        if (request.params.major === 'SWE') response.status(200).send(`List: ${swe.join(', ')}`);
        else response.status(200).send(`List: ${cs.join(', ')}`);
      }).catch(() => {
        response.status(500).send('Cannot load the database');
      });
    }
  }
}
module.exports = StudentsController;
export default StudentsController;
