from flask import Blueprint, render_template, request,session
from flaskr.db import get_db

# Blueprint setup
index_app = Blueprint('index', __name__)

# Dictionary for airport codes
codes = {
    'COK': 'Cochin International Airport',
    'CCJ': 'Calicut International Airport',
    'TRV': 'Trivandrum International Airport',
    'CNN': 'Kannur International Airport',
    'MAA': 'Chennai International Airport',
    'BOM': 'Chhatrapati Shivaji Maharaj International Airport',
    'BLR': 'Kempegowda International Airport',
    'SHJ': 'Sharjah International Airport',
    'DXB': 'Dubai International Airport',
    'AUH': 'Abu Dhabi International Airport',
    'DOH': 'Hamad International Airport',
    'BAH': 'Bahrain International Airport',
    'LHR': 'London Heathrow Airport',
    'JFK': 'John F. Kennedy International Airport'
}


@index_app.route('/')
def home():
    return render_template('index.html')

@index_app.route('/book_a_flight', methods=['GET', 'POST'])
def book_a_flight():
    if request.method == 'POST':
        From = request.form['from']
        To = request.form['to']
        Passengers = request.form['passenger']
        conn = get_db()
        c = conn.cursor()
        q = 'SELECT DEPARTUREAIRPORT, ARRIVALAIRPORT, AircraftType, Price FROM Flight WHERE DEPARTUREAIRPORT LIKE ? AND ARRIVALAIRPORT LIKE ?'
        c.execute(q, (From, To))
        table = c.fetchall()
        conn.close()
        departf = codes[From]
        arrivalf = codes[To]
        return render_template('bookingpage.html', tables=table, From=departf, To=arrivalf)
    return render_template('index.html')

@index_app.route('/manage', methods=['GET', 'POST'])
def manage():
    if request.method == 'POST':
        From = request.form['from']
        To = request.form['to']
        Passengers = request.form['passenger']
        conn = get_db()
        c = conn.cursor()
        q = 'SELECT DEPARTUREAIRPORT, ARRIVALAIRPORT, AircraftType, Price FROM Flight WHERE DEPARTUREAIRPORT LIKE ? AND ARRIVALAIRPORT LIKE ?'
        c.execute(q, (From, To))
        table = c.fetchall()
        conn.close()
        departf = codes[From]
        arrivalf = codes[To]
        return render_template('bookingpage.html', tables=table, From=departf, To=arrivalf)
    return render_template('index.html')

@index_app.route('/flight_status', methods=['GET', 'POST'])
def flight_status():
    if request.method == 'POST':
        From = request.form['from']
        To = request.form['to']
        date = request.form['date']
        conn = get_db()
        c = conn.cursor()
        q = 'SELECT * FROM FLIGHT WHERE FROM=? AND TO=?'  # Change table name
        c.execute(q, (From, To))
        val = c.fetchall()
        conn.close()
        return render_template('flightstatus.html', table=val)  # Add a status display page
    return render_template('intropage.html')
