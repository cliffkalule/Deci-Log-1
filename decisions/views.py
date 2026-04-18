from decisions import decision_app
from decisions.models import Decision  # ✅ correct single import
from db import db
from datetime import datetime
from flask import render_template, redirect, url_for, request


# VIEWS FOR THE DECISION

# would be a place to see all decisions (lists all decsions)


@decision_app.route("/")
@decision_app.route("/decisions")
def decisions():

    # logic to retrieve all decisions from the database
    decisions = Decision.query.all()

    return render_template("home.html", decisions=decisions)


# Reading a Single Decision
@decision_app.route("/decisions/<int:id>")
def single_decision(id):
    decision = Decision.query.get_or_404(id)
    return render_template("single_decision.html", decision=decision)


# Creating a Decision
@decision_app.route("/create", methods=["GET", "POST"])
def create_decision():
    if request.method == "POST":
        # logic to create a decision

        # creating a new row on our decision table
        decision = Decision(
            title=request.form["title"],
            reason=request.form["reason"],
            confidence_level=request.form["confidence_level"],
            outcome=request.form["outcome"],
            lesson_learned=request.form["lesson_learned"],
            created_at=datetime.now(),
        )
        # commting the changes to the table
        db.session.add(decision)
        db.session.commit()
        return redirect(url_for("decision.decisions"))
        # decisions.append(decision)
    return render_template("create_decision.html")


# UPDATE
@decision_app.route("/decisions/update/<int:id>", methods=["GET", "POST"])
def update_decision(id):

    # get a specific decision in the list using the index,
    decision = Decision.query.get_or_404(id)
    # remove that decision, : option 2 --> point the index to the new decision
    # add the new decision

    # get the details from the formB
    # To do: Fix this
    if request.method == "POST":
        # updating the decision using exisiting data
        decision.title = request.form["title"]
        decision.reason = request.form["reason"]
        decision.confidence_level = request.form["confidence_level"]
        decision.outcome = request.form["outcome"]
        decision.lesson_learned = request.form["lesson_learned"]
        # committing the changes to the table
        db.session.commit()

        print(decision)
        return redirect(url_for("decision.decisions"))
    return render_template("update_decision.html", decision=decision)


# Delete a decision: standalone as we dont have to render template (used in a single)
@decision_app.route("/decisions/delete/<int:id>", methods=["GET", "POST"])
def delete_decision(id):
    decision = Decision.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(decision)
        db.session.commit()
        return redirect(url_for("decision.decisions"))
    return render_template("single_decision.html", decision=decision, id=id)


# Connecting to database using sqlite3


# db = sqlite3.connect("database.db")  # use in sqlite


# cursor = db.cursor()


# cursor.execute(
#     "CREATE TABLE IF NOT EXISTS decisions(title, reason, confidence_level, outcome, lesson_learned)"
# )
# db.commit()


if __name__ == "__main__":
    app.run(debug=True)
