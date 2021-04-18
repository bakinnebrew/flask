#includes what the routes are and what these routes should do

from flask import Flask, render_template, request, redirect, session
from flask_session import Session
app = Flask(__name__)
# will allow seash session from individuals to exist within their own browsers
app.config["SESSION PERMANENT"] = False
app.config["SESSION TYPE"] = "filesystem"
Session(app)

@app.route("/")
def tasks():
    if "todos" not in session: #this function checks the user's session to see if there is a dictionary, key value pair, of todos. if not it creates it.
        session["todos"] = []
    return render_template("tasks.html", todos=session["todos"])

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        todo = request.form.get("task")
        session["todos"].append(todo) #adds todo task to the list of todos. 
        return redirect("/")
