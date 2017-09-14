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
    state_contents = storage.all(cls='State')
    state_dict = {}
    for pre_key, value in state_contents.items():
        key = pre_key.split(".")[1]
        state_dict[key] = value.name
    return render_template('7-states_list.html', values=state_contents)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
