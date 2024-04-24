#!/usr/bin/python3
""" Flask app """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """
    Remove current SQLAlchemy Session
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def getStates():
    """
    Display HTML page
    """
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
