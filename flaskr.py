import sqlite3
from flask import(
    Flask, request, session, g, redirect, url_for, abort,
    render_template, flash)

# configs
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'flaskr-dev-env'
USERNAME = 'admin'
PASSWORD = 'default'


# create the app now
app = Flask(__name__)
app.config.from_object(__name__)


# connect to db util
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
