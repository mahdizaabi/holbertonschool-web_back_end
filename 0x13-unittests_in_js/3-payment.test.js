const sinon = require("sinon");
const utils = require('./utils');
const assert = require('assert');

const sendPaymentRequestToApi = require('./3-payment');
describe("sendPaymentRequestToApi", function () {
    const Spy = sinon.spy(utils, 'calculateNumber');

    it("should inspect the external lib's usage of its internal methods", function () {
        sendPaymentRequestToApi(10, 14);
        assert(utils.calculateNumber.calledOnce);
    });
});
