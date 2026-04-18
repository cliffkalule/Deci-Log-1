from db import db
from datetime import datetime


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

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "reason": self.reason,
            "confidence_level": self.confidence_level,
            "outcome": self.outcome,
            "lesson_learned": self.lesson_learned,
            "due_date": self.due_date,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
