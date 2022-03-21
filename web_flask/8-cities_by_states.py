#!/usr/bin/python3
"""
starts a Flask web application
"""

from models import storage
from models.state import State
from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    HTML page of the States and the
    Cities by State
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(error):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
