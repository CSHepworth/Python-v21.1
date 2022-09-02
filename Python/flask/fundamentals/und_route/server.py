from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<name>')
def hi(name):
    print(name)
    return "Hi, " + name + "!"

@app.route('/repeat/<int:num>/<string:wrd>')
def rep(num, wrd):
    output = ''

    for i in range(0, num):
        output += f"<p>{wrd}</p>"

    return output

if __name__ == "__main__":
    app.run(debug = True)