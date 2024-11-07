from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder='./templates',static_folder='./static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/teachers')
def teachers():
    return render_template('teachers.html')


