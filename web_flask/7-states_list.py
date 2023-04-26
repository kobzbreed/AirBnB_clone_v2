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


@app.route('/states_list', strict_slashes=False)
def displays_states():
    """
    displays state HTML page
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
