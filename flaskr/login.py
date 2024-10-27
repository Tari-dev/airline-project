from flask import Blueprint, request, Response, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flaskr.db import get_db

# Blueprint setup
login_app = Blueprint('login', __name__)



@login_app.route('/login', methods=['GET', 'POST'])
def login_and_register():
    if request.method == 'POST':
        action = request.form.get('action')

        db = get_db()
        cursor = db.cursor()

        username = request.form.get('username')
        password = request.form.get('password')

        user = cursor.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

        if user and check_password_hash(user['password'], password):
            # Clear any existing session data
            session.clear()
            # Create new session
            session['user_id'] = user['userid']
            # Set session to non-permanent
            session.permanent = False

            cursor.execute('UPDATE users SET LastLogin = ? WHERE userid = ?', (datetime.now(), user['userid']))
            db.commit()
            return render_template('index.html')
        else:
            return Response('Invalid username or password!', status=401, mimetype='text/plain')

    return render_template('login-signup-pwdreset.html')

@login_app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    return render_template('login-signup-pwdreset.html')

@login_app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        phonenumber = request.form.get('phno')
        password = request.form.get('password')

        hashed_password = generate_password_hash(password)

        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO users (username, email, phonenumber, password)
            VALUES (?, ?, ?, ?)
        ''', (username, email, phonenumber, hashed_password))

        db.commit()

        return Response('User registered successfully!', status=201, mimetype='text/plain')
        
        
