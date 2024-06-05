# - /user/<user_id>
#    This endpoint accepts the GET method and expects to have an argument
#    called 'snack'. If the user_id is '123-456-7890', return a JSON
#    string with a 'message' property and value of "<user_id> loves to eat
#    <snack>s", otherwise the message will be "User not found."

from flask import Flask, request
import json

app = Flask(__name__)

@app.get("/user/<user_id>")
def user(user_id):
    snack = request.args.get('snack', "")
    if user_id == "123-456-7890":
        return {"message": f"{user_id} loves to eat {snack}s"}
    else: 
        return {"message": "User not found"}