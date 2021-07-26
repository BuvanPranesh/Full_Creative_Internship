from flask import *
from google.cloud import ndb, datastore
import os
import datetime
from google.cloud.datastore import *

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
    time = ndb.StringProperty()


client = ndb.Client()
client.context()
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
        res = Place.query().filter(Place.city == request.args.get('field')).fetch()
        j = 1
        for i in res:
            res_li.append({"no": j, "city": i.city, "vaccine_centre": i.vaccine_centre,
                           "slots_available": i.slots_available, "key_id": i.key.id()})
            j = j + 1
        return jsonify({"vaccine": res_li})


@app.route('/register', methods=['POST'])
def register():
    x = datetime.datetime.now()
    if request.form.get('name'):
        with client.context():
            res1 = Place.query()
            for i in res1:
                if i.key.id() == int(id1):
                    if int(i.slots_available) >= 1:
                        i.slots_available = str(int(i.slots_available)-1)
                        i.put()
                        res = People(name=request.form.get('name'), age=request.form.get('age'),
                                     aadhaar_no=request.form.get('aadhaar_no'), phone_no=request.form.get('phone_no'),
                                     address=request.form.get('address'), city=i.city, vaccine_centre=i.vaccine_centre,
                                     time=str(x))
                        res.put()
                    else:
                        return "<html><body><h1>Vaccine Not available at this centre</h1>" \
                               "<h2><a href='/'>Click to home page</a></h2></body></html>"
        return redirect(url_for('login'))


@app.route('/displayRegistration')
def display():
    res_li = []
    with client.context():
        res = People.query()
        for j in res:
            res_li.append({"city": j.city, "vaccine_centre": j.vaccine_centre,
                           "name": j.name, "age": j.age, "aadhaar_no": j.aadhaar_no, "phone_no": j.phone_no,
                           "address": j.address, "time": j.time})
        return jsonify({"register_vaccine": res_li})


if __name__ == "__main__":
    app.run(debug=True)
