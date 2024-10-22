from flask import Flask
from index import index_app  # Import the Flask app (blueprint) from index.py
from login import login_app  # Import the login blueprint from login.py

app = Flask(__name__)
app.register_blueprint(index_app)  # Register the blueprint from index.py
app.register_blueprint(login_app)  # Register the login blueprint from login.py

if __name__ == '__main__':
    app.run(debug=True)
