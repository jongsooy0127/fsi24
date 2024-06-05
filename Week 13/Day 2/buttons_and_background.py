# Find a fancy button online that you would like to serve with Flask.
# For example: https://codepen.io/ash_creator/pen/oNyNbNO
# Create a flask server with a route that will provide the page that
# shows this fancy looking button in the middle of the page, using a
# separate CSS file. Then add a JS file, as well, that will change the
# background color of the page to a random color with each button click.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def buttons_and_background():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Separate CSS and JS</title>
    <link rel="stylesheet" href="static/pretty.css">
    </head>

    <body>
        <div class="container">
            <a href="#" class="button type--A">
                <div class="button__line"></div>
                <div class="button__line"></div>
                <span class="button__text">ENTRY</span>
                <div class="button__drow1"></div>
                <div class="button__drow2"></div>
            </a>
        </div>
            
        <script src="static/actions.js"></script>
    </body>
    </html>
"""