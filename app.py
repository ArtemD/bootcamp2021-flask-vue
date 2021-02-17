from flask import Flask
from flask import render_template, request, redirect
from database.operations import insert_db_data
from api import get_json

app = Flask(__name__)
""" Flask instance """

@app.route('/')
def index():
    """
    Display homepage template
    """
    return render_template('front-page.html')

@app.route('/form')
def form():
    """
    Display form for content insertion
    """
    return render_template('form.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    """
    Process form's data or redirect if data is not correct.

    Also redirects if methods!=POST
    """
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
    """
    Display search results in JSON format

    Parameters
    ----------
    keyword : str
        Search keyword. Default None
    """
    return get_json(False, keyword)

@app.route('/api/all')
def api():
    """
    Return all rows found in database in JSON format
    """
    return get_json()

if __name__ == '__main__':
    app.config['DEBUG']=True
    """ Set debugging on when using localhost """
    app.run(threaded=True, port=5000)
    """ Run Flask dev server on port 5000 """