#!/usr/bin/python3
""" Script that starts a flask web application """

from flask import Flask, render_template


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


@app.route('/number/<int:n>')
def display_number(n):
    """ Number """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def display_template_number(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """ Odd or Even """
    if (n % 2 == 0):
        return render_template('6-number_odd_or_even.html', number=n,
                               num_type="even")
    else:
        return render_template('6-number_odd_or_even.html', number=n,
                               num_type="odd")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
