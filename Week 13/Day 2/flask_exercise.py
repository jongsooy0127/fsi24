# Create a flask server that will act as an API and have these endpoints:
# - /numvowels
#    This endpoint accepts the GET method and expects to have an argument
#    called 'word'. It will return the number of vowels in the word.
# - /greetings
#    This endpoint accepts the POST method and expects to have an argument
#    called 'name' sent in url-encoded form data. It will return a string
#    in the format: "Hello <name>, your name backwards is <name backwards>!"
# - /dateinfo
#    This endpoint accepts GET or POST and expects to have the arguments
#    sent in via JSON, with a property called 'date' in the format
#    'yyyy-mm-dd'. This endpoint will return a JSON string with the date
#    parsed out into properties for year, month name (not number), day of
#    month, day of week, and day of year.
# - /user/<user_id>
#    This endpoint accepts the GET method and expects to have an argument
#    called 'snack'. If the user_id is '123-456-7890', return a JSON
#    string with a 'message' property and value of "<user_id> loves to eat
#    <snack>s", otherwise the message will be "User not found."
#
# Also, create a web page with HTML forms with appropriate inputs for
# each of the above API endpoints. Use JS to handle form submissions,
# as necessary. Remember to also use the appropriate request methods
# and data formats to match what is expected from the API. Display results
# of each API call below the respective forms.

from flask import Flask, request
from datetime import datetime
import calendar

app = Flask(__name__)

body_css = """
<style>
    body {
        max-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-directions: column;
        gap: 1rem;
    }
</style>
"""

@app.get("/numvowels")
def numvowels():
    reverse_word = request.args.get("word")
    vowel_list = [letter for letter in reverse_word if letter in "aeiou"]
    print(vowel_list)
    return body_css + f"<h1>Number of vowels in {reverse_word}: {len(vowel_list)}<h1>"

@app.post("/greetings")
def greetings():
    name = request.form.get("name")
    return body_css + f"<p>Hello {name}, your name backwards is {name[::-1].title()}"

@app.route("/date", methods=["POST","GET"])
def date():
    if request.method == "GET":
        input_date = request.args.get("date")
    else:
        input_date = request.form.get("date")
    month = calendar.month_name[int(input_date[-5:-3])]
    date = calendar.day_name[datetime.fromisoformat(input_date).weekday()]
    year = datetime.fromisoformat(input_date).year
    day = datetime.fromisoformat(input_date).day

    return body_css + f"<h2>Month: {month}</h2><h2>Date: {date}</h2><h2>Day: {day}</h2><h2>Year: {year}</h2>"

@app.post("/snack")
def snack():
    user_id = request.form.get("user_id")
    snack = request.form.get("snack")
    if user_id == "123-456-7890":
        return body_css + f"{user_id} loves to eat {snack}s"
    else: return f"{user_id} does not exist"

@app.route("/webpage")
def get_webpage():
    return body_css + """
    <style>
        form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            max-height: 100vh;
            max-width: 100vw;
        }
    </style>

    <fieldset>
        <legend>GET Request</legend>
        <form method="get" action="/numvowels">
            <div>
                <label>
                    Enter a word:
                    <input name="word">
                </label>
            </div>
            <button>Send</button>
        </form>
    </fieldset>

    <fieldset>
        <legend>POST Request</legend>
        <form method="post" action="/greetings">
            <div>
                <label>
                    Enter your name:
                    <input name="name">
                </label>
            </div>
            <button>Send</button>
        </form>
    </fieldset>

    <fieldset>
        <legend>POST Request</legend>
        <form method="post" action="/date">
            <div>
                <label>
                    Enter a date:
                    <input name="date" placeholder="yyyy-mm-dd">
                </label>
            </div>
            <button>Send</button>
        </form>
    </fieldset>

    <fieldset>
        <legend>POST/JSON Request</legend>
        <form id="jsonForm" method = "GET" action = "/snack">
            <div>
                <label>
                    Enter your user ID:
                    <input name="user_id">
                </label>
            </div>
            <div>
                <label>
                    Enter a snack:
                    <input name="snack">
                </label>
            </div>
            <button>Send</button>
        </form>
        <div id="stuff" style="display: flex; justify-content: center;"></div>
    </fieldset>

    <script>
        document.querySelector("#jsonForm").addEventListener("submit", evt => {
            // evt.preventDefault();

            // Turn into FormData so we can get data out of the form easily.
            // You could have also put an id on each input and used
            // document.querySelector or document.getElementById to get the
            // input values. (eg. document.getElementById('colorInput').value)
            const fd = new FormData(evt.target);
            const user_id = fd.get("user_id");
            const snack = fd.get("snack");

            // Fetch with a POST request.
            // NOTE: JSON requests require the Content-type header to be set
            // appropriately as application/json
            const fetchOptions = {
                method: "post",
                headers: {
                    "Content-type": "application/json",
                },
                // body: JSON.stringify({ color: color, size: size })
                body: JSON.stringify({ user_id, snack })  // Same as above.
            }

            fetch("/snack", fetchOptions)
                .then(res => res.text())
                .then(res => {
                    // The '/squareJson' endpoint returns HTML. This is not
                    // typical, but to make the most of it, we're going
                    // to replace a portion of the UI with the new HTML.
                    document.querySelector('#stuff').innerHTML = res;
                });
        })
    </script>
"""