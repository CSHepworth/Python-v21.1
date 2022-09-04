from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = 'merncy'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/land')
def create_land():
    return render_template('land.html')

@app.route('/', methods=['POST'])
def takeoff():
    fname = request.form['fname']
    session['fname'] = fname
    print(session['fname'])
    return redirect('/land')

@app.route('/land')
def landing():
    return render_template('land.html', fname_template = session['fname'])

@app.route('/land')
def land():
    return render_template('land.html')

if __name__ == "__main__":
    app.run(debug=True)