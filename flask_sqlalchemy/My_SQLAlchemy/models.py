from My_SQLAlchemy import db


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



