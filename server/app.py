from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Test Responses</h1>'


@app.route('/home')
def home():
    return '<h1>Be kind to all people</h1>'


@app.route('/json')
def json():
    return jsonify({'key': 'value', 'key2': [1, 2, 3]})


@app.route('/data')
def data():
    return redirect(url_for('json'), 308)


if __name__ == '__main__':
    app.run()
