from app import app,trippy
from threading import Thread
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    trippy.tripstop = True
    return render_template('index.html')

@app.route('/trip')
def trip():
    trippy.tripstop = False
    t = Thread(target=trippy.trip)
    t.start()
    return render_template('trip.html', title = "Now Tripping")
