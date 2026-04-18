from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///decisions.db"

# Defining the DB and attaching our app
db = SQLAlchemy(app)

# db.init_app(app)

# this will act as our database (a list of dictionaries)
decisions = [
    {
        "title": "Invest in Bitcoin",
        "reason": "Market trend looked strong and many analysts predicted growth",
        "confidence_level": "3",
        "outcome": "Price dropped shortly after investment",
        "lesson_learned": "Avoid investing based only on hype, do deeper research",
        "created_at": "2026-03-05",
    },
    {
        "title": "Start a Flask teaching project",
        "reason": "Students learn better by building real applications",
        "confidence_level": "2",
        "outcome": "Students engaged more and asked deeper questions",
        "lesson_learned": "Hands-on projects drive deeper understanding than theory alone",
        "created_at": "2026-03-08",
    },
    {
        "title": "Wake up at 5 AM daily",
        "reason": "More quiet time for focused work",
        "confidence_level": "5",
        "outcome": "Productivity improved in the mornings",
        "lesson_learned": "Protecting early morning hours is one of the highest ROI habits",
        "created_at": "2026-02-01",
    },
    {
        "title": "Buy a second monitor",
        "reason": "Coding and teaching would be easier with more screen space",
        "confidence_level": "4",
        "outcome": "Workflow became faster and more organized",
        "lesson_learned": "Small environment upgrades can have a big impact on daily output",
        "created_at": "2026-01-15",
    },
    {
        "title": "Use Excalidraw for teaching diagrams",
        "reason": "It is simple, visual, and good for explaining systems",
        "confidence_level": "5",
        "outcome": "Students understood system architecture faster",
        "lesson_learned": "Visual tools lower the barrier to understanding complex systems",
        "created_at": "2026-02-20",
    },
]

# structure of a single decision (so far this does nothing)
decision = {
    "title": "",  # text
    "reason": "",  # text
    "confidence level": "",  # integer
    "outcome": "",  # text
    "lesson_learned": "",  # text
    "created_at": "",  # date
}


# A Model -- defines a table in our SQL database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    reason = db.Column(db.String(100))
    confidence_level = db.Column(db.String(100))
    outcome = db.Column(db.String)
    lesson_learned = db.Column(db.Text)
    created_at = db.Column(db.DateTime)


with app.app_context():
    db.create_all()


# Views

# would be a place to see all decisions (lists all decsions)


@app.route("/decisions")
def home():

    # logic to retrieve all decsions from the database

    return render_template("home.html", decisions=decisions)


# CRUD


# Reading a Single Decision
@app.route("/decisions/<int:id>")
def single_decision(id):
    # decision = Decision(
    # rendered_decision = None
    for decision in decisions:
        # print(decisions[id])
        # rendered_decision = decisions[id]
        return render_template("single_decision.html", decision=decisions[id])


# Creating a Decision
@app.route("/create", methods=["GET", "POST"])
def create_decision():
    if request.method == "POST":
        # logic to create a decision
        decision = {
            "title": request.form["title"],
            "reason": request.form["reason"],
            "confidence_level": request.form["confidence_level"],
            "outcome": request.form["outcome"],
            "lesson_learned": request.form["lesson_learned"],
            "created_at": request.form["created_at"],
        }
        decisions.append(decision)

        #         decision = Decision(
        #     title=request.form["title"],
        #     reason=request.form["reason"],
        #     confidence_level=request.form["confidence_level"]
        # )
        # db.session.add(decision)
        # db.session.commit()

        print("We have posted 👌", decisions)
    #     # rendered_decision = decisions[id]
    return render_template("create_decision.html", decisions=decisions)


# UPDATE
@app.route("/decisions/update/<int:id>", methods=["GET", "POST"])
def update_decision(id):

    # get a specific decision in the list using the index,
    # remove that decision, : option 2 --> point the index to the new decision
    # add the new decision

    if request.method == "POST":
        update_decision = {
            "title": request.form["title"],
            "reason": request.form["reason"],
            "confidence_level": request.form["confidence_level"],
            "outcome": request.form["outcome"],
            "lesson_learned": request.form["lesson_learned"],
            "created_at": request.form["created_at"],
        }
        decisions[id] = update_decision
        print(decisions)

    decision = ""
    for decision in decisions:
        return render_template(
            "update_decision.html", decision=decisions[id], id=id, decisions=decisions
        )

    # print(decisions)
    # rendered_decision = None
    # for decision in decisions:
    #     print(decisions[id])
    # rendered_decision = decisions[id]
    return render_template("update_decision.html", decision=decision)


# Delete a Decision
@app.route("/decisions/delete/<int:id>", methods=["GET", "POST"])
def delete_decision(id):
    decisions.pop(id)
    return redirect("/")


#     "Invest in Bitcoin",
#     "reason": "Market trend looked strong and many analysts predicted growth",
#     "confidence_level": "3",
#     "outcome": "Price dropped shortly after investment",
#     "lesson_learned": "Avoid investing based only on hype, do deeper research",
#     "created_at": "2026-03-05"
# },


# Connecting to database using sqlite3


db = sqlite3.connect("database.db")  # use in sqlite


cursor = db.cursor()


cursor.execute(
    "CREATE TABLE IF NOT EXISTS decisions(title, reason, confidence_level, outcome, lesson_learned)"
)
db.commit()


# cursor.execute("DROP TABLE movie")


# from flask import Flask, render_template


# app = Flask(__name__)

# # this will act as our database
# decisions = []

# # this will act as our database (a list of dictionaries)
# decisions = [
#     {
#         "title": "Invest in Bitcoin",
#         "reason": "Market trend looked strong and many analysts predicted growth",
#         "confidence_level": "3",
#         "outcome": "Price dropped shortly after investment",
#         "lesson_learned": "Avoid investing based only on hype, do deeper research",
#         "created_at": "2026-03-05",
#     },
#     {
#         "title": "Start a Flask teaching project",
#         "reason": "Students learn better by building real applications",
#         "confidence_level": "2",
#         "outcome": "Students engaged more and asked deeper questions",
#         "lesson_learned": "Hands-on projects drive deeper understanding than theory alone",
#         "created_at": "2026-03-08",
#     },
#     {
#         "title": "Wake up at 5 AM daily",
#         "reason": "More quiet time for focused work",
#         "confidence_level": "5",
#         "outcome": "Productivity improved in the mornings",
#         "lesson_learned": "Protecting early morning hours is one of the highest ROI habits",
#         "created_at": "2026-02-01",
#     },
#     {
#         "title": "Buy a second monitor",
#         "reason": "Coding and teaching would be easier with more screen space",
#         "confidence_level": "4",
#         "outcome": "Workflow became faster and more organized",
#         "lesson_learned": "Small environment upgrades can have a big impact on daily output",
#         "created_at": "2026-01-15",
#     },
#     {
#         "title": "Use Excalidraw for teaching diagrams",
#         "reason": "It is simple, visual, and good for explaining systems",
#         "confidence_level": "5",
#         "outcome": "Students understood system architecture faster",
#         "lesson_learned": "Visual tools lower the barrier to understanding complex systems",
#         "created_at": "2026-02-20",
#     },
# ]


# # Views

# # would be a place to see all decisions (lists all decsions)


# @app.route("/decisions")
# def get_decisions():

#     # logic to retrieve all decsions from the database

#     return render_template("home.html", decisions=decisions)


# # CRUD
# @app.route("/")
# def decision():
#     pass


if __name__ == "__main__":
    app.run(debug=True)
