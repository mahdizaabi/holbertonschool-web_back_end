import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response, filename) {
    readDatabase(filename).then((data) => {
      const message = [];
      const welcomeMessage = 'This is the list of our students';
      for (const [key, value] of Object.entries(data)) {
        message.push(`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
      }
      response.status(200).send(`${welcomeMessage}\n${message.join('\n')}`);
    }).catch(() => {
      response.status(500).send('Cannot load the database');
    });
  }

  static getAllStudentsByMajor(request, response, filename) {
    if (request.params.major !== 'CS' && request.params.major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
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
