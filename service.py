from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello!"

@app.route('/hello/<username>', methods = ['GET'])
def hello_user(username: str):
    return 'Hello, {}!'.format(username)