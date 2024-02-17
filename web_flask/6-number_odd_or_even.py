#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """
    simple flask to display an int
    """

    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_odd_or_even(n):
    """
    simple flask to display an int
    """
    num_type = None
    if n % 2 == 0:
        num_type = 'even'
    else:
        num_type = 'odd'

    return render_template('6-number_odd_or_even.html', n=n, num_type=num_type)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
