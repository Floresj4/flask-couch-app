from flask import Flask, render_template, make_response, request
from flask import flash, redirect, url_for

from jinja2 import Environment

import requests, json, urllib
import logging

logging.basicConfig(
    level = logging.INFO,
    handlers = [logging.StreamHandler()])
logger = logging.getLogger(__name__)

app = Flask(__name__)
#a session key is required for flash messaging
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    rn = request.cookies.get('remember-me')
    return render_template('index.html', remembered_name = rn)

@app.route('/hello')
def hello():
    return "Hello!"

@app.route('/baseball')
def baseball():
    error_message = None
    player_data = None
    filter = None

    # get a query param to use for filtering
    filter = request.args.get('filter')
    if filter != None and filter != '':
        encoded = urllib.parse.quote(str.encode(filter))
        filter = '?key=\"{}\"'.format(encoded)
    else: filter = ''

    # encode the filter text coming in and get database data
    response = requests.get('http://couch:5984/baseball/_design/byteam/_view/team{}'.format(filter))
    if response.status_code != 200:
        error_message = 'Unable to load team data.'
    else: player_data = json.loads(response.text)

    return render_template('baseball.html', data = player_data, error = error_message, filtering = filter != '')

@app.route('/hello/<username>', methods = ['GET'])
def hello_user(username: str):
    return render_template('hello.html', name = username)

@app.route('/cookie/<username>', methods = ['GET'])
def cookie_user(username: str):

    cookie_username = None
    try: cookie_username = request.cookies.get('username')
    except: print('No cookie found.')

    resp = make_response(render_template('hello.html', 
        name = username, 
        returning = (cookie_username is not None)))

    resp.set_cookie('username', username)
    return resp

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/rememberme', methods = ['POST'])
def remember_me():
    rm = request.form['remember-me']
    resp = make_response(redirect('/'))
    resp.set_cookie('remember-me', rm)
    return resp

@app.route('/showflash')
def showflash():
    return render_template('flash.html')

@app.route('/flash')
def flash_response():
    flash('You were successfully redirected.')
    return redirect(url_for('showflash'))
