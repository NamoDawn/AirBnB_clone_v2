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
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
