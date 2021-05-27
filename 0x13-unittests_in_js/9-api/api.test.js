const request = require('request');
const { assert } = require('chai');
const { expect } = require('chai');

const serverUrl = 'http://localhost:7865'

function fetchServer(serverUrl) {
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
        describe('GET /', () => {
            it('Code: 200 | Body: Welcome to the payment system', (done) => {
                const options = {
                    url: 'http://localhost:7865',
                    method: 'GET',
                };
                request(options, function (error, response, body) {
                    expect(response.statusCode).to.equal(200);
                    expect(body).to.equal('Welcome to the payment system');
                    done();
                });
            });
        });
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

        it('teststatus code and body response when id is Valid', function (done) {
            fetchServer(`${serverUrl}/cart/12`).then(({ response, body }) => {
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal('Payment methods for cart 12');
                done();
            }).catch((error) => {
                done(error)
                assert.throws(error);
            })
        });
        it('test status code and body response when id is not Valid', function (done) {
            fetchServer(`${serverUrl}/cart/str`).then(({ response, body }) => {
                expect(response.statusCode).to.be.above(400)
                done();
            }).catch((error) => {
                done(error)
                assert.throws(error);
            })
        });
    });
});


