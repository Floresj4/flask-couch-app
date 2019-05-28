from flask import Flask, render_template, make_response, request
app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello!"

@app.route('/hello/<username>', methods = ['GET'])
def hello_user(username: str):
    return render_template('hello.html', name = username)

@app.route('/cookie/<username>', methods = ['GET'])
def cookie_user(username: str):

    cookie_username = None
    try: cookie_username = request.cookies.get('username')
    except:
        print('No cookie found.')

    resp = make_response(render_template('hello.html', 
        name = username, 
        changed = (cookie_username is not None and cookie_username == username),
        returning = (cookie_username is not None)))

    resp.set_cookie('username', username)
    
    return resp

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404