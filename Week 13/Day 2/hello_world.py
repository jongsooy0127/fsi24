from flask import Flask

app = Flask(__name__)

@app.route("/")
def the_name_of_this_func_does_not_matter():
    return "<p>Hello World!</p>"

@app.route("/ping")
def ping():
	return "pong"

@app.route("/party")
def partyparty():
  return """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Party Party!</title>
  <style>
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }
    img {
      height: 400px;
    }
  </style>
</head>

<body>
  <img src="https://gifdb.com/images/high/excited-party-mode-baby-y6ohsg4asvx4171u.webp" alt="Baby NHL Penguins fan is very excited">
</body>
</html>
"""

@app.route("/excited")
def party_baby():
	return "<img src='static/excited-party-mode-baby.webp' alt='Baby NHL Penguins fan is very excited'>"

@app.route("/otherfiles")
def otherfiles():
  return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Separate CSS and JS</title>
  <link rel="stylesheet" href="static/pretty.css">
</head>

<body>
  <div class="square"></div>
  <script src="static/actions.js"></script>
</body>
</html>
"""