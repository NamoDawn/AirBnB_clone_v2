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
    states_dict = storage.all(cls='State')
    state_list = []
    for k, v in states_dict.items():
        state_id = k.split('.')
        state_id = state_id[0]
        name = v.name
        tup = (state_id, name)
        state_list.append(tup)
    state_list.sort(key=lambda x: x[1])
    return render_template('7-states_list.html', state_list=state_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
