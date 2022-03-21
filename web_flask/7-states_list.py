#!/usr/bin/python3
"""
Starts a web Flask app
"""


from flask import Flask, render_template
from models import storage
from models.state import State

if __name__ == '__main__':
    app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """displays 'Hello HBNB!'"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(cont):
    """remove the current sql alchemy session"""
    storage.close()


app.run('0.0.0.0', port="5000")
