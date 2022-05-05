from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit")
def submit():
    return "<p>Button Works!</p>"

if __name__ == "__main__":
   app.run()