#!/usr/bin/python3
"""
Script that starts a flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Displays Hello HBNB!
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run('0.0.0.0')
