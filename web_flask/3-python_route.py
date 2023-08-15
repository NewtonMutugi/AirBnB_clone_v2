#!/usr/bin/python3
""" Script that starts a flask web application """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Hello Flask """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ HBNB """
    return "HBNB"


@app.route('/c/<text>')
def display_text(text):
    """ C """
    return "C " + text.replace('_', ' ')

@app.route('/python/')
@app.route('/python/<text>')
def display_python(text="is_cool"):
    """ Python"""
    if (text != ""):
        return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
