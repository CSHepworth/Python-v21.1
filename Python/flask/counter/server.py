from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "And WE'RE BACK!!"

counter = 1

@app.route('/')
def index():
    global counter
    counter += 1
    session['counter'] = counter
    return render_template('index.html', counter = session['counter'])

"""
@app.route('/')
def newindex():
    return render_template('index.html', counter = session['counter'])
"""
@app.route('/destroy_session')
def destory_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)