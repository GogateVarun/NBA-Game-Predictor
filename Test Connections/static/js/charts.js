// Create the function to alunch charts on intitial page load
function init() {
  var gaugeData = [
    {
      domain: { x: [0, 1], y: [0, 1] },
      // The value is where we'll need to link to the resulting number from the model
      value: 50,
      title: { text: "<b>Moneyline?</b><br>Probability of<br>Moneyline Bets<br>Resulting in a Win"},
      type: "indicator",
      mode: "gauge+number",
      gauge: {
        axis: {
          range: [null, 100],
          tickmode: "array",
          tickvals: [0,20,40,60,80,100],
          ticktext: [0,20,40,60,80,100]
        },
        bar: {color: "black"},
        steps: [
          { range: [0, 20], color: "red" },
          { range: [20, 40], color: "orange" },
          { range: [40, 60], color: "yellow" },
          { range: [60, 80], color: "lime" },
          { range: [80, 100], color: "green" }]
      }
    }
  ];
  
  // 5. Create the layout for the gauge chart.
  var gaugeLayout = { 
    autosize: true,
    annotations: [{
      xref: 'paper',
      yref: 'paper',
      x: 0.5,
      xanchor: 'center',
      y: 0,
      yanchor: 'center',
      text: "Testing for gauge reactivity<br>just putting in placeholders",
      showarrow: false
    }]
  };

  // 6. Use Plotly to plot the gauge data and layout.
  Plotly.newPlot("gauge_ml", gaugeData, gaugeLayout, {responsive: true});
};

// Initialize the charts on the dashboard with a static number
init();

// 1. Create the buildCharts function.
function build_charts_function(data) {
    // Money Line Gauge First
    // 1. Create a variable that filters the metadata array for the object with the desired sample number.
    // 2. Create a variable that holds the first sample in the metadata array.
    // var ml_output = data[0];
    // console.log(metadata_UserId);
    console.log(data)
    var new_data = Object.values(data)
    console.log(new_data)
    // 3. Create a variable that holds the washing frequency.
    // var washFreq = +metadata_UserId[0].wfreq;
    var ml_value = (new_data[0])*100
    // 4. Create the trace for the gauge chart.
    console.log(ml_value)
    var gaugeData = [
      {
        domain: { x: [0, 1], y: [0, 1] },
        // The value is where we'll need to link to the resulting number from the model
        value: ml_value,
        title: { text: "<b>Moneyline?</b><br>Probability of<br>Moneyline Bets<br>Resulting in a Win"},
        type: "indicator",
        mode: "gauge+number",
        gauge: {
          axis: {
            range: [null, 100],
            tickmode: "array",
            tickvals: [0,20,40,60,80,100],
            ticktext: [0,20,40,60,80,100]
          },
          bar: {color: "black"},
          steps: [
            { range: [0, 20], color: "red" },
            { range: [20, 40], color: "orange" },
            { range: [40, 60], color: "yellow" },
            { range: [60, 80], color: "lime" },
            { range: [80, 100], color: "green" }]
        }
      }
    ];
    
    // 5. Create the layout for the gauge chart.
    var gaugeLayout = { 
      autosize: true,
      annotations: [{
        xref: 'paper',
        yref: 'paper',
        x: 0.5,
        xanchor: 'center',
        y: 0,
        yanchor: 'center',
        text: "Testing for gauge reactivity<br>just putting in placeholders",
        showarrow: false
      }]
    };

    // 6. Use Plotly to plot the gauge data and layout.
    Plotly.newPlot("gauge_ml", gaugeData, gaugeLayout, {responsive: true});
}