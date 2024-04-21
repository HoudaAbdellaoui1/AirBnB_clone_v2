#!/usr/bin/python3
""" Flask app """
from flask import Flask, render_template

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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def displayDefaultText(text="is_cool"):
    if '_' in text:
        return f'Python {text.replace("_", " ")}'
    else:
        return f'Python {text}'


@app.route("/number/<int:n>", strict_slashes=False)
def displayInt(n):
    if(isinstance(n, int)):
        return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def displayHTML(n):
    if(isinstance(n, int)):
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
