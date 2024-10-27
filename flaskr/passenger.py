from flask import Blueprint, request, redirect, render_template, url_for, session, flash
from datetime import datetime
import sqlite3 as sql

# Blueprint setup
passenger_app = Blueprint('passenger', __name__)


# Route to handle form submission
@passenger_app.route('/services', methods=['POST'])
def passenger_details():
        # Retrieve form data
        gender = request.form.get('gender')
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        dob = request.form.get('dob')
        contact_number = request.form.get('contact')
        email = request.form.get('email')
        address = request.form.get('address')

      

        # Convert date if provided
        dob_date = None
        if dob:
            try:
                dob_date = datetime.strptime(dob, "%d-%m-%Y").date()
            except ValueError:
                flash("Invalid date format. Please use dd-mm-yyyy format.", "error")
                return redirect(url_for('passenger.show_passenger_form'))

        # Insert into database
        with sql.connect("airline.db") as con:
            cursor = con.cursor()
            cursor.execute("""
                INSERT INTO passengers 
                (FirstName, LastName, Gender, Dob, ContactNumber, Email, Address) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, 
                (first_name, last_name, gender, dob_date, contact_number, email, address)
            )
            con.commit()
            
            # Store passenger ID in session for later use
          
            
            flash("Passenger details added successfully!", "success")
            return render_template('services.html')  # Assuming 'services.show_services' is the route for services.html
