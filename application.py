import random
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    name = request.args.get("name") # dont foget in import request
    if not name:
        return render_template("Failure.html")
    return render_template("Hello.html", name = name)