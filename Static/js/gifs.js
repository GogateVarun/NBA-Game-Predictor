function updateGauge() {

    // var docs = document.getElementById("img");
    // docs.setAttribute("src", "gif_path");

    // var myframe = document.getElementsByTagName("iframe")[0];

    var p = document.getElementById("output");

    var iframe = document.getElementById("iframe"); 
    // console.log(iframe.id, iframe.name);

    
    if (ml_value >= 66) {
        
        document.getElementById('iframe').id = "Steve"
        // myframe.id = "Steve"

        output.textContent = "Go for it!"
        
      } else if (ml_value >=50) {
        document.getElementById('iframe').id = "Westbrook"
        
        output.textContent = "Chances are slim!"
        // myframe.id = "Westbrook"

      } else if (ml_value <50) {
        document.getElementById('iframe').id = "Harden"

        output.textContent = "Odds not good!"
        // myframe.id = "Harden"
      }
    };