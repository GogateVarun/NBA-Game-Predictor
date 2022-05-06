
var inputs = {};

function grabInputs(){
    var input_values = d3.select("#input1");
    console.log(input_values)
    d3.json("http://127.0.0.1:5000/submit?").then(data => console.log(data));

}

d3.select("#submit_button").on("click",grabInputs);



console.log('Hi')

//var grabingInputs = d3.selectAll("input");
//localURL = "http://127.0.0.1:5000/submit";
//3.json(localURL).then(data => console.log(data));