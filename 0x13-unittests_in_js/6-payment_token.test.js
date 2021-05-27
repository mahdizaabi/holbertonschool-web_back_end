const getPaymentTokenFromAPI = require('./6-payment_token');
const { assert } = require('chai');

describe('getPaymentTokenFromAPI', function () {
    describe('Async tests with done', function () {
        const expected = { data: 'Successful response from the API' };

        it('should wait for the response', function (done) {
            getPaymentTokenFromAPI(true).then((data) => {
                assert.deepEqual(data, expected);
                done();
            }).catch((error) => done(error))
        });
    });
});