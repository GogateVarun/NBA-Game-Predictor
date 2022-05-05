# Copied over module 10 challenge app.py as a starting point
# Nothing has been edited or changed yet to reflect current project
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "//localhost:5000"
mongo = PyMongo(app)

# Default route
@app.route("/")
def index():
   # mars = mongo.db.mars.find_one()
   # return render_template("index.html", mars=mars)
   return("hi")

# Scrape route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

# Test route
@app.route("/test")
def test():
   return("hi")

if __name__ == "__main__":
   app.run()