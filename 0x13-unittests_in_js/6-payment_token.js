const getPaymentTokenFromAPI = (success) => success ? Promise.resolve({data: 'Successful response from the API'}) : false
module.exports = {getPaymentTokenFromAPI};