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
    
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    user = Account.save(data)
    if not user:
        flash("Email already has account")
        return redirect('/')
    session['user'] = user.id
    return redirect(f'/account/{user.id}')

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
    user = Account.get_by_email(data)
    if not account:
        flash("Invalid Email/Password")
        return redirect('/')
    session['user'] = user.id
    return redirect(f'/account/{user.id}')