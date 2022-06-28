<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Stock Predictor</title>
    <meta name="description" content="This is my stocks 101 predictor page" />
    <link rel="shortcut icon" href="favicon.ico" />
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
    <script src="js/nav.js" defer></script>
    <?php
    echo shell_exec("python stockPredictor.py");
    ?>
  </head>
  <body>
    <header>
      <picture><img src="images/stockLogo.jpg" alt="Logo" /></picture>
      <section class="heading">
        <h1>Stocks 101</h1>
      </section>
    </header>
    <nav>
      <ul class="navigation responsive">
        <li><a class="menu" href="#">Menu</a></li>
        <li><a href="stockInformation.php">Stock Information</a></li>
        <li><a href="stockPredictor.php">Stock Predictor</a></li>
      </ul>
    </nav>
    <main>
          <p class="start">Stock Predictor</p>
          <div class="input-place">
            <p>Input stock ticker:</p>
            <div class="form">
              <input id="stockTicker" type="text" step="any" persisted_props="value" persisted_type="local" value>
            </div>
          </div>
          <div class="buttons">
            <input type="text" placeholder="number of days" id="numberDays" step="any" persisted_props="value" persisted_type="local" value>
            <button id="predictor" class="prediction-btn">predictor</button>
          </div>
        </div>
        <div class="content">
          <div class="header">
            <img id="logo">
            <p id="ticker"></p>
          </div>
        <div id="description" class="ticker"></div>
        <div id="graphs-content"></div>
        <div id="main-content"></div>
        <div id="prediction-content"></div> 
    </main>
  </body>
  <footer></footer>
</html>
