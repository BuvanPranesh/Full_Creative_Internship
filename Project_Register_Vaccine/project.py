from flask import *
from google.cloud import ndb
import os
from google.cloud.datastore import *
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'database1.json'
app = Flask(__name__)


class Place(ndb.Model):
    city = ndb.StringProperty()
    vaccine_center = ndb.StringProperty()
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
        res = Place(city=request.form.get('city'), vaccine_center=request.form.get('center'),
                    slots_available=request.form.get('slots'))
        res.put()


@app.route('/search')
def search():
    res_li = []
    client = ndb.Client()
    with client.context():
        res = Place.query().filter(Place.city == request.args.get('field')).fetch()
        for i in res:
            res_li.append({"city": i.city, "vaccine_center": i.vaccine_center, "slots_available": i.slots_available})
        return jsonify({"vaccine": res_li})


@app.route('/register', methods=['POST'])
def register():
    client = ndb.Client()
    with client.context():
        a = request.get_json(force=True)
        name = a.get('name')
        age = a.get('age')
        aadhaar_no = a.get('aadhaar_no')
        phone_no = a.get('phone_no')
        address = a.get('address')
        res = People(name=name, age=age, aadhaar_no=aadhaar_no, phone_no=phone_no, address=address)
        res.put()


if __name__ == "__main__":
    app.run(debug=True)


