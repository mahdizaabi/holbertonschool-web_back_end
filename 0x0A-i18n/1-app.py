#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask_babel import Babel
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__, template_folder='templates')
babel = Babel(app)

class Config():
    """[summary]

    Returns:
        [type]: [description]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@app.route('/', methods=['GET'], strict_slashes=False)
def welcome_home():
    """[Render a basic jinja template]
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
