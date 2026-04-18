from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Defining the DB and attaching our app
db = SQLAlchemy()


# MODELS FOR THE DECISION
class Decision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    reason = db.Column(db.String(100))
    confidence_level = db.Column(db.Integer)
    outcome = db.Column(db.String)
    lesson_learned = db.Column(db.Text)
    due_date = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.now())
