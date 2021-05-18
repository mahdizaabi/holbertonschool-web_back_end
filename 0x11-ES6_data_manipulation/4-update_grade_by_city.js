const x = (arr, city, newGrades) => {
  const tempObj = {};
  newGrades.forEach((element) => { tempObj[element.studentId] = element; });
  return arr.map((item) => ({ ...item, grade: (tempObj[item.id] && (tempObj[item.id].grade)) || 'N/A' })).filter((item) => item.location === city);
};
export default x;
