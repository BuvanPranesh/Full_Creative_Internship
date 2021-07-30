from flask import *
from google.cloud import ndb
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vaccine-booking.json'
app = Flask(__name__)


class Place(ndb.Model):
    city = ndb.StringProperty()
    vaccine_centre = ndb.StringProperty()
    slots_available = ndb.StringProperty()


class People(ndb.Model):
    city = ndb.StringProperty()
    vaccine_centre = ndb.StringProperty()
    name = ndb.StringProperty()
    age = ndb.StringProperty()
    aadhaar_no = ndb.StringProperty()
    phone_no = ndb.StringProperty()
    address = ndb.StringProperty()
    register_time = ndb.DateTimeProperty(auto_now_add=True)


client = ndb.Client()
global id1


@app.route('/')
def login():
    return render_template('project.html')


@app.route('/booking')
def book():
    global id1
    id1 = request.args.get('id')
    return render_template('register.html')


@app.route('/centre', methods=['POST'])
def center():
    res = Place(city=request.form.get('city'), vaccine_centre=request.form.get('center'),
                slots_available=request.form.get('slots'))
    res.put()


@app.route('/search')
def search():
    res_li = []
    with client.context():
        res = Place.query().filter(Place.city == request.args.get('search_field')).fetch()
        for i in res:
            print('i', i)
            res_li.append({"city": i.city, "vaccine_centre": i.vaccine_centre,
                           "slots_available": i.slots_available, "key_id": i.key.id()})
        return jsonify({"vaccine": res_li})


@app.route('/order_by')
def order_by():
    field = request.args.get('order_by_field')
    res_li = []
    with client.context():
        if field == "city":
            res = People.query().order(People.city).fetch()
            for j in res:
                res_li.append({"city": j.city, "vaccine_centre": j.vaccine_centre,
                               "name": j.name, "age": j.age, "aadhaar_no": j.aadhaar_no, "phone_no": j.phone_no,
                               "address": j.address, "time": j.register_time})
            return jsonify({"register_vaccine": res_li})
        elif field == "vaccine_centre":
            res = People.query().order(People.vaccine_centre).fetch()
            for j in res:
                res_li.append({"city": j.city, "vaccine_centre": j.vaccine_centre,
                               "name": j.name, "age": j.age, "aadhaar_no": j.aadhaar_no, "phone_no": j.phone_no,
                               "address": j.address, "time": j.register_time})
            return jsonify({"register_vaccine": res_li})
        elif field == "name":
            res = People.query().order(People.name).fetch()
            for j in res:
                res_li.append({"city": j.city, "vaccine_centre": j.vaccine_centre,
                               "name": j.name, "age": j.age, "aadhaar_no": j.aadhaar_no, "phone_no": j.phone_no,
                               "address": j.address, "time": j.register_time})
            return jsonify({"register_vaccine": res_li})
        elif field == "age":
            res = People.query().order(People.age).fetch()
            for j in res:
                res_li.append({"city": j.city, "vaccine_centre": j.vaccine_centre,
                               "name": j.name, "age": j.age, "aadhaar_no": j.aadhaar_no, "phone_no": j.phone_no,
                               "address": j.address, "time": j.register_time})
            return jsonify({"register_vaccine": res_li})


@app.route('/filter_by')
def filter_by():
    res_li = []
    with client.context():
        res = People.query().order(-People.register_time).fetch()
        for j in res:
            if j.city == request.args.get('filter_by_city'):
                res_li.append({"city": j.city, "vaccine_centre": j.vaccine_centre, "name": j.name, "age": j.age,
                               "aadhaar_no": j.aadhaar_no, "phone_no": j.phone_no,
                               "address": j.address, "time": j.register_time})
        return jsonify({"register_vaccine": res_li})


@app.route('/register', methods=['POST'])
def register():
    if request.form.get('name'):
        with client.context():
            res1 = Place.query()
            for i in res1:
                print(i)
                if i.key.id() == int(id1):
                    if int(i.slots_available) >= 1:
                        i.slots_available = str(int(i.slots_available)-1)
                        i.put()
                        res = People(name=request.form.get('name'), age=request.form.get('age'),
                                     aadhaar_no=request.form.get('aadhaar_no'), phone_no=request.form.get('phone_no'),
                                     address=request.form.get('address'), city=i.city, vaccine_centre=i.vaccine_centre)
                        res.put()
                        return "<html><body><h1>You have been registered successfully for the vaccination</h1>" \
                               "<h2><a href='/'>Click to home page</a></h2></body></html>"
        return redirect(url_for('login'))


@app.route('/displayRegistration')
def display():
    res_li = []
    with client.context():
        res = People.query().order(-People.register_time).fetch()
        for j in res:
            res_li.append({"city": j.city, "vaccine_centre": j.vaccine_centre, "name": j.name, "age": j.age,
                           "aadhaar_no": j.aadhaar_no, "phone_no": j.phone_no, "address": j.address,
                           "time": j.register_time})
        return jsonify({"register_vaccine": res_li})


if __name__ == "__main__":
    app.run(debug=True)
