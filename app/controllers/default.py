from app import app
from markupsafe import escape
from flask import render_template


@app.route('/')
@app.route('/index')

def index():
    name= "Pedro"
    data= {'Job' : 'Programmer', 'Channel' : 'Code Park'}

    return render_template('index.html', name = name, data = data)

@app.route('/contact')

def contat():

    return render_template('contact.html')