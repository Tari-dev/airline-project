from flaskr import Blueprint, render_template, request
from flaskr.db import get_db
import secrets


payment_app = Blueprint('payment', __name__)

@payment_app.route('/payment')
def payment_index():
    db = get_db()
    cursor = db.cursor()

    cursor.execute('SELECT * FROM bookings WHERE user_id = ?')
    return render_template('payment.html')


@payment_app.route('/process_payment', methods=['GET', 'POST'])
def process_payment():
    payment_method = request.form['payment_method']
    payment_id = secrets.token_hex(9)
    payment_amount = request.form['payment_amount']

    booking_id = request.form['booking_id']
    
    db = get_db()
    cursor = db.cursor()

    cursor.execute('''
        INSERT INTO payments (payment_id, payment_method, payment_amount)
        VALUES (?, ?, ?)
    ''', (payment_id, payment_method, payment_amount)
    )

    db.commit()

    #get booking info
    cursor.execute('SELECT * FROM bookings WHERE booking_id=?', (booking_id,))
    booking = cursor.fetchone()

    booking_info = {
        'booking_id': booking['booking_id'],
        'flight': booking['flight'],
        'amount_paid': payment_amount,
        'payment_method': payment_method,
        'flight_date': booking['date'],
        'passenger_name': booking['passenger_name'],
    }

    return render_template('payment_success.html', booking=booking_info)

