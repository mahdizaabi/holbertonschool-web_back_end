const fs = require('fs');

function countStudents(pathFile) {
  const csList = [];
  const sweList = [];
  try {
    // read contents of the file
    const data = fs.readFileSync(pathFile, 'UTF-8');
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
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
