#!/usr/bin/python3
"""
A script that starts a Flask web application
The application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exc):
    """
    Close database
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """
    displays state HTML page
    """
    states = storage.all("State")
    return render_template('9-states.html', state=states)


@app.route('/states/<id>', strict_slashes=False)
def cities_states(id):
    """
    displays a HTML page
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
