from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello!"

@app.route('/hello/<username>', methods = ['GET'])
def hello_user(username: str):
    return render_template('hello.html', name = username)