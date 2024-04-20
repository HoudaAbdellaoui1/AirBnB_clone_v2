#!/usr/bin/python3
""" Flask app """
from flask import Flask

app = Flask(__name__)


@app.route("/c/<text>", strict_slashes=False)
def displayText(text):
    if '_' in text:
        return f'C {text.replace("_", " ")}'
    else:
        return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
