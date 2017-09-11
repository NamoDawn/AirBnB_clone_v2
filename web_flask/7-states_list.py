#!/usr/bin/python3
''' script that starts a Flask web application'''
from flask import Flask
from models import storage
from flask import render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    '''remove the current SQLAlchemy Session'''
    storage.close()


@app.route('/states_list')
def states_list():
    '''display a HTML page'''
    state_dict = storage.all(cls='State')
    return render_template('7-states_list.html', state_list=state_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
