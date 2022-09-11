from flask import Flask, render_template, request, redirect, session
from survey import Survey

app = Flask(__name__)
app.secret_key = "And WE'RE BACK!!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def sendResults():
    if Survey.validate_survey(request.form):
        Survey.save(request.form)
        return redirect('/results')
    return redirect('/')

@app.route('/results')
def showResults():
    return render_template('results.html', survey = Survey.get_recent())

if __name__ == "__main__":
    app.run(debug=True)
