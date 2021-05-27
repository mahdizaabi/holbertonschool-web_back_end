const request = require('request');
const { expect } = require('chai');

describe('Integration Testing', () => {
  describe('GET /', () => {
    it('Code: 200 | Body: Welcome to the payment system', (done) => {
      const params = {
        url: 'http://localhost:7865',
        method: 'GET',
      };

      request(params, function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });
});