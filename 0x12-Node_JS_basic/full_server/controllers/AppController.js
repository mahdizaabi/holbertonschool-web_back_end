class AppController {
  static getHomepage(request, response) {
    response.send('Hello Holberton School!');
  }
}

module.exports = AppController;
