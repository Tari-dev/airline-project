from flask import Flask
from flaskr.index import index_app
from flaskr.login import login_app


BLUEPRINTS = [index_app, login_app]

def create_app():
    app = Flask(__name__)

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
