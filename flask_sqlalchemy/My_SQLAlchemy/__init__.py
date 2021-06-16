from flask import *
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentsdetails.db'
app.config['SECRET_KEY'] = "StudentDetails"
db = SQLAlchemy(app)


from My_SQLAlchemy import views