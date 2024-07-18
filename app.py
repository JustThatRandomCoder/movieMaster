from flask_socketio import SocketIO, emit
from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True

socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def index2():
    return render_template('index.html') 
    
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')     
    
if __name__ == '__main__':
    from waitress import serve
    #serve(app, host="0.0.0.0", port=8008)
    app.run(host="0.0.0.0", port=8034)    