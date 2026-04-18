from flask import Flask, render_template



app = Flask(__name__)

# this will act as our database
# decisions = []

# this will act as our database (a list of dictionaries)
decisions = [
    {
        "title": "Invest in Bitcoin",
        "reason": "Market trend looked strong and many analysts predicted growth",
        "confidence_level": "3",
        "outcome": "Price dropped shortly after investment",
        "lesson": "Avoid investing based only on hype, do deeper research",
        "createdAt": "2026-03-05"
    },
    {
        "title": "Start a Flask teaching project",
        "reason": "Students learn better by building real applications",
        "confidence_level": "2",
        "outcome": "Students engaged more and asked deeper questions",
        "lesson": "Hands-on projects drive deeper understanding than theory alone",
        "createdAt": "2026-03-08"
    },
    {
        "title": "Wake up at 5 AM daily",
        "reason": "More quiet time for focused work",
        "confidence_level": "5",
        "outcome": "Productivity improved in the mornings",
        "lesson": "Protecting early morning hours is one of the highest ROI habits",
        "createdAt": "2026-02-01"
    },
    {
        "title": "Buy a second monitor",
        "reason": "Coding and teaching would be easier with more screen space",
        "confidence_level": "4",
        "outcome": "Workflow became faster and more organized",
        "lesson": "Small environment upgrades can have a big impact on daily output",
        "createdAt": "2026-01-15"
    },
    {
        "title": "Use Excalidraw for teaching diagrams",
        "reason": "It is simple, visual, and good for explaining systems",
        "confidence_level": "5",
        "outcome": "Students understood system architecture faster",
        "lesson": "Visual tools lower the barrier to understanding complex systems",
        "createdAt": "2026-02-20"
    },
]


# Views

# would be a place to see all decisions (lists all decsions)

@app.route("/decisions")
def decisions():

    #logic to retrieve all decsions from the database

    return render_template("home.html", decisions=decisions)
    

# CREATE
@app.route("/decisions/<int:id>")
def single_decision(id):
    # rendered_decision = None
    for decision in decisions:
        print(decisions[id])
        # rendered_decision = decisions[id]
    return render_template("single_decision.html", decision=decisions[id])


# UPDATE
# @app.route("//decisions/update<int:id>", methods = ["GET", "POST"])
# def update_decision(id):
    
#     update_decision = {

#     }
#     if request.method =="POST":
#         {
#             "title": request.form["title"],
#             "reason": request.form["reason"],
#             "condfidence_level": request.form["confidence_level"],
#             "outcomes": request.form["outcomes"],
#             "lesson_leearned": request.form["lesson_leearned"],
#             "outcomes": request.form["outcomes"],
#         }
#             print(decisions)
        
#     # rendered_decision = None
#     for decision in decisions:
#         print(decisions[id])
#         # rendered_decision = decisions[id]
#     return render_template("single_decision.html", decision=decisions[id])
   
        
#         "Invest in Bitcoin",
#         "reason": "Market trend looked strong and many analysts predicted growth",
#         "confidence_level": "3",
#         "outcome": "Price dropped shortly after investment",
#         "lesson": "Avoid investing based only on hype, do deeper research",
#         "createdAt": "2026-03-05"
#     },
    
    
if __name__=="__main__":
    app.run(debug=True)
    
    
    
# import sqlite3


# db = sqlite3.connect("database.db")


# cursor = db.cursor()


# cursor.execute("CREATE TABLE decisions(title, reason, confidence_level, outcome, lesson_learned)")


# cursor.execute("DROP TABLE movie")



