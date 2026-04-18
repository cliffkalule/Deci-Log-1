from flask import Flask, request, jsonify


app = Flask(__name__)

users = []

print("Hello world")

@app.route("/") # decorator function - magic functon that makes the return to app in the browser
def hello_world():
    name = {"name" : "eric", "nationality" : "Ugandan"}
    return f"Hello, {name['name']}! You are {name['nationality']}"


# @app.route("/about/<name>")
# def about(name):
#     return f"hello from about {name}"

# @app.route("/user/<name>")
# def user(name):
#         users = [{
#             "name": "eric"
#         },                
#         {"name": "kevin",
#          "age":"20"
#         }         
#         ]        
#         for i in users:
#             if i["name"] == name:
#                 return jsonify(i)
#         return "User not found"
        
# @app.route("/articles/create", methods=["GET","POST"])
# def articles():
#     if request.method == "POST":
#         user = {
#             "name": request.form.get("name"),
#             "email": request.form.get("email")
#         }
#         users.append(user) 
#         return jsonify(users)
#     else:
#         return "Send a POST request to create a user"
