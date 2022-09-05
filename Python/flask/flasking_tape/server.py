from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "And WE'RE BACK!!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['Post'])
def displayInput():
    print(request.form)
    input1 = request.form['input1']
    session['input1'] = input1
    return redirect('/display')

@app.route('/display')
def display():
    return render_template("display.html", input1 = session['input1'])

if __name__ == "__main__":
    app.run(debug=True)