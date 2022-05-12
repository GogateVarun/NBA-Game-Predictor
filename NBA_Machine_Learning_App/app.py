from flask import Flask, render_template, redirect, url_for, request, jsonify
import pymongo
import UserInputCleaning
import ML


app = Flask(__name__)

client = pymongo.MongoClient("mongodb://team3:vegas@cluster0-shard-00-00.vttn9.mongodb.net:27017,cluster0-shard-00-01.vttn9.mongodb.net:27017,cluster0-shard-00-02.vttn9.mongodb.net:27017/NBA_odds?ssl=true&replicaSet=atlas-bu6vn9-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.NBA_odds

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=['GET','POST'])
def submit():

    print('Grabbing Data...')
    home_away_input = request.args.get('home_away')
    bet_ml_input = request.args.get('bet_ml')
    value_ml_input = request.args.get('value_ml')
    bet_spread_input = request.args.get('bet_spread')
    value_spread_input = request.args.get('value_spread')
    odds_spread_input = request.args.get('odds_spread')
    bet_ou_input = request.args.get('bet_ou')
    value_ou_input = request.args.get('value_ou')
    odds_ou_input = request.args.get('odds_ou')

    user_inputs = {
        'home_away': home_away_input,
        'bet_ml': bet_ml_input,
        'value_ml': value_ml_input,
        'bet_spread': bet_spread_input,
        'value_spread':value_spread_input,
        'odds_spread':odds_spread_input,
        'bet_ou': bet_ou_input,
        'value_ou': value_ou_input,
        'odds_ou': odds_ou_input
    }

    user_inputs = dict(user_inputs)
  
    collection = db.get_collection('Input Table')
    collection.insert_many([user_inputs])
    clean_user_inputs = UserInputCleaning.clean_inputs(user_inputs)

    output = ML.run_models(clean_user_inputs)

    return jsonify(output)

if __name__ == "__main__":
   app.run()