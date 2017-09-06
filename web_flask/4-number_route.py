#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_route():
    '''method to return sentence upon request'''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb_route():
    '''method to return sentence on request'''
    return "HBNB"


@app.route('/c/<text>')
def c_route(text):
    '''method to return sentence with variable supplied'''
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/<text>')
@app.route('/python/')
def python_route(text='is cool'):
    '''method to return setence with variable or default'''
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def number_route(n):
    '''method to return sentence with number'''
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
