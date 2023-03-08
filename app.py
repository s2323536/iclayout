from flask import Flask,request,render_template,jsonify,session
import pandas as pd

app = Flask(
    __name__,
    static_folder='static',
    static_url_path='/'
)
app.secret_key="any string but secret"

@app.route('/')
def home():
    return render_template('iclayout.html')
    
