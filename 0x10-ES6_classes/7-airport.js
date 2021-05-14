export default class Airport {
  constructor(name, code) {
    this.name = name;
    this.code = code;
  }

  set name(value) {
    this._name = value;
  }

  get name() {
    return this._name;
  }

  set code(value) {
    this._code = value;
  }

  get code() {
    return this._code;
  }

  get [Symbol.toStringTag]() {
    return this._code;
  }
}
