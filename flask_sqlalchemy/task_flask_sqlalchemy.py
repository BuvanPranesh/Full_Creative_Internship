from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SECRET_KEY'] = "StudentDetails"
db = SQLAlchemy(app)


class Students(db.Model):
    name = db.Column(db.String(100))
    roll = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(50))
    physics = db.Column(db.Integer)
    chemistry = db.Column(db.Integer)
    maths = db.Column(db.Integer)

    def __init__(self, name, roll, gender, physics, chemistry, maths):
        self.name = name
        self.roll = roll
        self.gender = gender
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/user-details')
def insert():
    return render_template('user_details.html')


@app.route('/field-value')
def search():
    result = Students.query.all()
    if not result:
        return "<html><body><h1>Table contains no row to search</h1></body></html>"
    else:
        return render_template('field_value.html')


@app.route('/search-roll-update')
def change():
    result = Students.query.all()
    if not result:
        return "<html><body><h1>Table contains no row to update</h1></body></html>"
    else:
        return render_template('search_roll.html')


@app.route('/delete')
def delete():
    result = Students.query.all()
    if not result:
        return "<html><body><h1>Table contains no row to delete</h1></body></html>"
    else:
        return render_template('delete.html')


@app.route('/user-details', methods=['POST'])
def new():
    try:
        student = Students(request.form.get('name').title(), request.form.get('roll'), request.form.get('gender').title(),
                           request.form.get('physics'), request.form.get('chemistry'), request.form.get('maths'))
        db.session.add(student)
        db.session.commit()
        return "<html><body><h1>Added Successfully </h1><h2><a href='/'>Click to home page</a></h2></body></html>"
    except NameError:
        return "<html><body><h1>Name error in class name</h1></body></html>"
    except exc.IntegrityError:
        return "<html><body><h1>Roll no already exists</h1></body></html>"


@app.route('/field-value', methods=['POST'])
def search1():
    try:
        roll = {}
        field = request.form.get('mySelect')
        val = request.form.get('val')
        roll[field] = val.title()
        result = Students.query.filter_by(**roll).all()
        if not result:
            return "<html><body><h1>Value no not found</h1>" \
                   "<h2><a href='/'>Click to home page</a></h2></body></html></body></html>"
        else:
            return render_template('display.html', students=result)
    except NameError:
        return "<html><body><h1>Name error in class name</h1></body></html>"


@app.route('/search-roll-update', methods=['POST'])
def change1():
    try:
        roll_val = {}
        roll = request.form.get('roll')
        session['roll'] = roll
        roll_val['roll'] = roll
        c = Students.query.filter_by(roll=roll).count()
        if c == 1:
            li = Students.query.filter_by(**roll_val).all()
            return render_template('display_update.html', students=li)
        else:
            return "<html><body><h1>Roll no not found</h1>" \
                   "<h2><a href='/'>Click to home page</a></h2></body></html></body></html>"
    except NameError:
        return "<html><body><h1>Name error in class name</h1></body></html>"


@app.route('/update-result', methods=['POST'])
def res():
    try:
        field_val = {}
        roll_val = {}
        roll = session.get('roll')
        field = request.form.get('mySelect')
        val = request.form.get('val').title()
        roll_val['roll'] = roll
        field_val[field] = val
        Students.query.filter_by(**roll_val).update(field_val)
        db.session.commit()
        result = Students.query.filter_by(**roll_val).all()
        return render_template('display.html', students=result)
    except NameError:
        return "<html><body><h1>Name error in class name</h1></body></html>"


@app.route('/delete', methods=['POST'])
def erase():
    try:
        roll = request.form.get('roll')
        c = Students.query.filter_by(roll=roll).count()
        if c == 1:
            Students.query.filter_by(roll=roll).delete()
            db.session.commit()
            return "<html><body><h1>Deleted from the table</h1>" \
                   "<h2><a href='/'>Click to home page</a></h2></body></html>"
        else:
            return "<html><body><h1>Roll number not found</h1" \
                   "><h2><a href='/'>Click to home page</a></h2></body></html>"
    except NameError:
        return "<html><body><h1>Name error in class name</h1></body></html>"


@app.route('/display')
def display():
    try:
        result = Students.query.all()
        if not result:
            return "<html><body><h1>Table contains no row to display</h1></body></html>"
        else:
            return render_template('display.html', students=result)
    except NameError:
        return "<html><body><h1>Name error in class name</h1></body></html>"


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
