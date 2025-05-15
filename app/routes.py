from flask import Flask, redirect, url_for, render_template, request
from app import app
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Future form processing can be added here
        return render_template('index.html', current_year=datetime.now().year)
    return render_template('index.html', current_year=datetime.now().year)

@app.route('/how-it-works')
def how_it_works():
    return render_template('how_it_works.html', current_year=datetime.now().year)

@app.route('/about')
def about():
    return render_template('about.html', current_year=datetime.now().year)
