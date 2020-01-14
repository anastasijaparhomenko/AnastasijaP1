from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return "Hi!"

@app.route('/home')
def home():
  return "<h1>Feels like home<h1>"

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contacts')
def contacts():
  return render_template('contacts.html')

app.run(host = '0.0.0.0',port = 8020)