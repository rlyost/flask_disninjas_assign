from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninja')
def ninja():
  return render_template("ninja.html")

@app.route('/ninja/red')
def red():
  return render_template("/ninja/red.html")

@app.route('/ninja/blue')
def blue():
  return render_template("/ninja/blue.html")

@app.route('/ninja/orange')
def orange():
  return render_template("/ninja/orange.html")

@app.route('/ninja/purple')
def purple():
  return render_template("/ninja/purple.html")

@app.route('/ninja/<color>')
def catchall(color):
  return render_template("/ninja/notapril.html")

app.run(debug=True) # run our server