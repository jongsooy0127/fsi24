from flask import Flask, request
import sqlalchemy
from sqlalchemy.sql import text

app = Flask(__name__)

db = sqlalchemy.create_engine("mariadb+mariadbconnector://root:@127.0.0.1:3306/wcoding")

@app.get("/question1")
def question1():
    return_str = ""
    with db.begin() as conn:
        res = conn.execute(text("SELECT UPPER(brand) AS brand_up, LOWER(model) AS model_low FROM phones"))
        for phone in res:
            return_str += f"""
<tr>
    <td>{phone.brand_up}</td>
    <td>{phone.model_low}</td>
</tr>
"""
        return f"""
<table>
    <tr>
        <td>Brand</td>
        <td>Model</td>
    </tr>
""" + return_str + "</table>"
    
@app.get("/question2")
def question2():
    return_str = ""
    with db.begin() as conn:
        res = conn.execute(text("SELECT owner, model, brand, price FROM phones"))
        for phone in res:
            return_str += f"""
<tr>
    <td>{phone.owner} ---- {phone.model}({phone.brand}){phone.price}$
</tr>
"""
        return f"""
<table>
    <tr>
        <td>Phone List</td>
    </tr> 
""" + return_str + "</table>"
    
@app.get("/question3")
def question3():
    return_str = ""
    with db.begin() as conn:
        res = conn.execute(text("SELECT model, LENGTH(comment) AS comment_len FROM phones"))
        for phone in res:
            return_str += f"""
<tr>
    <td>{phone.model}</td>
    <td>{phone.comment_len}</td>
</tr>
"""
        return f"""
<table>
    <tr>
        <td>Model</td>
        <td>Length Comment</td>
    </tr>
""" + return_str + "</table>"
    
@app.get("/question4")
def question4():
    with db.begin() as conn:
        res = conn.execute(text("SELECT ROUND(AVG(weight),4) AS avg_weight FROM phones WHERE owner='Brad'"))
        for phone in res:
            return_str = f"<tr><td>{phone.avg_weight}</td></tr>"
        return f"""
<table>
    <tr>
        <td>Average Phone's Weight</td>
    </tr>
""" + return_str
    
@app.get("/question5")
def question5():
    return_str = ""
    with db.begin() as conn:
        res = conn.execute(text("SELECT SUM(price) AS phone_sum, owner FROM phones WHERE owner='Brad' OR owner='Roland' GROUP BY owner"))
        for phone in res:
            return_str += f"<tr><td>{phone.owner}</td><td>{phone.phone_sum}</td></tr>"
        return f"""
<table>
    <tr>
        <td>Owner</td>
        <td>Total Price</td>
    </tr>
""" + return_str     + "</table>"
    
@app.get("/question6")
def question6():
    with db.begin() as conn:
        res = conn.execute(text("SELECT MAX(price) AS max_price FROM phones WHERE owner='Richard'"))
        for phone in res:
            return_str = f"<tr><td>{phone.max_price}</td></tr>"
        return f"""
<table>
    <tr>
        <td>Price</td>
    </tr>
""" + return_str + "</table>"
    
@app.get("/question7")
def question7():
    with db.begin() as conn:
        res = conn.execute(text("SELECT MIN(price) AS min_price FROM phones WHERE owner='Frank'"))
        for phone in res:
            return_str = f"<tr><td>{phone.min_price}</td></tr>"
        return f"""
<table>
    <tr>
        <td>Price</td>
    </tr>
""" + return_str + "</table>"
    
@app.get("/question8")
def question8():
    return_str = ""
    with db.begin() as conn:
        res = conn.execute(text("SELECT COUNT(owner) AS count, owner FROM phones WHERE owner='Brad' OR owner='Stacy' GROUP BY owner"))
        for phone in res:
            return_str += f"""
<tr>
    <td>{phone.owner}</td>
    <td>{phone.count}</td>
</tr>
"""
        return f"""
<table>
    <tr>
        <td>Owner</td>
        <td>Total amount</td>
    </tr>
""" + return_str + "</table>"
    
@app.get("/question9")
def question9():
    return_str = ""
    with db.begin() as conn:
        res = conn.execute(text("SELECT COUNT(model) AS count, owner FROM phones GROUP BY owner"))
        for phone in res:
            return_str += f"""
<tr>
    <td>{phone.owner}</td>
    <td>{phone.count}</td>
</tr>
"""
        return f"""
<table>
    <tr>
        <td>Owner</td>
        <td>Total amount</td>
    </tr>
""" + return_str + "</table>"
    
@app.get("/question10")
def question10():
    return_str = ""
    with db.begin() as conn:
        res = conn.execute(text("SELECT brand, ROUND(AVG(price),0) AS avg, COUNT(model) AS count FROM phones GROUP BY brand HAVING avg < 125"))
        for phone in res:
            return_str += f"""
<tr>
    <td>{phone.brand}</td>
    <td>{phone.avg}</td>
    <td>{phone.count}</td>
</tr>
"""
        return f"""
<table>
    <tr>
        <td>Brand</td>
        <td>Average Price</td>
        <td>Phone Amount</td>
""" + return_str + "</table>"
    
@app.get("/question11")
def question11():
    return_str = ""
    with db.begin() as conn:
        res = conn.execute(text("SELECT COUNT(model) as count, brand FROM phones WHERE weight > 170 GROUP BY brand HAVING count > 3"))
        for phone in res:
            return_str += f"""
<tr>
    <td>{phone.brand}</td>
    <td>{phone.count}</td>
</tr>
"""
        return f"""
<table>
    <tr>
        <td>Brand</td>
        <td>Phone Amount</td>
    </tr>
""" + return_str + "</table>"