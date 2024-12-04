from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder='./templates',static_folder='./static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/lessonplan')
def teachers():
    return render_template('lessonplan.html')

@app.route('/assembly')
def students():
    return render_template('assembly.html')

@app.route('/pedagogies')
def pedagogies():
    return render_template('pedagogies.html')