const readFile = require('fs/promises');

function countStudents(fileName) {
  const csList = [];
  const sweList = [];
  try {
    const promise = readFile.readFile(fileName);
    promise.then((data) => {
      const lines = data.toString().split(/\r?\n/);
      lines.forEach((line) => {
        if (line.includes('CS')) {
          csList.push(line.split(',')[0]);
        } else if (line.includes('SWE')) {
          sweList.push(line.split(',')[0]);
        }
      });
      const studentsCount = csList.length + sweList.length;
      console.log(`Number of students: ${studentsCount}`);
      console.log(`Number of students in CS: ${csList.length}. List: ${csList.join(', ')}`);
      console.log(`Number of students in SWE: ${sweList.length}. List: ${sweList.join(', ')}`);
    });
    return promise;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
