"""test Flask with this"""

from flask import Flask
test = Flask(__name__)

@test.route('/')
def home():
    return '<h1>Hello World!</h1>'

@test.route('/about')
def about():
    return '<h1>This is the about page</h1>'

if __name__ == '__main__':
    test.run(debug=True)
