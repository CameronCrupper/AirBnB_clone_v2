#!/usr/bin/python3
"""
starts a Flask web application
"""

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
        """
        C then value of text
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

    app.run('0.0.0.0')
