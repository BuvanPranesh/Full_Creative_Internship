from My_Sql import con
from flask import *
import sqlite3
from My_Sql import app
cur = con.cursor()


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/user-details')
def insert():
    cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='students' ")
    if cur.fetchone()[0] == 1:
        return render_template("user_details.html")
    else:
        return "<html><body><h1>Table not exists for insert</h1></body></html>"


@app.route('/field-value')
def search():
    cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='students' ")
    if cur.fetchone()[0] == 1:
        cur.execute("SELECT count(*) from students")
        if cur.fetchone()[0] >= 1:
            return render_template("field_value.html")
        else:
            return "<html><body><h1>Table does not contains any row for search </h1>" \
                   "<h2><a href='/'>Click here to home page</a></h2></body></html>"
    else:
        return "<html><body><h1>Table not exists for search</h1></body></html>"


@app.route('/search-roll-update')
def update():
    cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='students' ")
    if cur.fetchone()[0] == 1:
        cur.execute("SELECT count(*) from students")
        if cur.fetchone()[0] >= 1:
            return render_template('search_roll.html')
        else:
            return "<html><body><h1>Table does not contains any row for update</h1>" \
                   "<h2><a href='/'>Click here to home page</a></h2></body></html>"
    else:
        return "<html><body><h1>Table not exists</h1></body></html>"


@app.route('/delete')
def delete():
    cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='students' ")
    if cur.fetchone()[0] == 1:
        cur.execute("SELECT count(*) from students")
        if cur.fetchone()[0] >= 1:
            return render_template('delete.html')
        else:
            return "<html><body><h1>Table does not contains any row for delete</h1>" \
                   "<h2><a href='/'>Click here to home page</a></h2></body></html>"
    else:
        return "<html><body><h1>Table not exists for delete</h1></body></html>"


@app.route('/user-details', methods=['POST'])
def user_details():
    try:
        name = request.form.get('name').title()
        roll = request.form.get('roll')
        gender = request.form.get('gender').title()
        physics = request.form.get('physics')
        chemistry = request.form.get('chemistry')
        maths = request.form.get('maths')
        cur.execute("INSERT INTO students (name, roll, gender, physics, chemistry, maths )"
                    "VALUES(?, ?, ?, ?,?,?)", (name, roll, gender, physics, chemistry, maths))
        con.commit()
        return "<html><body><h1>User details added successfully</h1>" \
               "<h2><a href='/'>Click to home page</a></h2></body></html>"
    except sqlite3.OperationalError:
        return "<html><body><h1>Error in database name</h1></body></html>"
    except sqlite3.IntegrityError:
        return "<html><body><h1>Roll no already exists</h1><h2><a href='/'>Click to home page</a></h2></body></html"


@app.route('/field-value', methods=['POST'])
def search_field_value():
    try:
        field = request.form.get('mySelect')
        val = request.form.get('val')
        cur.execute(f"select count(*) from students where {field} like '{val}'")
        row = cur.fetchall()
        if row[0][0] >= 1:
            cur.execute(f"select * from students where {field} like '{val}'")
            search_results = cur.fetchall()
            return render_template('display.html', display_results=search_results)
        else:
            return "<html><body><h1>Value not found in the table</h1>" \
                   "<h2><a href='/field-value'>Click here to search page</body></html>"
    except sqlite3.OperationalError:
        return "<html><body><h1>Error in database name</h1></body></html>"


@app.route('/search-roll-update', methods=['POST'])
def change():
    try:
        roll = request.form.get('roll')
        session['roll'] = roll
        cur.execute(f"select count(*) from students where roll like '{roll}'")
        row = cur.fetchall()
        if row[0][0] >= 1:
            cur.execute(f"select * from students where roll like '{roll}'")
            search_results = cur.fetchall()
            return render_template('display_update.html', display_results=search_results)
        else:
            return "<html><body><h1>Roll no not found in the table</h1>" \
               "<h2><a href='/'>Click here to home page</h2>"
    except sqlite3.OperationalError:
        return "<html><body><h1>Error in database name</h1></body></html>"


@app.route('/update-result', methods=['POST'])
def res():
    try:
        roll1 = session.get('roll')
        field = request.form.get('mySelect')
        val = request.form.get('val').title()
        cur.execute(f"update students set {field} = '{val}' where roll = '{roll1}' ")
        con.commit()
        cur.execute(f"select * from students where roll = '{roll1}'")
        results = cur.fetchall()
        return render_template('display.html', display_results=results)
    except sqlite3.OperationalError:
        return "<html><body><h1>Error in database name</h1></body></html>"


@app.route('/delete', methods=['POST'])
def clear():
    try:
        val = request.form.get('roll')
        cur.execute(f"select count(*) from students where roll like '{val}'")
        row = cur.fetchall()
        if row[0][0] >= 1:
            cur.execute(f"delete from students where roll like '{val}'")
            con.commit()
            return "<html><body><h1>deleted from the table</h1>" \
                   "<h2><a href='/'>Click to home page</a></h2>" \
                   "<h3><a href='/display'>Click to display page</a></h3></body></html>"
        else:
            return "<html><body><h1>Roll no not found in the table</h1>" \
                   "<h2><a href='/'>Click here to home page</h2></body></html>"
    except sqlite3.OperationalError:
        return "<html><body><h1>Error in database name</h1></body></html>"


@app.route('/display')
def display():
    try:
        cur.execute("SELECT count(*) from students")
        if cur.fetchone()[0] >= 1:
            cur.execute("select * from students order by roll asc")
            display_results = cur.fetchall()
            return render_template('display.html', display_results=display_results)
        else:
            return "<html><body><h1>Table does not contains any row to display</h1><h2>" \
                   "<a href='/'>Click here to home page</a></h2></body></html>"
    except sqlite3.OperationalError:
        return "<html><body><h1>Error in database name</h1></body></html>"

