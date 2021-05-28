const request = require('request');
const { assert } = require('chai');
const { expect } = require('chai');

const serverUrl = 'http://localhost:7865'

function fetchServer(serverUrl) {
    return new Promise((resolve, reject) => {
        request(serverUrl, (e, res, body) => {
            if (!e && res.statusCode == 200) {
                resolve({ res, body })
            }
            else {
                reject(res)
            }
        })
    })
}

describe('Basic Integration testing', function () {
    describe('test server response => GET request', function () {
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
            it('test the response', function (done) {
                fetchServer(serverUrl).then(({ res, body }) => {
                    expect(res.statusCode).to.equal(200);
                    expect(body).to.equal('Welcome to the payment system');
                    done();
                }).catch((error) => done(error))
            });
        });
        describe('GET /cart/:id', () => {
            it('GET /cart/:id with valid id', function () {
                return fetchServer('http://localhost:7865/cart/14')
                    .then(({ res }) => {
                        expect(res.statusCode).to.equal(200);
                        expect(res.body).to.equal('Payment methods for cart 14');
                    });
            });


        })
        describe('GET /cart/m', () => {
            it('GET /cart/:id with invalid id', function () {
                return fetchServer('http://localhost:7865/cart/m')
                    .catch(e => {
                        expect(e.statusCode).to.equal(404);
                    });
            });
        })
        describe('GET /cart/', () => {
            it('GET /cart/:id with invalid path', function () {
                return fetchServer('http://localhost:7865/cart/')
                    .catch(e => {
                        expect(e.statusCode).to.equal(404);
                    });
            });
        })

        describe('GET /cart/hello', () => {
            it('GET /cart/:id with invalid path', function () {
                return fetchServer('http://localhost:7865/cart/hello')
                    .catch(e => {
                        expect(e.statusCode).to.equal(404);
                    });
            });
        })
        describe('GET /cart/12b', () => {
            it('Responds with 404', (done) => {
                const options = {
                    url: 'http://localhost:7865/cart/12b',
                    method: 'GET',
                };

                request(options, function (error, response, body) {
                    expect(response.statusCode).to.equal(404);
                    done();
                });
            });
        });
        describe('GET /available_payments', () => {
            it('Responds with 200 with deep equl object', (done) => {
                const options = {
                    url: 'http://localhost:7865/available_payments',
                    method: 'GET',
                };

                request(options, function (error, response, body) {
                    expect(response.statusCode).to.equal(200);
                    expect(JSON.parse(response.body)).to.deep.equal({
                        payment_methods: {
                            credit_cards: true,
                            paypal: false
                        }
                    });
                    done();
                });
            });
        });
        describe('POST /login/Mahdi', () => {
            it('Responds with 404', (done) => {
                const options = {
                    url: 'http://localhost:7865/login/',
                    method: 'POST',
                    json: {
                        userName: 'Betty'
                    }
                };
                request(options, function (error, response, body) {
                    expect(response.statusCode).to.equal(200);
                    expect(response.body).to.equal("Welcome Betty");
                    done();
                });
            });
        });
    });
});


