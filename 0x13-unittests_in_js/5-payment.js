
const utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const result = utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${result}`);
}
module.exports = sendPaymentRequestToApi;


