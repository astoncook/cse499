// Defines the global and mod variables.
var global = "";
var mod = '';

// Function to fetch the data from the server.
function fetchResult(event) {
  var x = document.getElementById('input').value
  if (x == "") {
    var mmmm = 0
  } else {
    var req = new XMLHttpRequest();
    var form = document.getElementById('result');
    var dataForm = new FormData(form);
    // This function is called when the request is ready.
    req.onreadystatechange = function () {
      if (req.readyState == 4 && req.status == 200) {
        var response = JSON.parse(req.responseText);
        var input1 = response['ticker'];
        // If the input is not empty, then the following code is executed.
        if (input1 != undefined) {
          document.getElementById('logo').innerHTML = "<img class='logo1' src= " + response['logo'] + ">"
          document.getElementById('company').innerHTML = response['name']
          document.getElementById('ticker').innerHTML = response['ticker']
          document.getElementById('code').innerHTML = response['exchange']
          document.getElementById('date').innerHTML = response['ipo']
          document.getElementById('category').innerHTML = response['finnhubIndustry']
          global = response['ticker']
        } else {
          document.getElementById('error').style.display = 'block';
          document.getElementById('table1').style.display = 'none';
          document.getElementById('navbar').style.display = 'none';
          document.getElementById('table2').style.display = 'none';
          document.getElementById('container').style.display = 'none';
          document.getElementById('block4').style.display = 'none';
        }
      }
    }
  };

  // Gets route 1 ready and sends it to the server.
  var param = new URLSearchParams(dataForm);
  param = param.toString();
  req.open('GET', '/route1?' + param, true);
  req.send(null);
  event.preventDefault();

};

// This function gets the data ready for route 2 and sends it to the server.
function fetchResult2(event) {
  var req = new XMLHttpRequest();
  var form = document.getElementById('result');
  var dataForm = new FormData(form);
  req.onreadystatechange = function () {
    if (req.readyState == 4 && req.status == 200) {
      var response = JSON.parse(req.responseText);
      // All of the stock summary data.
      document.getElementById('STS').innerHTML = response['symbol']
      document.getElementById('TD').innerHTML = response['t']
      document.getElementById('PCP').innerHTML = response['pc']
      document.getElementById('OP').innerHTML = response['o']
      document.getElementById('HP').innerHTML = response['h']
      document.getElementById('LP').innerHTML = response['l']
    }
  }

  // This is calling route 2 and sending the data to the server.
  var param = new URLSearchParams(dataForm);
  param = param.toString();
  req.open('GET', '/route2?' + param, true);
  req.send(null);
  event.preventDefault();
};

// This function will help break up the company data and style it.
function companyInformation() {
  mod = 1;
  document.getElementById('table1').style.display = 'block';
  document.getElementById('table2').style.display = 'none';
  document.getElementById('container').style.display = 'none';
  document.getElementById('block4').style.display = 'none';
  document.getElementById('navbar').style.display = 'block';
}

// This function will help break up the stock summary data and style it.
function stockInfo() {
  mod = 2;
  document.getElementById('table2').style.display = 'block';
  document.getElementById('table1').style.display = 'none';
  document.getElementById('container').style.display = 'none';
  document.getElementById('block4').style.display = 'none';
}

// This function will help break up the chart data and style it.
function charts() {
  mod = 3;
  document.getElementById('table1').style.display = 'none';
  document.getElementById('table2').style.display = 'none';
  document.getElementById('container').style.display = 'block';
  document.getElementById('block4').style.display = 'none';

  // This is the start of the chart in nav bar column 3.
  Highcharts.getJSON('/route3', function (data) {
    const d = new Date()
    dd = d.getMonth() + 1
    // This helps with the bottom scroll bar getting the full year info.
    datetime = d.getFullYear() + "-0" + dd + "-" + d.getDate()
    // This is the start of the chart.
    var currentStockPrice = [],
      dataLength = data.length,
      i = 0;

    // This is the loop that will help break up the data.
    for (i; i < dataLength; i += 1) {
      currentStockPrice.push([
        data[i][0],
        data[i][1],
      ]);
    }

    // This is the chart.
    Highcharts.stockChart('container', {
      rangeSelector: {
        selected: 1
      },

      // This is the title of the chart.
      title: {
        text: global + ' Stock Price ' + datetime
      },
      // Labels for the x-axis.
      yAxis: [{
        opposite: false,
        labels: {
          align: 'right',
          x: -3
        },
        title: {
          text: 'Stock Price'
        },
        height: '100%',
        lineWidth: 2,
        resize: {
          enabled: true
        }
      }, {
        labels: {
          align: 'right',
          x: -3
        },
        height: '100%',
        offset: 0,
        lineWidth: 2
      }],
      plotOptions: {
        series: {
          pointWidth: 5
        }
      },

      // Helps select range from a week to 3 months.
      rangeSelector: {
        selected: 0,
        inputEnabled: false,
        buttons: [{
          type: 'day',
          count: 7,
          text: '7d',
        }, {
          type: 'day',
          count: 15,
          text: '15d',
        }, {
          type: 'month',
          count: 1,
          text: '1m',
        }, {
          type: 'month',
          count: 3,
          text: '3m',
        }]
      },

      // This is the data for the chart.
      series: [{
        name: global + ' Stock Price',
        data: currentStockPrice,
        type: 'area',
        threshold: null,
        tooltip: {
          valueDecimals: 2
        },

        // Filling the area between the two lines.
        fillColor: {
          linearGradient: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 1
          },

          // This is the color of the area.
          stops: [
            [0, Highcharts.getOptions().colors[0]],
            [1, Highcharts.color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
          ]
        }
      }]
    });
  });
}

// This function helps with the "x" button on the search bar.
function reset() {
  mod = 0;
  document.getElementById('table1').style.display = 'none';
  document.getElementById('table2').style.display = 'none';
  document.getElementById('container').style.display = 'none';
  document.getElementById('block4').style.display = 'none';
  document.getElementById('navbar').style.display = 'none';
  document.getElementById('error').style.display = 'none';
}

// This function will return the data corresponding to the element clicked.
function elementClicking() {
  if (mod == 2) {
    document.getElementById('button2').click()
  } else if (mod == 3) {
    document.getElementById('button3').click()
  } else {
    document.getElementById('button1').click()
  }
};