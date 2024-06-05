# 1. Create a list of 3 fruits and store it in a variable called "fruits"
fruits = ["strawberry", "grapes", "watermelon"]

#    b. Check if "apples" is in your list of fruits (True or False)
print("APPLES IN LIST?:", "apples" in fruits)

#    c. Append 2 more fruits to your list of fruits
fruits.append("orange")
fruits.append("cherry")
print("UPDATED LIST:", fruits)

#    d. Update your fruits variable to contain the values of the original
#       fruits list, but in reverse order
#========================================BOTH WORKS!!==============================================
# fruits.reverse()
fruits = fruits[::-1]
print("REVERSED FRUITS:", fruits)

#    e. Print the very first in your list of fruits
print("FIRST FRUIT:", fruits[0])


#    f. Print the 3rd and 4th fruits as a sublist (shorter list)
print("3RD and 4TH fruit", fruits[2:4])

#    g. Add the string 'big ' in front of the last item in the list
#       If the lastfruit was "pineapple", update it to be "big pineapple"
fruits[(len(fruits)) - 1] = "big " + fruits[(len(fruits)) - 1]
print("LAST ITEM IN LIST:", fruits[len(fruits) - 1])

#    h. Pop off the last fruit in the list and store it in variable big_fruit
big_fruit = fruits.pop()
print("POPPED FRUIT:", big_fruit)

#    i. Print the current length of the fruits list
print("LENGTH OF LIST:", len(fruits))

#    j. Print the length of big_fruit
print("LENGTH OF STRING BIG_FRUIT:", len(big_fruit))


# 2. Create an empty dictionary and store it in the variable shopping_cart.
#     Then add the following keys:
#     - "items" key should correspond to an empty list
#     - "created_at" key should correspond to today's date as a string
#     - "total" key is the total value of the items in shopping_cart (0)
#     - "recent" key should correspond to True
from datetime import date
today = date.today()

shopping_cart = {
    "items": [],
    "created_at": today,
    "total": 0,
    "recent": True
}

#    b. Update the "total" in the shopping_cart by increasing it by 5000
shopping_cart["total"] += 5000
print("TOTAL: SHOPPING CART", shopping_cart.get("total"))

#    c. Update the "items" in the shopping_cart by appending to it big_fruit
shopping_cart["items"].append(big_fruit)

#    d. Check if "big apples" is in the "items" list in your shopping_cart
print("ITEM IN SHOPPING CART:",shopping_cart.get("items"))

# 3. Create a dictionary called favorites. It should have...
#    an "items" property that corresponds to ["water", "juice", "bread"]
#    a "total" property that corresponds to 15000
#    a "recent" property that corresponds to False
#    and a "created_at" property that is yesterday's date as a string
favorites = {
    "items": ["water", "juice", "bread"],
    "total": 15_000,
    "recent": False,
    "created_at": "May 6th 2024"
}


# 4. Create a dictionary called order. It should have...
#    an "items" property which is the combination of
#         "items" from shopping_cart and
#         "items" from favorites
#    a "total" property which is the sum of
#         "total" from shopping_cart and
#         "total" from favorites
#    a "created_at" property which corresponds to today's date as a string
#    a "recent" property which corresponds to applying logical or to
#         "recent" of shopping_cart and
#         "recent" of favorites
order = {
    "items": shopping_cart["items"] + favorites["items"],
    "total": shopping_cart["total"] + favorites["total"],
    "created_at": shopping_cart["created_at"],
    "recent": shopping_cart["recent"] or favorites["recent"]
}

print("ORDER DICTIONARY:", order)