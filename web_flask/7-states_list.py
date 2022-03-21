#!/usr/bin/python3
"""
starts a Flask web application
"""

from models import storage
from models.state import State
from flask import render_template
from flask import Flask


if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def index():
        """
        Display Hello HBNB!
        """
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """
        Display HBNB
        """
        return "HBNB"

    @app.route("/c/<text>", strict_slashes=False)
    def c(text):
        """Display “C ” followed by the value of
        the text variable (replace underscore _
        symbols with a space)
        """
        return "C " + text.replace("_", " ")

    @app.route('/python')
    @app.route('/python/')
    @app.route('/python/<text>', strict_slashes=False)
    def python(text="is cool"):
        """
        display "Python" followed by value of "text"
        with _ equaling a space
        """
        return "Python " + text.replace("_", " ")

    @app.route('/number/<int:n>', strict_slashes=False)
    def number(n):
        """
        displays n if its a number
        """
        return str(n) + " is a number"

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def number_template(n):
        """
        display a HTML page ONLY if n ist an int
        """
        return render_template("5-number.html", n=n)

    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def number_odd_or_even(n):
        """
        H1 tag: “Number: n is even|odd” inside the tag BODY
        """
        num = 'even' if n % 2 == 0 else 'odd'
        return render_template("6-number_odd_or_even.html", n=n, num=num)

    @app.route('/states_list', strict_slashes=False)
    def states_list():
        """
        display a HTML page: (inside the tag BODY)
        """
        st = storage.all(State).values()
        return render_template("7-states_list.html", st=st)

    @app.teardown_appcontext
    def teardown_db(error):
        """
        remove the current SQLAlchemy Session
        """
        storage.close()

    app.run('0.0.0.0')
