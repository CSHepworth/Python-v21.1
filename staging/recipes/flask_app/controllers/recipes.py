from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.account import Account
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/new_recipe/<int:id>')
def new_recipe(id):
    data = {
        "id": id
    }
    return render_template('new_recipe.html', account = Account.get_one(data))

@app.route('/create_recipe', methods=["POST"])
def create_recipe():
    print(request.form)
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "under30": request.form["under30"],
        "author_id": session['user']
    }
    recipe = Recipe.save(data)
    return redirect(f'/account/{session["user"]}')