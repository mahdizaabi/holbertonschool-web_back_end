export default function createIteratorObject(report) {
  let iterable = [];

  iterable = {
    * [Symbol.iterator]() {
      for (const value of Object.values(report.allEmployees)) {
        for (const i of value) {
          yield i;
        }
      }
    },
  };

  return iterable;
}
