from flask import Flask,redirect,url_for,render_template,request
from flask_moment import Moment

app=Flask(__name__)

moment=Moment(app)

from .routes import *