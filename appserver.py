# Don't call this flask.py!
# Documentation for Flask can be found at:
# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)
app.secret_key = b'REPLACE_ME_x#pi*CO0@^z'

sqlite_uri = 'sqlite:///' + os.path.abspath(os.path.curdir) + '/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User

@app.before_first_request
def initialize():
    try:
        User.query.all()
    except:
        print('---- WARNING: no DB tables found.  Creating tables. ----')
        db.create_all()

@app.route('/')
def index():
    return 'Results of GET /'

from random import randint

@app.route('/makeuser/')
def makeuser():
    i = randint(1, 100000)
    randomusername = 'User' + str(i)
    u = User(username=randomusername, email='fakeemail@yahoo.com')
    db.session.add(u)
    db.session.commit()
    return 'Made user ' + u.username

@app.route('/getusers/')
def getusers():
    userlist = User.query.all()
    usernames = ''
    for user in userlist:
        usernames += user.username + ','

    usernames = usernames[:-1]

    return 'Users in this system are: ' + usernames

