from flask import Flask, request
from sqlalchemy.sql import text
import sqlalchemy

db = sqlalchemy.create_engine("mariadb+mariadbconnector://root:@127.0.0.1:3306/wcoding")

#Question 1: Get all the messages sent today.
print("Question 1")
with db.begin() as conn:
    res = conn.execute(text("SELECT * FROM chat WHERE date_created >= '2024-06-04 00:00:00'"))
    for chat in res:
        print(chat.username + "--" + chat.message + "--" + str(chat.date_created))

#Question 2: Get messages from a specific time today.
print("Question 2")
with db.begin() as conn:
    res = conn.execute(text("SELECT * FROM chat WHERE date_created = '2024-06-04 14:40:19'"))
    for chat in res:
        print(chat.username + "--" + chat.message + "--" + str(chat.date_created))

#Question 3: Get messages from a date that has messages, that were sent between two specific hours.
print("Question 3")
with db.begin() as conn:
    res = conn.execute(text("SELECT * FROM chat WHERE date_created BETWEEN '2024-06-03 12:00:00' AND '2024-06-03 14:55:00'"))
    for chat in res:
        print(chat.username + "--" + chat.message + "--" + str(chat.date_created))

#Question 4: Put some messages into the table that are dated as 2 days ago.
print("Question 4")
with db.begin() as conn:
    res = conn.execute(text("INSERT INTO chat (username, message, date_created) VALUES ('Godzilla', 'ROAR!', '2024-06-02 00:00:00')"))
    print("INSERTED: GODZILLA, ROAR, 2024-06-02 00:00:00")

#Question 5: Get the messages from 2 days ago.
print("Question 5")
with db.begin() as conn:
    res = conn.execute(text("SELECT username, message, date_created, DATE_FORMAT(date_created, '%Y-%m-%d') AS created_at FROM chat HAVING created_at = '2024-06-02'"))
    for chat in res:
        print(chat.username + "--" + chat.message + "--" + str(chat.date_created))

#Question Get the messages from 2 days ago with a specific time.
print("Question 6")
with db.begin() as conn:
    res = conn.execute(text("SELECT * FROM chat WHERE date_created = '2024-06-02 15:04:54'"))
    for chat in res:
        print(chat.username + "--" + chat.message + "--" + str(chat.date_created))

#Question 7: Get the date as “dd/mm/yyyy” (common European format) and get the first 20 messages — do this without the DATE_FORMAT function
print("Question 7")
with db.begin() as conn:
    res = conn.execute(text("SELECT username, message, DAY(date_created) AS day, MONTH(date_created) AS month, YEAR(date_created) AS year FROM chat ORDER BY day LIMIT 20"))
    for chat in res:
        print(chat.username + "--" + chat.message + "--" + str(chat.day) + "/" + str(chat.month) + "/" + str(chat.year))

#Question 8: 8:  Get the date as “mm/dd/yyyy” (common US format) and display the first 15 messages — do this with the DATE_FORMAT function
print("Question 8")
with db.begin() as conn:
    res = conn.execute(text("SELECT username, message, DATE_FORMAT(date_created, '%m/%d/%Y') AS us_date FROM chat ORDER BY us_date LIMIT 15"))
    for chat in res:
        print(chat.username + "--" + chat.message + "--" + str(chat.us_date))

#Question 9: Add an expiration date field to your table and update every row so that it is 2 months after the created_at value for each row — update all the rows in the database with a single query
print("Question 9")
with db.begin() as conn:
    res = conn.execute(text("ALTER TABLE chat ADD expiration_date DATETIME")) 
    res = conn.execute(text("UPDATE chat SET expiration_date = DATE_ADD(date_created, INTERVAL 2 MONTH)"))
    
