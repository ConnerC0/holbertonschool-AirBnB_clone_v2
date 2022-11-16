#!/usr/bin/python3
<<<<<<< HEAD
'''Starts a Flask Web app'''
=======
"""
    starts a Flask web application
"""
>>>>>>> a4b00aa2179dd8349c9b329bbab5069268e4c205
from flask import Flask


app = Flask(__name__)

<<<<<<< HEAD

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="5000")
=======
@app.route('/')
def index():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, strict_slashes=False)
>>>>>>> a4b00aa2179dd8349c9b329bbab5069268e4c205
