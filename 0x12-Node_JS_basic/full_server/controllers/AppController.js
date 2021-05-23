class AppController {
  static getHomepage(request, response) {
    response.send(200, 'Hello Holberton School!');
  }
}

module.exports = AppController;
