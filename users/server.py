from flask_app.controllers import users


@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('users.html',users=User.get_all())

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create_new', methods=['POST'])
def create_new():

    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }

    User.save(data)

    return redirect('/users')

@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template('show.html', user=User.get_one(data))

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={
        "id":id
    }
    return render_template('edit.html', user=User.get_one(data))

@app.route('/user/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)