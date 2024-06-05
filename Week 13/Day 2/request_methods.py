from flask import Flask, request

app = Flask(__name__)

general_css = """
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            flex-direction: column;
            gap: 2rem;
        }
    </style>
"""

square_css = """
    <style>
        div.square {
            width: 10rem;
            height: 10rem;
            border-radius: 10px;
            background-color: cornflowerblue;
        }
    </style>
"""

def drawSquare(color, size):
    return f"<div class='square' style='background-color:{color}; width:{size}rem; height:{size}rem;'></div>"

@app.get("/squareGet")
def one():
    new_color = request.args.get('color')
    square_size = request.args.get('size')

    return general_css + square_css + drawSquare(new_color, square_size)

@app.post("/squarePost")
def two():
    new_color = request.form.get('color')
    square_size = request.form.get('size')

    return general_css + square_css + drawSquare(new_color, square_size)

@app.route("/squareBoth", methods=['GET', 'POST'])
def three():
    if request.method == 'GET':
        new_color = request.args.get('color')
        square_size = request.args.get('size')
    else:
        new_color = request.form.get('color')
        square_size = request.form.get('size')

    return general_css + square_css + drawSquare(new_color, square_size)

@app.post("/squareJson")
def four():
    new_color = request.json.get('color')
    square_size = request.json.get('size')

    return general_css + square_css + drawSquare(new_color, square_size)

@app.get("/getSquareColor")
def getSquareColor():
    return general_css + """
    <style>
        form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
    </style>

    <fieldset>
        <legend>GET Request</legend>
        <form method="get" action="/squareGet">
            <div>
                <label>
                    Enter a valid CSS color:
                    <input name="color">
                </label>
            </div>
            <div>
                <label>
                    Enter a size:
                    <input type="number" name="size">
                </label>
            </div>
            <button>Send</button>
        </form>
    </fieldset>

    <fieldset>
        <legend>POST Request</legend>
        <form method="post" action="/squarePost">
            <div>
                <label>
                    Enter a valid CSS color:
                    <input name="color">
                </label>
            </div>
            <div>
                <label>
                    Enter a size:
                    <input type="number" name="size">
                </label>
            </div>
            <button>Send</button>
        </form>
    </fieldset>

    <fieldset>
        <legend>POST/JSON Request</legend>
        <form id="jsonForm">
            <div>
                <label>
                    Enter a valid CSS color:
                    <input name="color">
                </label>
            </div>
            <div>
                <label>
                    Enter a size:
                    <input type="number" name="size">
                </label>
            </div>
            <button>Send</button>
        </form>
        <div id="stuff" style="display: flex; justify-content: center;"></div>
    </fieldset>
"""