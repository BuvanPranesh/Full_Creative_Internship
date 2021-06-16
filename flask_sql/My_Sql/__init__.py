from flask import *
import sqlite3
from traceback import format_exc
import logging
app = Flask(__name__)
app.config['SECRET_KEY'] = "student details"
con = sqlite3.connect('details.db', check_same_thread=False)
con.row_factory = sqlite3.Row
try:
    con.execute('create table students(name varchar(255), roll int not null PRIMARY KEY,'
                'gender Text,physics Integer, chemistry Integer,maths Integer);')
    cur = con.cursor()
    con.commit()
except Exception:
    logging.info(format_exc())


from My_Sql import views


