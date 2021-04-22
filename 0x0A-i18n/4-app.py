#!/usr/bin/env python3
""" Module for trying out Babel i18n """
from flask_babel import Babel, _
from flask import Flask, render_template, request, flash

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ Configuration Class for Babel """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """Renders a Basic Template for Babel Implementation"""
    return render_template("3-index.html")


@babel.localeselector
def get_locale() -> str:
    """[ Force locale with URL parameter]
    """
    locale = request.args.get('locale')
    if locale:
        return locale
    if request.args.get('login_as'):
        language = users.get(int(user).get('locale'))
        if language in app.config['LANGUAGES']:
            return language
    headers = request.headers.get('locale')
    if headers:
        return headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
