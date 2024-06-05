from flask import Flask, request
import sqlalchemy
from sqlalchemy.sql import text

app = Flask(__name__)

db = sqlalchemy.create_engine("mariadb+mariadbconnector://root:@localhost:3306/wcoding", echo=True)

#Question 1: Retrieve all the phones belonging to {owner}.
#EXAMPLE: http://127.0.0.1:5000/question1?owner=Alex
@app.get("/question1")
def question1():
    return_string = ""
    with db.begin() as conn:
        response = conn.execute(text("select MODEL, OWNER, PRICE, BRAND from PHONES where OWNER=:person"),
                                {"person": request.args.get("owner")})
        for owner in response:
            return_string += f"""
        <ul>
            <li> Model: {owner.MODEL} </br>
                Brand: {owner.BRAND} </br>
                Owned by: {owner.OWNER} </br>
                Price: ${owner.PRICE} dollars
            </li>
        </ul>
        """
        return return_string 
    
#Question 2: Retrieve all the phones with a weight of {weight}.
#EXAMPLE: http://127.0.0.1:5000/question2?weight=295
@app.get("/question2")
def question2():
    return_string = ""
    with db.begin() as conn:
        response = conn.execute(text("SELECT model, brand, owner, price FROM phones WHERE weight=:gram"),
                                {"gram": request.args.get("weight")})
        for phone in response:
            return_string += f"""
<ul>
    <li> Model: {phone.model} </br>
    Brand: {phone.brand} </br>
    Owned by: {phone.owner} </br>
    Price: ${phone.price} dollars
    </li>
</ul>
"""
        return return_string
    
#Question 3: Retrieve all the phones made by {brand}.
#EXAMPLE: http://127.0.0.1:5000/question3?brand=Nokia
@app.get("/question3")
def question3():
    return_string = ""
    with db.begin() as conn:
        response = conn.execute(text("SELECT model, brand, owner, price FROM phones WHERE brand=:company"),
                                {"company": request.args.get("brand")})
        for phone in response:
            return_string += f"""
<ul>
    <li> Model: {phone.model} </br>
    Brand: {phone.brand} </br>
    Owned by: {phone.owner} </br>
    Price: ${phone.price} dollars
    </li>
</ul>
"""
        return return_string
    
#Question 4: Retrieve the phones made by {brand1} and {brand2}.
#EXAMPLE: http://127.0.0.1:5000/question4?brand1=Apple&brand2=Nokia
@app.get("/question4")
def question4():
    return_string = ""
    with db.begin() as conn:
        response = conn.execute(text("SELECT model, brand, owner, price FROM phones WHERE brand=:company1 OR brand=:company2"),
                                {
                                    "company1": request.args.get("brand1"),
                                    "company2": request.args.get("brand2")
                                })
        for phone in response:
            return_string += f"""
<ul>
    <li> Model: {phone.model} </br>
    Brand: {phone.brand} </br>
    Owned by: {phone.owner} </br>
    Price: ${phone.price} dollars
    </li>
</ul>
"""
        return return_string

#Question 5: Retrieve the phones that cost {cost}.
#EXAMPLE: http://127.0.0.1:5000/question5?price=115
@app.get("/question5")
def question5():
    return_string = ""
    with db.begin() as conn:
        res = conn.execute(text("SELECT model, brand, owner, price FROM phones WHERE price=:cost"),
        {
            "cost": request.args.get("price")
        })
        for phone in res:
            return_string += f"""
<ul>
    <li> Model: {phone.model} </br>
    Brand: {phone.brand} </br>
    Owned by: {phone.owner} </br>
    Price: ${phone.price} dollars
    </li>
</ul>
"""
        return return_string
    
#Question 6: Get all the phones ordered by weight in ascending order.
#EXAMPLE: http://127.0.0.1:5000/question6
@app.get("/question6")
def question6():
    return_string = ""
    with db.begin() as conn:
        res = conn.execute(text("SELECT * FROM phones ORDER BY weight"))
        for phone in res:
            return_string += f"""
<ul>
    <li> Model: {phone.model} </br>
    Brand: {phone.brand} </br>
    Owned by: {phone.owner} </br>
    Price: ${phone.price} dollars
    </li>
</ul>
"""
        return return_string
    
#Question 7: Get the 5 first phones owned by {owner}.
#EXAMPLE: http://127.0.0.1:5000/question7?owner=Victoria
@app.get("/question7")
def question7():
    return_string = ""
    with db.begin() as conn:
        res = conn.execute(text("SELECT model, brand, owner, price FROM phones WHERE owner=:person LIMIT 5"), {
            "person": request.args.get("owner")
        })
        for phone in res:
            return_string += f"""
<ul>
    <li> Model: {phone.model} </br>
    Brand: {phone.brand} </br>
    Owned by: {phone.owner} </br>
    Price: ${phone.price} dollars
    </li>
</ul>
"""
        return return_string
    
#Question 8: Get {owner} phones with a price lower than {price} in order of descending price.
#EXAMPLE: http://127.0.0.1:5000/question8?owner=Nina&price=250
@app.get("/question8")
def question8():
    return_string = ""
    with db.begin() as conn:
        res = conn.execute(text("SELECT * FROM phones WHERE owner=:person AND price<=:cost ORDER BY price DESC"), {
            "person": request.args.get("owner"),
            "cost": request.args.get("price") 
        })
        for phone in res:
            return_string += f"""
<ul>
    <li> Model: {phone.model} </br>
    Brand: {phone.brand} </br>
    Owned by: {phone.owner} </br>
    Price: ${phone.price} dollars
    </li>
</ul>
"""
        return return_string
