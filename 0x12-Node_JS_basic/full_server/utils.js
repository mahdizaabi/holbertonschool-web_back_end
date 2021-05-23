const fs = require('fs');

function readDatabase(path) {
  const csList = [];
  const sweList = [];
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error(err));
        return;
      }
      const lines = data.split(/\r?\n/);
      lines.forEach((line) => {
        if (line.includes('CS')) {
          csList.push(line.split(', ')[0]);
        } else if (line.includes('SWE')) {
          sweList.push(line.split(', ')[0]);
        }
      });

      resolve({
        cs: csList,
        swe: sweList,
      });
    });
  });
}
export default readDatabase;
