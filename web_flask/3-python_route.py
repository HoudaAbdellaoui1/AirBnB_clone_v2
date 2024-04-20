#!/usr/bin/python3
""" Flask app """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def displayText(text):
    if '_' in text:
        return f'C {text.replace("_", " ")}'
    else:
        return f'C {text}'


@app.route("/python/<text>", strict_slashes=False)
def displayDefaultText(text="is_cool"):
    if '_' in text:
        return f'Python {text.replace("_", " ")}'
    else:
        return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
