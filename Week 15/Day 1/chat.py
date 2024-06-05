from flask import Flask, request
import sqlalchemy
from sqlalchemy.sql import text
import datetime

app = Flask(__name__)
db = sqlalchemy.create_engine("mariadb+mariadbconnector://root:@127.0.0.1:3306/wcoding", echo=True)

@app.post("/sendchat")
def sendchat():
    username = request.json.get("username")
    message = request.json.get("message")
    user_msg = {"username": username, "message": message}
    print("JSON REQUEST: ", request.json)
    with db.begin() as conn:
        res = conn.execute(text("INSERT INTO chat (username, message, date_created) VALUES (:username, :message, :date_created)"), {
            # "username": user_msg["username"],
            # "message": user_msg["message"],
            "username": username,
            "message": message,
            "date_created": datetime.datetime.now()
        })
        return user_msg

get_more = 11

@app.get("/getchat")
def getchat():
    global get_more
    with db.begin() as conn:
        list_of_msgs = []
        res = conn.execute(text("SELECT * FROM chat"))
        for i in range(get_more):
            for msg in res:
                list_of_msgs.append({"username": msg.username, "message": msg.message})
        get_more += 10
        return list_of_msgs[:i]
    
@app.post("/randomtest")
def randomtest():
    # id = request.json.get("id")
    # pw = request.json.get("pw")
    id = request.form.get("id")
    pw = request.form.get("pw")
    return_value = [id, pw]
    print(return_value)
    return return_value

    
