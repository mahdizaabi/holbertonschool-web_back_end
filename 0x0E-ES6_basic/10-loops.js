export default function appendToEachArrayValue(array, appendString) {
  const arrx = [];
  for (const string of array) {
    arrx.push(appendString + string);
  }

  return arrx;
}
