# Ask the user for the name of a cocktail. Then use the Cocktails DB
# (https://www.thecocktaildb.com/) to get data about the drink. List
# all the ingredients on separate lines sorted alphabetically. Then,
# below the ingredients, show the directions on how to make the
# cocktail. (English) If the cocktail name does not exist then let the
# user know. Regardless, ask again for another cocktail name. If the
# user types 'q', then stop asking and end the program.

import requests

def find_cocktail(api_url):
    in_progress = True

    while in_progress:

        item_search = input("Provide the name of the item you want to search: ")
        
        if item_search == "q":
            print("User has quit")
            in_progress = False
        try:
            if item_search != "q":  
                r = requests.get(api_url+item_search)
                r_json = r.json()
            
                
                cocktail = r_json["drinks"][0]

                list_of_ingred = []

                for i in range(1,16):
                    # if cocktail[f"strIngredient{i}"] != None and cocktail[f"strIngredient{i}"] != "":
                        list_of_ingred.append(cocktail[f"strIngredient{i}"])

                list_of_ingred = [item for item in list_of_ingred if item != "" and item != None]
                list_of_ingred.sort()
                
                cocktail_instructions = cocktail["strInstructions"]

                for i,ingred in enumerate(list_of_ingred):
                     print("Ingredient", i+1, ingred)
                print(cocktail_instructions)
        except Exception as e:
            print("The cocktail does not exist. Please try again")


find_cocktail("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=")
