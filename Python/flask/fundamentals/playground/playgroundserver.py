from distutils.log import debug
from os import times
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('play.html', times = 0)

@app.route('/play')
def play():
    return render_template('play.html', times = 3)

@app.route('/play/<int:times>')
def play2(times):
    return render_template('play.html', times = times)

@app.route('/play/<int:times>/<string:color>')
def play3(times, color):
    return render_template('play.html', times = times, color = color)
    
if __name__ == "__main__":
    app.run(debug = True)