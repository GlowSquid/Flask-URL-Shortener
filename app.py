# Import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# Create new flask app
app = Flask(__name__)
# Config from settings.py
app.config.from_object('settings')
# Initiate DB
db = SQLAlchemy(app)

# Set up flask CSRF
csrf = CSRFProtect(app)
