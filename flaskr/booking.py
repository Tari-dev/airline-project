from flask import Blueprint, request, redirect, render_template,url_for,session,flash
from datetime import datetime
import sqlite3 as sql


booking_app = Blueprint('booking', __name__)

# Define the route for booking a flight
@booking_app.route('/passenger_details', methods=['POST'])
def book_flight():
    # Retrieve flight data from the form
    flight_id = request.form.get('flight_id')
    
    fare = request.form.get('fare')
    user_id = session.get('user_id')  # Change to 'user_id'

    if not user_id:
        flash("Please log in to book a flight.")
        return render_template('login-signup-pwdreset.html')  # Adjust if 'login' blueprint or function name differs

    # Insert booking information into the database
    with sql.connect('airline.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Bookings (UserId, FlightId, Fare, BookingDate, BookingStatus)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, flight_id, fare, datetime.now(), 'Confirmed'))
        conn.commit()
    
    flash("Flight booked successfully!")
    return render_template('passenger.html') # Adjust to your main homepage or a confirmation page