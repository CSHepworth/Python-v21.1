from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.account import Account
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login&registration.html')

@app.route('/create_account', methods=["POST"])
def create_account():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    account = Account.save(data)
    session['account'] = account
    return redirect('/')

@app.route('/account/<int:id>')
def account(id):
    data = {
        "id": id
    }
    return render_template('account.html', account = Account.get_one(data))


@app.route('/login', methods=["POST"])
def login():
    data = {
        "email": request.form['email']
    }
    account_in_db = Account.get_by_email(data)
    if not account:
        flash("Invalid Email/Password")
        return redirect('/')
    session['account_id'] = account_in_db.id
    return redirect(f'/account/{account_in_db.id}')