import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    if (typeof floors !== 'number') {
      throw new TypeError('floors must be a number');
    }
    super(sqft);
    this._floors = floors;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    if (typeof newSqft !== 'number') {
      throw new TypeError('newSqft must be a number');
    }
    this._sqft = newSqft;
  }

  get floors() {
    return this._floors;
  }

  set floors(newFloors) {
    if (typeof newFloors !== 'number') {
      throw new TypeError('newFloors must be a number');
    }

    this._floors = newFloors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
