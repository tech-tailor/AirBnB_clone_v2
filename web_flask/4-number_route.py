#!/usr/bin/python3
"""Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    simple flask to display hello HBNB
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    simple flask to display hello HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """
    simple flask to display hello HBNB
    """
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    """
    simple flask to display hello HBNB
    """
    formatted_text = text.replace('_', ' ')
    return f"Pyhon {formatted_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    simple flask to display an int
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
