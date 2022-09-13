from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.email import Email

@app.route('/')
def index():
    return redirect('/new_address')

@app.route('/new_address')
def new_address():
    return render_template('new_address.html')

@app.route('/save_new', methods=["POST"])
def save_new():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/emails')

@app.route('/emails')
def emails():
    return render_template('emails.html', emails = Email.get_all())

@app.route('/email/destory/<int:id>')
def destroy(id):
    data = {
        'id': id
    }
    Email.destroy(data)
    return redirect('/emails')    