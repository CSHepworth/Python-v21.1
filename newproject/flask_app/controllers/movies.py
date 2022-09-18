from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.movie import Movie
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/addmovie')
def new_movie():
    if 'user_id' not in session:
        flash('error')
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    user = User.get_by_id(data)
    return render_template('addmovie.html', user = user)

@app.route('/create_movie', methods = ["POST"])
def create_movie():
    is_valid = Movie.validate_movie(request.form)
    if not is_valid:
        return redirect('/addmovie')
    data = {
        "title": request.form['title'],
        "description": request.form['description'],
        "rating": request.form['rating'],
        "release_date": request.form['release_date'],
        "author_id": session['user_id']
    }
    movie = Movie.save(data)
    return redirect('/dashboard')