#!/usr/bin/python3
#  Flask web application

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    simple flask to display hello HBNB
    """
    return "Hello HBNB!"
app.run(host="0.0.0.0", port=5000)
