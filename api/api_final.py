import flask
import datetime
import sqlite3 as sql
import requests

from flask import request, jsonify
from datetime import date

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

app = flask.Flask(__name__)
app.config["DEBUG"] = True

testdata = [
        {'username': 'naeem',
            'dob': '1985-08-31'}
        ]

def insert_readings(username,dob):
    DATABASE = 'test.db'
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO data (username,dob) VALUES (?,?)", (username,dob))
        con.commit()

@app.route("/", methods=['GET','POST'])
def result():
    if request.method == 'POST':
        val1 = request.form['username']
        val2 = request.form['dob']
        insert_readings(val1,val2)
        return "Done"
    else:
        insert_readings(4,3) #This works
        return render_template('main.html', name='GET')

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# endpoint to create new user

# A route to return all of the available entries in our catalog.
@app.route('/hello/all', methods=['GET'])
def api_all():
    conn = sql.connect('test.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM data;').fetchall()

    return jsonify(all_books)

@app.route('/hello', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'username' in request.args:
        username = request.args['username']
    else:
        return "Error: No username field provided. Please specify a username."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for res in testdata:
        if res['username'] == username:
            results.append(res)
            dob = res['dob']

    d = datetime.datetime.strptime(dob,'%Y-%m-%d')
    d0 = d.date()
    today=date.today()
    bday = date(today.year,d0.month,d0.day)
    delta = bday-today

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    #return jsonify(results)
    return "Hello" +username+ "  your bday is in " + str(delta.days) + " days"

if __name__ == "__main__":
    app.run(debug=True)
