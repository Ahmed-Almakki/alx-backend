#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ configuration class for the app"""
    LANGUAGES = ["en", "fr"]
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Bable(app)


@app.route("/")
def hello_world():
    """ default route"""
    return render_template("0-index.html")
