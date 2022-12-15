from flask import render_template
from app import app

@app.route('/')   # == @app.route('/index')
def index():
    print(__name__)
    return render_template('index.html')