const assert = require('assert');
const calculateNumber = require('./0-calcul');





describe('calculateNumber', function () {
  const testAddition = ({args, expected}) => function() {
    assert.strictEqual(calculateNumber(...args), expected);    
  }
  it('should return 8 when values are 4 et 2', testAddition({args: [2.1, 6], expected: 8}))
  it('should return 9 when values are 4 et 2', testAddition({args: [2.8, 6], expected: 9}))
  it('should return 8 when values are 4 et 2', testAddition({args: [2, 6], expected: 8}))
  it('should return 8 when values are 4 et 2', testAddition({args: [2, 6], expected: 8}))
  it('should return 8 when values are 4 et 2', testAddition({args: [14.0, 14.9], expected: 29}))
  it('should return 8 when values are 4 et 2', testAddition({args: [0.8, 0.8], expected: 2}))
  it('should return 8 when values are 4 et 2', testAddition({args: [0, 0.2], expected: 0}))
  it('should return 8 when values are 4 et 2', testAddition({args: [0, 0.2], expected: 0}))
  it('should return 8 when values are 4 et 2', testAddition({args: [0, 0.2], expected: 0}))
  it('should return 8 when values are 4 et 2', testAddition({args: [0, 0.2], expected: 0}))


  it('should return 20 when values are 4 et 2', function () {
    assert.strictEqual(calculateNumber(4, 2.8), 7);
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