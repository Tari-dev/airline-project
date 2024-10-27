import os
from flask import Flask
from flaskr.index import index_app
from flaskr.login import login_app
from flaskr.booking import booking_app
from flaskr.passenger import passenger_app

BLUEPRINTS = [index_app, login_app, booking_app, passenger_app]


def create_app():
    app = Flask(__name__)

    # Set a secret key for session management
    app.secret_key = os.environ.get('SECRET_KEY', 'a_default_secret_key')

    for bp in BLUEPRINTS:
        app.register_blueprint(bp)

    return app

if __name__ == '__main__':
    app = create_app()
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        app.db.close()
        print('Exiting...')

