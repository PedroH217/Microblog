from app import app
from markupsafe import escape
from flask import render_template


@app.route('/')
@app.route('/index/', defaults= {'name' : 'users', 'job' : 'No Job', 'channel' : 'No channel'})
@app.route('/index/<name>/<job>/<channel>')

def index(name, job , channel):

    data= {'Job' : job , 'Channel' : channel }

    return render_template('index.html', name = name, data = data)

@app.route('/contact')

def contat():

    return render_template('contact.html')