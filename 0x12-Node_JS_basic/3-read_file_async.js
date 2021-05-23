const fs = require('fs');

function countStudents(path) {
  const csList = [];
  const sweList = [];
  const dataSend = [];

  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }
      const lines = data.split(/\r?\n/);
      lines.forEach((line) => {
        if (line.includes('CS')) {
          csList.push(line.split(',')[0]);
        } else if (line.includes('SWE')) {
          sweList.push(line.split(',')[0]);
        }
      });
      const studentsCount = csList.length + sweList.length;
      const listCs = csList.join(', ');
      const nCs = csList.length;
      const listSwe = sweList.join(', ');
      const nSwe = sweList.length;

      dataSend.push(`Number of students: ${studentsCount}\n`);
      dataSend.push(`Number of students in CS: ${csList.length}. List: ${csList.join(', ')}\n`);
      dataSend.push(`Number of students in SWE: ${sweList.length}. List: ${sweList.join(', ')}\n`);
      for (const data of dataSend) {
        process.stdout.write(data);
      }
      resolve({
        listCs, nCs, listSwe, nSwe, dataSend,
      });
    });
  });
}

module.exports = countStudents;
