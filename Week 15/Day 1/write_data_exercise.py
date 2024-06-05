from flask import Flask, request
import sqlalchemy
from sqlalchemy.sql import text

app = Flask(__name__)

db = sqlalchemy.create_engine("mariadb+mariadbconnector://root:@127.0.0.1:3306/wcoding")

# **1:** `insert` an entry **without** using a prepared query
# The phone is a Samsung S8 Plus owned by Alexis, weighs 173g, the comment is “Good for watching videos”, and the price is $80 
@app.get("/sqlactivity")
def sqlactivity():
    with db.begin() as conn:
        res = conn.execute(text(
            """INSERT INTO phones VALUES (
                '',
                'Samsung S8 Plus', 
                'Samsung', 
                'Alexis', 
                80, 
                173, 
                'Good for watching videos'
            )"""))

# **2 :** `insert` an entry using a **prepared** query
# The phone is an Apple iPhone 12 owned by Alex, weighs 164g, the comment is “My company provided a phone i don’t need this one anymore, brand new”, and the price is $700
        res = conn.execute(text("INSERT INTO phones (model, brand, owner, price, weight, comment) VALUES (:model, :brand, :owner, :price, :weight, :comment)"), {
                "model": "iPhone 12",
                "brand": "Apple",
                "owner": "Alex",
                "price": 700,
                "weight": 164,
                "comment": "My company provided a phone. I don't need this one anymore, brand new"})

# **3 :** `update` **without** using a prepared query
# Reduce the price of Alex’s iPhone 12 to $690
        res = conn.execute(text("UPDATE phones SET price=690 WHERE model='iPhone12' AND owner='Alex'"))


# **4 :** `update` **using** a prepared query
# Change the comment on Alexis’s Phone by appending: “And listening to music!”
        res = conn.execute(text("UPDATE phones SET comment=:comment WHERE id=:id"),
                           {
                               "comment": "Good for watching videos and listening to music",
                               "id": 46
                           })        

# **5 :** `delete` an entry
# Delete Alexis’ Samsung S8 Plus from the table
        res = conn.execute(text("DELETE FROM phones WHERE id=46"))