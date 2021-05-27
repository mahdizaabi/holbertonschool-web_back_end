const request = require('request');
const { assert } = require('chai');

const serverUrl = 'http://localhost:7865'

function fetchServer(serverUrl) {
    const res = {};
    return new Promise((resolve, reject) => {
        request(serverUrl, (e, res, body) => {
            if (e) {
                resolve({ res, body, e })
            }
            else {
                reject(e)
            }
        })
    })
}

describe('Basic Integration testing', function () {
    describe('test server response after GET request', function () {

        it('test the response status', function (done) {
            fetchServer(serverUrl).then(({ response, body }) => {
                assert.strictEqual(response.statusCode, '200');
                done();
            }).catch((error) => done(error))
        });
        it('test the response body', function (done) {
            fetchServer(serverUrl).then(({ response, body }) => {
                assert.strictEqual(body, 'Welcome to the payment system');
                done();
            }).catch((error) => done(error))
        });
        it('test error after failed request', function (done) {
            fetchServer('http://localhost:7866').then(({ e }) => {
                done();
            }).catch((error) => { done(error)
                assert.throws(error);
            })
        });
    });
});


