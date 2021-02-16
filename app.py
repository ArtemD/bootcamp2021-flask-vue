from flask import Flask
from flask import render_template, request, redirect
from database.operations import insert_db_data
from api import get_json

app = Flask(__name__)

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

@app.route('/api/search/')
@app.route('/api/search/<keyword>')
def search(keyword=None):
    return get_json(False, keyword)

@app.route('/api/all')
def api():
    return get_json()

if __name__ == '__main__':
    app.config['DEBUG']=True
    app.run(threaded=True, port=5000)