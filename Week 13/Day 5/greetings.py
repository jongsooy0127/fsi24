from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  name = request.args.get('firstname', 'Alvin')
  return render_template("personal_greeting.html", user=name)