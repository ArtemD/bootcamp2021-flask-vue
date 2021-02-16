from flask import Flask
from flask import render_template, jsonify, request, redirect
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL']
db = create_engine(DATABASE_URL)

def insert_db_data(name, address, postcode, city, date, type, businessid):
    sql = text("""INSERT INTO 
    alcohol_license_places("name", address, postcode, city, license_granting_date, license_type, business_id)
    VALUES ( :name, :address, :postcode, :city, :date, :license_type, :bid )""")
    return db.execute(sql, {'name':name, 'address':address, 'postcode':postcode, 'city':city, 'date':date, 'license_type':type, 'bid':businessid})




def get_db_data():
    sql = text('SELECT * from alcohol_license_places')
    results = db.execute(sql)
    return results

@app.route('/')
def index():
    return render_template('front-page.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():

    if request.method!='POST':
        return redirect('/form')

    if request.form['name'] and request.form['address'] and request.form['postcode'] and request.form['city'] and request.form['businessid'] and request.form['date'] and request.form['type']:
        if insert_db_data(request.form['name'], request.form['address'], request.form['postcode'], request.form['city'],request.form['date'], request.form['type'], request.form['businessid']):
            return "Data inserted"
        else:
            return "Data NOT INSERTED"
    else:
        return redirect('/form')

@app.route('/api/all')
def api():
    results = get_db_data()

    data = []
    line = 0 

    for row in results:
        r = [row['name'],row['address'], row['postcode'],  row['city'],  row['license_granting_date'],  row['license_type'], row['business_id']]
        data.insert(line, r)
        line +=1

    return jsonify({'data': data})

if __name__ == '__main__':
    app.config['DEBUG']=True
    app.run(threaded=True, port=5000)