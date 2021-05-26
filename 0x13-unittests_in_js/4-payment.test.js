const sinon = require("sinon");
const utils = require('./utils');
const assert = require('assert');

const sendPaymentRequestToApi = require('./3-payment');
describe("sendPaymentRequestToApi", function () {
    let stubCalculate;
    let stubConsole;
    beforeEach(function () {
        stubCalculate = sinon.stub(utils, 'calculateNumber');
        stubCalculate.returns(10);
        stubConsole = sinon.stub(console, 'log');
    });
    afterEach(function () {
        stubCalculate.resetBehavior();
        stubConsole.resetBehavior();
    });

    it("should inspect passed arguments to utils.calculate and console.log", function () {
        sendPaymentRequestToApi(100, 20);
        assert(stubCalculate.calledOnceWithExactly('SUM', 100, 20));
        assert(stubConsole.calledOnceWithExactly('The total is: 10'));
    });


});
