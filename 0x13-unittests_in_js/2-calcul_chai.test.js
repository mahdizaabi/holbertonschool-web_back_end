const chai = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('Add()', function () {
    const tests = [
        { args: ["SUM", 1, 2], expected: 3 },
        { args: ["SUM", 3, 3], expected: 6 },
        { args: ["SUM", 7, 3], expected: 10 }
    ];
    tests.forEach(({ args, expected }) => {
        it(`correctly add ${args[1]} and ${args[2]} args`, function () {
            const res = calculateNumber(...args);
            chai.expect(res).to.equal(expected);
        });
    });
});

describe('Substract()', function () {
    const tests = [
        { args: ["SUBTRACT", 2.2, 1.1], expected: 1 },
        { args: ["SUBTRACT", 2.8, 1.1], expected: 2 },
        { args: ["SUBTRACT", 2.0, 1.9], expected: 0 }
    ];
    tests.forEach(({ args, expected }) => {
        it(`correctly Substract ${args[1]} and ${args[2]}`, function () {
            const res = calculateNumber(...args);
            chai.expect(res).to.equal(expected);
        });
    });
});

describe('Division()', function () {
    const tests = [
        { args: ["DIVIDE", 2.2, 1.1], expected: 2 },
        { args: ["DIVIDE", 2.8, 1.1], expected: 3 },
        { args: ["DIVIDE", 2.0, 1.9], expected: 1 }
    ];
    tests.forEach(({ args, expected }) => {
        it(`correctly divided ${args[1]} and ${args[2]}`, function () {
            const res = calculateNumber(...args);
            chai.expect(res).to.equal(expected);
        });
    });
});

describe('Edgecases()', function () {
    describe('subzero', function () {
        it("cant be zero", function () {
            chai.expect(calculateNumber("DIVIDE", 14, 0)).to.equal("Error");
        });
    })
});
