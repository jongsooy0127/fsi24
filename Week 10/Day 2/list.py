# 1. Create an empty new list called all_colors.
all_colors = []

# 2. Add red, orange, yellow, green, blue, and purple to
#     the all_colors list one item at a time.
all_colors.append("red")
all_colors.append("orange")
all_colors.append("yellow")
all_colors.append("green")
all_colors.append("blue")
all_colors.append("purple")

# 3. Unfortunately, purple was not supposed to be in the list. Can you
#     edit the all_colors list to replace purple with 2 other items,
#     indigo and violet, as the last items in the list?
all_colors.pop()
all_colors.append("indigo")
all_colors.append("violet")
print(all_colors)

# 4. Ask the user for more input: provide 3 more colors, separated by
#     commas. Parse the input appropriately and insert each of the colors
#     into the all_colors list at the end of the list.
user_input = input("Provide 3 colors, separated by commas")

# 5. Add a check to make sure the user submitted at least 3 items.
#     If not, print out an appropriate error message to the user and have
#     the Python script run to the end without doing anything more.
# if user_input.count(",") == 2:
#     user_input = user_input.split(",")
#     user_input[0] = user_input[0].strip()
#     user_input[1] = user_input[1].strip()
#     user_input[2] = user_input[2].strip()
#     all_colors.append(user_input[0])
#     all_colors.append(user_input[1])
#     all_colors.append(user_input[2])
#     print(all_colors)
# else:
#     print("Error! You have inputted more than or less than 3 colors. Try again later!")
#     exit()


# 6. Add a check on inserting the user submitted colors into the list.
#     Only add a user submitted color, if it doesn't already exist
#     in the list.
# if user_input.count(",") == 2:
#     user_input = user_input.split(",")
#     user_input[0] = user_input[0].strip()
#     user_input[1] = user_input[1].strip()
#     user_input[2] = user_input[2].strip()
#     if not user_input[0] in all_colors: all_colors.append(user_input[0])
#     if not user_input[1] in all_colors: all_colors.append(user_input[1])
#     if not user_input[2] in all_colors: all_colors.append(user_input[2])
#     print(all_colors)
# else:
#     print("Error! You have inputted more than or less than 3 colors. Try again later!")

# 7. Again, ask the user to provide 3 colors with one prompt. Do the
#     same input validation (make sure there is at least 3 colors and
#     skip adding any colors that already exist in the all_colors list)
#     but this time add these colors to the front of the list.
if user_input.count(",") == 2:
    user_input = user_input.split(",")
    user_input[0] = user_input[0].strip()
    user_input[1] = user_input[1].strip()
    user_input[2] = user_input[2].strip()
    if not user_input[0] in all_colors: all_colors.append(user_input[0])
    else: all_colors.insert(0, user_input[0])
    if not user_input[1] in all_colors: all_colors.append(user_input[1])
    else: all_colors.insert(0, user_input[1])
    if not user_input[2] in all_colors: all_colors.append(user_input[2])
    else: all_colors.insert(0, user_input[2])
    print("NEW COLOR TO BACK, EXISTING COLOR TO THE FRONT", all_colors)
else:
    print("Error! You have inputted more than or less than 3 colors. Try again later!")
    exit()

# 8. Swap the middle color and the color at the end of the list.
#     If there are an even number of items in the list, bias the
#     middle towards the front of the list. (ie. the middle of four
#     elements would be the second element)
all_col_length = len(all_colors)
if all_col_length % 2 == 0:
    all_colors[int(all_col_length/2)], all_colors[all_col_length-1] = all_colors[all_col_length-1], all_colors[int(all_col_length/2)]
print("SWAP", all_colors)

# 9. Move the third to last element to the front.
all_colors.insert(0, all_colors[-3])
all_colors.pop(-3)
print("MOVE THIRD ITEM TO THE FRONT", all_colors)

# 10. Move "red" to the back of the all_colors list.
all_colors.remove("red")
all_colors.append("red")
print("RED TO THE BACK", all_colors)

# 11. Ask the user for a number between 1 and the length of the all_colors
#      list. Actually display the length of the list in the prompt, so
#      the user doesn't have to guess the limit. Create a new list called
#      some_colors with this number of colors from the all_colors list.
number = input(f"Select a number between 1 and {all_col_length}")
number = int(number)
some_colors = all_colors[:number]
print("SOME COLORS", some_colors)
# 12. Print out the index of "green" in some_colors list. If it is not in
#      the some_colors list, print out a apologetic message to the user
#      that there is no green in the some_colors list.
if "green" in some_colors:
    print("INDEX OF GREEN", some_colors.index("green"))
else: print("There is no green in the some colors list")

# 13. Print out the some_colors list on one line, with "ish" added to
#      each color. (For example: "yellowish greenish orangeish ...")
some_colors = [color+"ish" for color in some_colors]
print("ADD ISH", some_colors)