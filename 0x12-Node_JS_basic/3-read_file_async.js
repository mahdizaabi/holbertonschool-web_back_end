const readFile = require('fs/promises');

function countStudents(fileName) {
  return new Promise((resolve, reject) => {
    try {
      const csList = [];
      const sweList = [];
      readFile.readFile(fileName, 'UTF-8').then((data) => {
        const lines = data.split(/\r?\n/);
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
        resolve(data);
      }).catch(() => reject(new Error('Cannot load the database')));
    } catch (e) {
      console.log(e);
    }
  });
}

module.exports = countStudents;
