#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/')  # pylint: disable=W0612
def states_list():
    """ displays an HTML page with a list of all State objects """
    states = storage.all(State)
    cities = storage.all(City)
    return render_template('7-states_list.html', states=states, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """ closes the storage on teardown """
    storage.close()


if __name__ == '__main__':
    app.run(host='localhost', port='5000')
