export default class Building {
  constructor(sqft) {
    {
      const proto = Object.getPrototypeOf(this);
      const superProto = Building.prototype;
      /*eslint-disable */
      const missing = Object.getOwnPropertyNames(superProto).find((name) => typeof superProto[name] === 'function' && !proto.hasOwnProperty(name));
      if (missing) throw new TypeError('Class extending Building must override evacuationWarningMessage');
    }
    this.sqft = sqft;
  }

  evacuationWarningMessage() {
    return this._sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('Sqft must be a number');
    }
    this._sqft = sqft;
  }
}
