<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Stock Information</title>
    <meta name="description" content="This is my stocks 101 home page" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Noto+Serif&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="css/normalize.css" />
    <link rel="stylesheet" href="css/small.css" />
    <link rel="stylesheet" href="css/medium.css" />
    <link rel="stylesheet" href="css/large.css" />
    <link href="images/favicon.ico" rel="shortcut icon" type="image/jpg" />
    <script src="js/nav.js" defer></script>
    <script src="js/stockInfomation.js" defer></script>
  </head>
  <body>
    <header>
      <picture><img src="images/stockLogo.jpg" alt="Logo" /></picture>
      <section class="heading">
        <h1>Stocks 101</h1>
      </section>
    </header>
    <nav id="nav">
    <div class="innertube">
      <h1>Navigation</h1>
      <ul>
        <li><a data-page="stockInformation.php">Stock Information</a></li>
        <li><a data-page="stockPredictor.php">Stock Predictor</a></li>
      </ul>
    </div>
  </nav>
    <main>
    <div class="innertube">
      <div id="page"></div>
    </div>
      <div class="back">
        <h1 class="t1">Stock Search</h1>
        <form action="/test" method="get" id="result" name="myform">
          <div class="search-wrapper">
            <input
              type="image"
              alt="search"
              class="circle"
              onclick="getresult(event);abc();"
              src="images/search-icon.jpg"
            />
            <input
              type="text"
              id="input"
              name="CPN"
              class="search"
              placeholder="Enter Stock Ticker Symbol"
              oninvalid="this.setCustomValidity('Please fill out this field')"
              onput="this.setCustomValidity('')"
              required
            />
            <div class="line"></div>
            <input type="reset" value="Reset" id="rrr" style="display: none" />
            <img
              onclick="noresult(); document.getElementById('rrr').click()"
              src="images/x-ixon.jpg"
              class="delete"
            />
          </div>
        </form>
      </div>

      <div class="choices" id="choices">
        <button class="button b1" id="b1" onclick="company();getresult(event);">
          Company
        </button>
        <button
          class="button b2"
          id="b2"
          onclick="stocksummary();get_result2(event);"
        >
          Stock Summary
        </button>
        <button class="button b3" id="b3" onclick="charts()">Charts</button>
      </div>

      <table class="table1" id="table1" style="display: none">
        <tr>
          <td id="logo" colspan="2"></td>
        </tr>
        <tr>
          <th>Company Name</th>
          <td id="company"></td>
        </tr>
        <tr>
          <th>Stock Ticker Symbol</th>
          <td id="ticker"></td>
        </tr>
        <tr>
          <th>Stock Exchange Code</th>
          <td id="code"></td>
        </tr>
        <tr>
          <th>Company IPO Date</th>
          <td id="date"></td>
        </tr>
        <tr>
          <th>Category</th>
          <td id="category"></td>
        </tr>
      </table>

      <div class="t2" id="t2" style="display: none">
        <table class="table2" id="table2">
          <tr>
            <th>Stock Ticker Symbol</th>
            <td id="STS"></td>
          </tr>
          <tr>
            <th>Trading Day</th>
            <td id="TD"></td>
          </tr>
          <tr>
            <th>Previous Closing Price</th>
            <td id="PCP"></td>
          </tr>
          <tr>
            <th>Opening Price</th>
            <td id="OP"></td>
          </tr>
          <tr>
            <th>High Price</th>
            <td id="HP"></td>
          </tr>
          <tr>
            <th>Low Price</th>
            <td id="LP"></td>
          </tr>
        </table>
      </div>

      <script src="https://code.highcharts.com/stock/highstock.js"></script>
      <script src="https://code.highcharts.com/stock/modules/data.js"></script>
      <script src="https://code.highcharts.com/stock/modules/exporting.js"></script>
      <script src="https://code.highcharts.com/stock/modules/export-data.js"></script>
      <div class="container" id="container" style="display: none"></div>

      <div id="block4">
        <div id="0"></div>
        <div id="1"></div>
        <div id="2"></div>
        <div id="3"></div>
        <div id="4"></div>
      </div>

      <div id="error" class="error" style="display: none">
        Error : No record has been found, please enter a valid symbol
      </div>
    </main>
  </body>
  <footer></footer>
</html>
