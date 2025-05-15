import os, time, platform, sys

py_vers = (".").join(platform.python_version().split(".")[:2])
dir_path = os.path.dirname(os.path.realpath(__file__)).strip("app")
python_path = os.path.join(dir_path, f"venv/lib/python{py_vers}/site-packages")

print(py_vers, dir_path, python_path)

#sys.path.insert(0, 'venv/lib/python3.8/site-packages')
#sys.path.insert(0, f'{dir_path}')
sys.path.insert(0, f'{python_path}')

from flask import Flask,redirect,url_for,render_template,request
from flask_moment import Moment


app=Flask(__name__)

moment=Moment(app)

from .routes import *