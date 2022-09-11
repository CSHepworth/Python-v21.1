from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "And WE'RE BACK!!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def sendResults():
    print(request.form)
    input_name = request.form['input_name']
    location = request.form['location']
    favLang = request.form['favLang']
    comments = request.form['comments']
    session['input_name'] = input_name
    session['location'] = location
    session['favLang'] = favLang
    session['comments'] = comments
    return redirect('/results')

@app.route('/results')
def showResults():
    return render_template('results.html', input_name_on_template = session['input_name'], location = session['location'], favlang = session['favLang'], comments = session['comments'])

if __name__ == "__main__":
    app.run(debug=True)