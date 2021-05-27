
var { expect } = require('chai');
const sinon = require("sinon");
const utils = require('./utils');
const assert = require('assert');
const sendPaymentRequestToApi = require('./5-payment');

describe("sendPaymentRequestToApi", function () {
    let spyConsole;
    beforeEach(function () {
        spyConsole = sinon.spy(console, "log");
    });
    afterEach(function () {
        spyConsole.restore()
    });
    it("test console logout with 100 and 20", function () {
        const res = sendPaymentRequestToApi(100, 20);
        assert(spyConsole.calledOnceWithExactly('The total is: 120'));
        expect(console.log.calledOnce).to.be.true;
    });


    it("test console logout with 10 and 10", function () {
        const res = sendPaymentRequestToApi(10, 10);
        const expected = 'The total is: 20';
        assert(spyConsole.calledOnceWithExactly('The total is: 20'));
        expect(console.log.calledOnce).to.be.true;

    });
});