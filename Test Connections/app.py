from flask import Flask, render_template, redirect, url_for, request
#from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)

#client = MongoClient("mongodb+srv://team3:vegas@cluster0.sqdyt.mongodb.net/test?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb://team3:vegas@cluster0-shard-00-00.vttn9.mongodb.net:27017,cluster0-shard-00-01.vttn9.mongodb.net:27017,cluster0-shard-00-02.vttn9.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-bu6vn9-shard-0&authSource=admin&retryWrites=true&w=majority")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=['GET','POST'])
def submit():

    print('Heres the Dictionary')
    print(request.args.to_dict())
    #print(input1)
    db = client.get_database('NBA_odds')
    collection = db.get_collection('Test')
    collection.insert_many([request.args.to_dict()])


    #request.args.get('Key Name')
    #request.args.to_dict()
    #print(request.args.to_dict())

    return 'asdvadbv'

if __name__ == "__main__":
   app.run()