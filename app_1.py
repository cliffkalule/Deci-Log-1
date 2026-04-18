from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from db import db
from flask_marshmallow import Marshmallow, fields


load_dotenv()
print("POSTGRES_URL:", os.getenv("POSTGRES_URL"))

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("POSTGRES_URL")


migrate = Migrate(app, db)


ma = Marshmallow(app)

from decisions.models import Decision, Comment

# importing blueprints and registering them
from decisions import decision_app
from users import users_app

app.register_blueprint(decision_app)
app.register_blueprint(users_app)


db.init_app(app)


# our schema for serializers
class DecisionSchema(ma.Schema):
    id = ma.Integer()
    title = ma.Str()
    reason = ma.Str()
    confidence_level = ma.Str()
    outcome = ma.Str()
    lesson_learned = ma.Str()
    due_date = ma.Str()
    created_at = ma.DateTime()


class CommentSchema(ma.Schema):
    id = ma.Integer()
    title = ma.Str()


@app.route("/comments")
def get_comments():
    comments = Comment.query.all()
    comment_schema = CommentSchema(many=True)
    return comment_schema.dumps(comments)


# This creates all tables, doesn't update tables if your models change
with app.app_context():

    db.create_all()


decision_schema = DecisionSchema(many=True)


# class DecisionSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         Model = Decision
#         fields = (
#             "id",
#             "title",
#             "reason"
#             "confidence_level",
#             "outcome",
#             "lesson_learned",
#             "due_date",
#             "created_at",
#         )


@app.route("/api")
def get_decisions():
    decisions = Decision.query.all()
    cleaned_decision = []
    # for decision in decisions:
    #     clean = {
    #         "id": decisions.id,
    #         "title": decision.title,
    #     }
    #     cleaned_decision.append(decision.as_dict())

    # This  renders out html
    # return render_template("home.html", decisions=decisions)

    # decisions = [{"title": "my title"}, {"title": "my title 2"}]
    # # return data in terms of JSON/XML
    # print(decisions)
    # # print(cleaned_decisions)

    # print(decisions)
    # decision = Decision.query.get_or_404(4)
    decision_schema = DecisionSchema(many=True)
    return decision_schema.dump(decisions)


if __name__ == "__main__":
    app.run(debug=True)

# print(decisions)
# decision = Decision.query.get_or_404(4)
# decision_schema = DecisionSchema(many=True)
# print(decision_schema.dump(decision))
# return decision_schema.dump(decisions)
