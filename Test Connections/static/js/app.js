// The function below should be transferable to our built out app.js with same info

function grabInputs(){
    home_away_input = document.getElementById('home_away').value
    bet_ml_input = document.getElementById('bet_ml').value
    value_ml_input = document.getElementById('value_ml').value
    bet_spread_input = document.getElementById('bet_spread').value
    value_spread_input = document.getElementById('value_spread').value
    odds_spread_input = document.getElementById('odds_spread').value
    bet_ou_input = document.getElementById('bet_ou').value
    value_ou_input = document.getElementById('value_ou').value
    odds_ou_input = document.getElementById('odds_ou').value
    d3.json("http://127.0.0.1:5000/submit?home_away=" + home_away_input + "&bet_ml=" + bet_ml_input + "&value_ml=" + value_ml_input + "&bet_spread=" + bet_spread_input + "&value_spread=" + value_spread_input + "&odds_spread=" + odds_spread_input + "&bet_ou=" + bet_ou_input + "&value_ou=" + value_ou_input + "&odds_ou=" + odds_ou_input)
        .then((data) => {
            build_charts_function(data);
            gif_updater_function(data);
        });
}

d3.select("#submit_button").on("click",grabInputs);


