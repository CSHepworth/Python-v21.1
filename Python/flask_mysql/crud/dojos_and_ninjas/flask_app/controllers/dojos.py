from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos = Dojo.get_all())

@app.route('/new_dojo', methods=['POST'])
def new_dojo():
    data = {
        "name": request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/addninja')
def addninja():
    return render_template('addninja.html', dojos = Dojo.get_all())

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo']
    }
    Ninja.save(data)
    return redirect('/')

@app.route('/dojo/show/<int:id>')
def showDojo(id):
    data = {
        "id": id
    }
    return render_template('showdojo.html', dojo = Dojo.get_dojo_and_ninjas(data))