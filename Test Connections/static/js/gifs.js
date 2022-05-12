// Create the function to alunch charts on intitial page load
function init() {

}

// Initialize the charts on the dashboard with a static number
init();

function gif_updater_function(data) {

    
    // var docs = document.getElementById("img");
    // docs.setAttribute("src", "gif_path");

    // var myframe = document.getElementsByTagName("iframe")[0];

    var new_data = Object.values(data)

    var ml_value = (new_data[0])*100
    var spread_value = (new_data[1])*100
    var OU_value = (new_data[2])*100

    // var p = document.getElementById("output");

    // var iframe = document.getElementById("iframe"); 
    // // console.log(iframe.id, iframe.name);


    
    //src="https://giphy.com/embed/syBmkKtvQ2xYgSX22t"
    
    if (ml_value >= 66) {
        
        document.getElementById('ml_gif').setAttribute('src',"https://giphy.com/embed/JTy79YRYXtPy3YNWbg")
        //src="https://giphy.com/embed/JTy79YRYXtPy3YNWbg" 
        // myframe.id = "Steve"

        //output.textContent = "Go for it!"
        
      } else if (ml_value >=50) {
        document.getElementById('ml_gif').setAttribute('src',"https://giphy.com/embed/syBmkKtvQ2xYgSX22t")
        //src="https://giphy.com/embed/syBmkKtvQ2xYgSX22t"
        
        //output.textContent = "Chances are slim!"
        // myframe.id = "Westbrook"

      } else if (ml_value <50) {
        document.getElementById('ml_gif').setAttribute('src',"https://giphy.com/embed/3oAt2dA6LxMkRrGc0g")
        //src="https://giphy.com/embed/3oAt2dA6LxMkRrGc0g"

        //output.textContent = "Odds not good!"
        // myframe.id = "Harden"
      };






    if (spread_value >= 66) {
        
      document.getElementById('spread_gif').setAttribute('src',"https://giphy.com/embed/JTy79YRYXtPy3YNWbg")
      //src="https://giphy.com/embed/JTy79YRYXtPy3YNWbg" 
      // myframe.id = "Steve"

      //output.textContent = "Go for it!"
      
    } else if (spread_value >=50) {
      document.getElementById('spread_gif').setAttribute('src',"https://giphy.com/embed/syBmkKtvQ2xYgSX22t")
      //src="https://giphy.com/embed/syBmkKtvQ2xYgSX22t"
      
      //output.textContent = "Chances are slim!"
      // myframe.id = "Westbrook"

    } else if (spread_value <50) {
      document.getElementById('spread_gif').setAttribute('src',"https://giphy.com/embed/3oAt2dA6LxMkRrGc0g")
      //src="https://giphy.com/embed/3oAt2dA6LxMkRrGc0g"

      //output.textContent = "Odds not good!"
      // myframe.id = "Harden"
    };







    if (OU_value >= 66) {
        
      document.getElementById('OU_gif').setAttribute('src',"https://giphy.com/embed/JTy79YRYXtPy3YNWbg")
      //src="https://giphy.com/embed/JTy79YRYXtPy3YNWbg" 
      // myframe.id = "Steve"

      //output.textContent = "Go for it!"
      
    } else if (OU_value >=50) {
      document.getElementById('OU_gif').setAttribute('src',"https://giphy.com/embed/syBmkKtvQ2xYgSX22t")
      //src="https://giphy.com/embed/syBmkKtvQ2xYgSX22t"
      
      //output.textContent = "Chances are slim!"
      // myframe.id = "Westbrook"

    } else if (OU_value <50) {
      document.getElementById('OU_gif').setAttribute('src',"https://giphy.com/embed/3oAt2dA6LxMkRrGc0g")
      //src="https://giphy.com/embed/3oAt2dA6LxMkRrGc0g"

      //output.textContent = "Odds not good!"
      // myframe.id = "Harden"
    }


  };



    //<iframe src="https://giphy.com/embed/ycllbrN3Kx27e" width="480" height="468" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/funny-eye-roll-reactiongif-ycllbrN3Kx27e">via GIPHY</a></p>