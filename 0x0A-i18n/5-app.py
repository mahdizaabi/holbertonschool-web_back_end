#!/usr/bin/env python3
""" Module for trying out Babel i18n """
from flask_babel import Babel, _
from flask import Flask, render_template, request, g
from typing import Union

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ Configuration Class for Babel """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    """ Returns a user dictionary or
    None mulate a similar behavior,
    copy the following user table
    """

    try:
        login_as = request.args.get("login_as")
        user_dic = users[int(login_as)]
    except Exception:
        user_dic = None

    return user_dic


@app.before_request
def before_request():
    """ use get_user to find a user if any,
    and set it as a global on flask.g.user"""
    user = get_user()
    g.user = user


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """Renders a Basic Template for Babel"""
    return render_template("5-index.html")


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
