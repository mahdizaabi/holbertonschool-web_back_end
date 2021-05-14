export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw new TypeError('name must be a string');
    if (typeof length !== 'number') throw new TypeError('Length must be a number');
    if (!Array.isArray(students)) throw new TypeError('students must be an array');
    for (const std of students) {
      if (typeof std !== 'string') throw new TypeError('std must be a string');
    }
    this.name = name;
    this.length = length;
    this.students = students;
  }

  // name
  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof (name) === 'string') {
      this._name = name;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  get length() {
    return this._length;
  }

  set length(length) {
    if (typeof length === 'number') {
      this._length = length;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  get students() {
    return this._students;
  }

  set students(students) {
    if (Array.isArray(students) && ((students.find((s) => typeof s !== 'string')) === 'undefined')) {
      this._students = students;
    } else {
      throw new TypeError('students must be an array of strings');
    }
  }
}