from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Fetch environment variables
hostname = os.getenv("HOSTNAME")
database = os.getenv("DATABASE")
username = os.getenv("USER")
password = os.getenv("PASSWORD")
port = os.getenv("PORT_ID")
secret_key = os.getenv("SECURITY")

# Configure SQLAlchemy database connection
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@{hostname}/{database}"
app.config["SECRET_KEY"] = secret_key
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)