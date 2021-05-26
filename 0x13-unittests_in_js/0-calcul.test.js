const assert = require('assert');
const calculateNumber = require('./0-calcul');





describe('calculateNumber', function () {
  it('should return 20 when values are 4 et 2', function () {
    assert.equal(calculateNumber(4, 2.8), 7);
  });
  it('should return NAN when second arg is of type String', function () {
    assert.ok(isNaN(calculateNumber(14, "str")));
  });
  it('should return NAN when first arg is of type String', function () {
    assert.ok(isNaN(calculateNumber("str", 14, 2)));
  });
  it('should return NAN when both arguments are of type String', function () {
    assert.ok(isNaN(calculateNumber("str", "str")));
  });
  
});