const request = require('request');
const { assert } = require('chai');
const { expect } = require('chai');

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
        it('test the response', function (done) {
            fetchServer(serverUrl).then(({ response, body }) => {
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal('Welcome to the payment system');
                done();
            }).catch((error) => done(error))
        });
        it('test error after failed request', function (done) {
            fetchServer('http://localhost:7866').then(({ e }) => {
                done();
            }).catch((error) => {
                done(error)
                assert.throws(error);
            })
        });
    });
});


