from flask import *
from google.cloud import ndb, datastore
import os
from google.cloud.datastore import *

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vaccine-booking.json'
app = Flask(__name__)


class Place(ndb.Model):
    city = ndb.StringProperty()
    vaccine_centre = ndb.StringProperty()
    slots_available = ndb.StringProperty()


class People(ndb.Model):
    name = ndb.StringProperty()
    age = ndb.StringProperty()
    aadhaar_no = ndb.StringProperty()
    phone_no = ndb.StringProperty()
    address = ndb.StringProperty()


@app.route('/')
def login():
    return render_template('project.html')


@app.route('/centre', methods=['POST'])
def center():
    client = ndb.Client()
    with client.context():
        res = Place(city=request.form.get('city'), vaccine_centre=request.form.get('center'),
                    slots_available=request.form.get('slots'))
        res.put()


@app.route('/search')
def search():
    res_li = []
    li2 = []
    client = ndb.Client()
    with client.context():
        res = Place.query().filter(Place.city == request.args.get('field')).fetch()
        j = 1
        for i in res:
            res_li.append({"no": j, "city": i.city, "vaccine_centre": i.vaccine_centre,
                           "slots_available": i.slots_available, "key_id": i.key.id()})
            j = j + 1
        return jsonify({"vaccine": res_li})


@app.route('/register', methods=['POST'])
def register():
    print(request.form.get("name"))


def register1(aa1):
    res1 = Place.query()
    for i in res1:
        if i.key.id() == aa1:
            i.slots_available = str(int(i.slots_available) - 1)
            i.put()
    return "<html><h1>You have Registered Successfully For vaccination<h1><h2><a href='/'>Home Page</a></h2></html>"


@app.route('/displayRegistration')
def display():
    res_li = []
    c = 1
    client = ndb.Client()
    with client.context():
        res = People.query()
        for j in res:
            res_li.append({"total_registration": c, "name": j.name, "age": j.age, "aadhaar_no": j.aadhaar_no,
                           "phone_no": j.phone_no, "address": j.address})
            c = c + 1
        return jsonify({"register_vaccine": res_li})


if __name__ == "__main__":
    app.run(debug=True)
