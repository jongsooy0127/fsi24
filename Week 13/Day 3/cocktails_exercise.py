"""
    Create an API server for drink data. Use the 'cocktails.json' file as the source of data for your server. Your server should have the following endpoints and behaviors:

    /search
        This API endpoint accepts a query parameter 's', that allows the user to search all drinks for drink names that match the word(s) provided in 's'. Multiple search terms can be provided as a comma separated list of terms and the search should match on names including any of those terms. This returns an array of matching drink names and respective ids.
    /ingredients
        This API endpoint accepts a query parameter 's', that allows the user to search all drinks for drink ingredients that match the word(s) provided in 's'. Multiple search terms can be provided as a comma separated list of terms and the search should match on ingredients including any of those terms. This returns an array of matching drink names and respective ids.
    /details/<drink_id>
        This API endpoint uses the path parameter to find a specific drink and returns all the details of that drink.

    Then create a UI that uses the API server above to give the user the ability to search by drink name or particular ingredients. (Two different forms, please.) Once the user receives a list of matches from either one of the searches, clicking on one of the matches will provide all the details of that drink on another page in an attractive way.
"""
import json
from flask import Flask, request

app = Flask(__name__)

all_drinks = []
with open("cocktails.json", encoding="utf-8") as drink_file:
    all_drinks = json.load(drink_file)
    all_drinks = list(filter(lambda drink: drink is not None, all_drinks))
    for i in range (1,16):
        for drink in all_drinks:
            if drink[f"strIngredient{i}"] == None:
                drink[f"strIngredient{i}"] = ""
            if drink[f"strMeasure{i}"] == None:
                drink[f"strMeasure{i}"] = ""


@app.get("/search")
def search():
    search_terms = request.args.get("s")
    search_list = search_terms.split(",")
    all_matches = []
    for term in search_list:
        # all_matches = [(drink["idDrink"],drink["strDrink"])for drink in all_drinks if "strDrink" in drink and term.lower() in drink ["strDrink"].lower()]
        for drink in all_drinks:
            if "strDrink" in drink and term.lower() in drink["strDrink"].lower():
                new_matches = {"id": drink["idDrink"], "name": drink["strDrink"]}
                all_matches.append(new_matches)    
    return all_matches

@app.get("/ingredients")
def ingredients():
    search_terms = request.args.get("s")
    search_list = search_terms.split(",")
    all_matches = []
    for term in search_list:
        for drink in all_drinks:
            for i in range(1,16):
                if f"strIngredient{i}" in drink and term.lower() in drink[f"strIngredient{i}"].lower() and drink[f"strIngredient{i}"] != None:
                    new_matches = {"id": drink["idDrink"], "name": drink["strDrink"]}
                    all_matches.append(new_matches)
    return all_matches

@app.get("/details/<drink_id>")
def details(drink_id):
    concat_ingred = ""
    concat_measure = ""
    for drink in all_drinks:
        if drink["idDrink"] == drink_id:
            for i in range(1,16):
                if drink[f"strIngredient{i}"] != "":
                    concat_ingred += f"Ingredient {i}: {drink[f"strIngredient{i}"]}<br>"
                if drink[f"strMeasure{i}"] != "":
                    concat_measure += f"Measure {i}: {drink[f"strMeasure{i}"]}<br>"
            concat_string = f"""
<img src="{drink["strDrinkThumb"]}" style="height: 60%;"> <br>
Cocktail ID: {drink["idDrink"]} <br>    
Cocktail Name: {drink["strDrink"]} <br>
{concat_ingred} <br>
{concat_measure} <br>
Instructions: {drink["strInstructions"]}
"""
            return concat_string