var global = "";
var mod = '';

function fetchResult(event) {
  var x = document.getElementById('input').value
  if (x == "") {
    var mmmm = 0
  } else {
    var req = new XMLHttpRequest();
    var form = document.getElementById('result');
    var FD = new FormData(form);
    req.onreadystatechange = function () {
      if (req.readyState == 4 && req.status == 200) {
        var response = JSON.parse(req.responseText);
        var input1 = response['ticker'];
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

  var param = new URLSearchParams(FD);
  param = param.toString();
  req.open('GET', '/test?' + param, true);
  req.send(null);
  event.preventDefault();

};


function fetchResult2(event) {
  var req = new XMLHttpRequest();
  var form = document.getElementById('result');
  var FD = new FormData(form);
  req.onreadystatechange = function () {
    if (req.readyState == 4 && req.status == 200) {
      var response = JSON.parse(req.responseText);
      document.getElementById('STS').innerHTML = response['ticker']
      document.getElementById('TD').innerHTML = response['t']
      document.getElementById('PCP').innerHTML = response['pc']
      document.getElementById('OP').innerHTML = response['o']
      document.getElementById('HP').innerHTML = response['h']
      document.getElementById('LP').innerHTML = response['l']
    }
  }
  var param = new URLSearchParams(FD);
  param = param.toString();
  req.open('GET', '/route2?' + param, true);
  req.send(null);
  event.preventDefault();
};

function company() {
  mod = 1;
  document.getElementById('table1').style.display = 'block';
  document.getElementById('table2').style.display = 'none';
  document.getElementById('container').style.display = 'none';
  document.getElementById('block4').style.display = 'none';
  document.getElementById('navbar').style.display = 'block';
}

function stockInfo() {
  mod = 2;
  document.getElementById('table2').style.display = 'block';
  document.getElementById('table1').style.display = 'none';
  document.getElementById('container').style.display = 'none';
  document.getElementById('block4').style.display = 'none';
}

function charts() {
  mod = 3;
  document.getElementById('table1').style.display = 'none';
  document.getElementById('table2').style.display = 'none';
  document.getElementById('container').style.display = 'block';
  document.getElementById('block4').style.display = 'none';

  Highcharts.getJSON('/route3', function (data) {
    const d = new Date()
    dd = d.getMonth() + 1
    datetime = d.getFullYear() + "-0" + dd + "-" + d.getDate()
    var stockprice = [],
      volume = [],
      dataLength = data.length,

      i = 0;

    for (i; i < dataLength; i += 1) {
      stockprice.push([
        data[i][0],
        data[i][1],
      ]);

      volume.push([
        data[i][0],
        data[i][2]
      ]);
    }

    Highcharts.stockChart('container', {
      rangeSelector: {
        selected: 1
      },

      title: {
        text: global + ' Stock Price ' + datetime
      },
      subtitle: {
        text: '<a href="https://finnhub.io/." target="_blank">Source: Finnhub</a>'
      },

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
        title: {
          text: 'Volume'
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
        }, {
          type: 'month',
          count: 6,
          text: '6m',
        }]
      },

      //stock chart
      series: [{
        name: global + ' Stock Price',
        data: stockprice,
        type: 'area',
        threshold: null,
        tooltip: {
          valueDecimals: 2
        },
        fillColor: {
          linearGradient: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 1
          },
          stops: [
            [0, Highcharts.getOptions().colors[0]],
            [1, Highcharts.color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
          ]
        }
      }, {
        type: 'column',
        name: 'Volume',
        data: volume,
        yAxis: 1,
        color: 'grey'
      }]
    });
  });
}

function reset() {
  mod = 0;
  document.getElementById('table1').style.display = 'none';
  document.getElementById('table2').style.display = 'none';
  document.getElementById('container').style.display = 'none';
  document.getElementById('block4').style.display = 'none';
  document.getElementById('navbar').style.display = 'none';
  document.getElementById('error').style.display = 'none';
}

function elementClicking() {
  if (mod == 2) {
    document.getElementById('button2').click()
  } else if (mod == 3) {
    document.getElementById('button3').click()
  } 
  else {
    document.getElementById('button1').click()
  }
};