
var inputs = {};

function grabInputs(){
    var input_values = d3.select("input");
    console.log(input_values)
    d3.json("http://127.0.0.1:5000/submit?Test1=Hello&Test2=Guys").then(data => console.log(data));

}

d3.select("#submit_button").on("click",grabInputs);



console.log('Hi')

//var grabingInputs = d3.selectAll("input");
//localURL = "http://127.0.0.1:5000/submit";
//3.json(localURL).then(data => console.log(data));