#!/usr/bin/env python3
""" Module for trying out Babel i18n """
from flask_babel import Babel
from flask import Flask, render_template

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
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
