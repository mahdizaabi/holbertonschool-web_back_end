import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this.sqft = sqft;
    this.floors = floors;
  }

  get floors() {
    return this._floors;
  }

  set floors(floors) {
    this._floors = floors;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(sqft) {
    this._sqft = sqft;
  }

  evacuationWarningMessage() {
    this.x = 14;
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
