from flask_app import app
from flask import render_template, redirect, request, session, flash
import re
from flask_app.models.user import User
from flask_app.models.movie import Movie
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register_user', methods = ["POST"])
def register_user():
    is_valid = User.validate_user(request.form)
    if not is_valid:
        flash('v')
        return redirect('/')
    data = {
        "first_name": request.form['fname'],
        "last_name": request.form['lname'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    address = {
        "email": request.form['email']
    }
    email = User.get_by_email(data)
    if email:
        flash('Error: Email is already in use')
        return redirect('/')
    id = User.save(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("error")
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    user = User.get_by_id(data)
    movies = Movie.get_all()
    print(movies)
    return render_template('dashboard.html', user = user, movies = movies)

@app.route('/login', methods = ["POST"])
def login():
    data = {
        "email": request.form['email']
    }
    user = User.get_by_email(data)
    if not user:
        flash("Error: Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    return redirect('/')