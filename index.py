from flask import Flask, render_template, redirect, request
import sqlite3 as sql
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
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/book_a_flight', methods=['GET', 'POST'])
def book_a_flight():
    if request.method == 'POST':
        From = request.form['from']
        To = request.form['to']
        Passengers = request.form['passenger']
        conn = sql.connect('airline.db')
        c = conn.cursor()
        q = 'SELECT DEPARTUREAIRPORT, ARRIVALAIRPORT, AircraftType, Price FROM FLIGHT WHERE DEPARTUREAIRPORT LIKE ? AND ARRIVALAIRPORT LIKE ?'
        c.execute(q, (From, To))
        table = c.fetchall()
        conn.close()
        departf=codes[From]
        arrivalf=codes[To]
        return render_template('bookingpage.html', tables=table,From=departf,To=arrivalf)
    return render_template('index.html')


@app.route('/manage', methods=['GET', 'POST'])
def manage():
    if request.method == 'POST':
        refno = request.form['reference_number']
        lastname = request.form['last_name']  
        conn = sql.connect('airline.db')
        c = conn.cursor()
        q = 'DELETE FROM TABLE_NAME WHERE REFERENCE_NUMBER=?'
        c.execute(q, (refno,))
        conn.commit()
        conn.close()
        return redirect('message.html') 
    return render_template('intropage.html')


@app.route('/flight_status', methods=['GET', 'POST'])
def flight_status():
    if request.method == 'POST':
        From = request.form['from']
        To = request.form['to']
        date = request.form['date']
        conn = sql.connect('airline.db')
        c = conn.cursor()
        q = 'SELECT * FROM TABLE_NAME WHERE FROM=? AND TO=?'  # Change the table name
        c.execute(q, (From, To))
        val = c.fetchall()
        conn.close()
        return render_template('intropage.html', table=val)
    return render_template('intropage.html')


if __name__ == '__main__':
    app.run(debug=True)
