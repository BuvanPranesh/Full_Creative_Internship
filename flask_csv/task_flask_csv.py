from flask import *
import csv
import os
app = Flask(__name__)


fieldnames = ['name', 'roll', 'gender', 'physics', 'chemistry', 'maths']


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/user-details')
def insert():
    return render_template("user_details.html")


@app.route('/field-value')
def search():
    return render_template("field_value.html")


@app.route('/user-details', methods=['POST'])
def user_details():
    try:
        if os.stat('students_details.csv').st_size > 0:
            pass
        else:
            with open('students_details.csv', 'a+', newline='\n') as insert:
                writer = csv.writer(insert)
                writer.writerow(fieldnames)
    except OSError:
        with open('students_details.csv', 'a+', newline='\n') as insert:
            writer = csv.writer(insert)
            writer.writerow(fieldnames)
    with open('students_details.csv', 'a+', newline='\n') as insert:
        write = csv.writer(insert)
        name = request.form.get('name')
        roll = request.form.get('roll')
        gender = request.form.get('gender')
        physics = request.form.get('physics')
        chemistry = request.form.get('chemistry')
        maths = request.form.get('maths')
        write.writerow([name, roll, gender, physics, chemistry, maths])
        return redirect(url_for('login'))


@app.route('/field-value', methods=['POST'])
def search_field_value():
    try:
        field = request.form.get('mySelect')
        val = request.form.get('val')
        search_results = []
        f = 0
        with open('students_details.csv', 'r+', newline='\n') as search_result:
            reader = csv.reader(search_result)
            next(reader)
            for i in reader:
                if i[fieldnames.index(field)] == val.lower():
                    f = 1
                    search_results.append(i)
            if f == 1:
                return render_template('search_field&value.html', search_results=search_results)
            else:
                return "<html><body><h1>Value Not Found</h1></body></html>"
    except FileNotFoundError:
        return "<html><body><h1>File Not Found</h1></body></html>"
    except Exception:
        return "<html><body><h1>Key Mismatch</h1></body></html>"


@app.route('/display')
def display():
    try:
        with open('students_details.csv', 'r+', newline='\n') as display_result:
            reader = csv.reader(display_result)
            next(reader)
            return render_template('display.html', display_results=reader)
    except FileNotFoundError:
        return "<html><body><h1>File Not Found</h1></body></html>"


if __name__ == "__main__":
    app.run(debug=True)