"""
    Using the 'allMostWanted.json' file of FBI's most wanted, create an API server that will provide the following endpoints:

    /highbounty
        Find the 20 highest bounties from all the records and return for each record at least the bounty amount, the name of the person and an id.
    
    /details/<person_id>
        Provide a webpage of the details and picture(s) of the period for the id provided in a user-friendly way.
"""
from flask import Flask, request
import json

app = Flask(__name__)

all_criminal = []
with open ("allMostWanted.json",encoding="utf-8") as f:
    all_criminal = json.load(f)

@app.get("/highbounty")
def highbounty():
    new_obj_of_crim = []
    for criminal in all_criminal:
        reward_list = ["0"]
        if criminal["reward_text"] != None or criminal["reward_text"] == "":
            writing_num = False
            for char in criminal["reward_text"]:
                if str(char) in "1234567890,":
                    writing_num = True
                    if char != ",":
                        reward_list.append(char)
                elif writing_num:
                    break
        # criminal["reward_text"] = {int("".join(reward_list))}
        new_obj_of_crim.append({"reward_text": int("".join(reward_list)), "title": criminal["title"], "images": criminal["images"]})
    top_twenty = sorted(new_obj_of_crim, key=lambda criminal: criminal["reward_text"], reverse=True)
    return top_twenty[:20]

@app.get("/detail/<person_id>")
def detail(person_id):
    for criminal in all_criminal:
        if criminal["uid"] == person_id:
            return """

"""