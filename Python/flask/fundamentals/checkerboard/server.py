from turtle import color
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('checkerboard.html', row=8, col=8, color1='red', color2='black')

@app.route('/<int:x>')
def cust_checkerboard0(x):
    return render_template('checkerboard.html', row=x, col=8, color1='red', color2='black')

@app.route('/<int:x>/<int:y>')
def cust_checkerboard1(x, y):
    return render_template('checkerboard.html', row=x, col=y, color1='red', color2='black')

@app.route('/<int:x>/<int:y>/<string:col1>')
def cust_checkerboard2(x, y, col1):
    return render_template('checkerboard.html', row=x, col=y, color1=col1, color2='black')    

@app.route('/<int:x>/<int:y>/<string:col1>/<string:col2>')
def cust_checkerboard3(x, y, col1, col2):
    return render_template('checkerboard.html', row=x, col=y, color1=col1, color2=col2)    

if __name__ == "__main__":
    app.run(debug = True)