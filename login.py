from flask import Blueprint, request, Response, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import sqlite3 as sql

# Blueprint setup
login_app = Blueprint('login', __name__)

DATABASE = 'airline.db'

@login_app.route('/templates/login-signup-pwdreset.html', methods=['GET', 'POST'])
def login_and_register():
    if request.method == 'POST':
        action = request.form.get('action')
        conn = sql.connect(DATABASE)

        if action == 'register':
            username = request.form.get('username')
            email = request.form.get('email')
            phonenumber = request.form.get('phonenumber')
            password = request.form.get('password')

            hashed_password = generate_password_hash(password)

            conn.execute('''
                INSERT INTO users (username, email, phonenumber, password)
                VALUES (?, ?, ?, ?)
            ''', (username, email, phonenumber, hashed_password))

            conn.commit()
            conn.close()

            return Response('User registered successfully!', status=201, mimetype='text/plain')

        elif action == 'login':
            username = request.form.get('username')
            password = request.form.get('password')

            user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

            if user and check_password_hash(user['password'], password):
                conn.execute('UPDATE users SET last_login = ? WHERE userid = ?',
                             (datetime.now(), user['userid']))
                conn.commit()
                conn.close()
                return Response(f'Login successful! Status: {user["status"]}', status=200, mimetype='text/plain')
            else:
                conn.close()
                return Response('Invalid username or password!', status=401, mimetype='text/plain')

    return render_template('login-signup-pwdreset.html')
