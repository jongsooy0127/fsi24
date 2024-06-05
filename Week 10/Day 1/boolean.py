# What value does each expression produce? Verify your answers by printing out
# the expressions with Python. Or, use the Python IDLE.

# True and not False # what is the output?
# #TRUE => ANS: TRUE

# True and not false # what is the output?
# #ERROR => ANS: ERROR

# True or True and False # what is the output?
# #FALSE => ANS: TRUE (AND TAKES PRECEDENCE OVER OR)

# not True or not False # what is the output?
# #TRUE => ANS: TRUE

# True and not 0 # what is the output?
# #TRUE => ANS: TRUE

# 52 < 52.3 # what is the output?
# #TRUE => ANS: TRUE

# 1 + 52 < 52.3 # what is the output?
# #FALSE => ANS: FALSE

# 4 != 4.0 # what is the output?
# #FALSE => ANS: FALSE

# Variables population and land_area refer to floats.
population = 13_960_000
land_area = 2_191

# 1. Write an if statement that will print the population
#    if it is less than 10,000,000.

# 2. Write an if statement that will print the population
#    if it is between 10,000,000 and 35,000,000.

# 3. Write an if statement that will print “Densely populated”
#    if the land density (number of people per unit of area) is
#    greater than 100.

# 4. Write an if statement that will print “Densely populated”
#    if the land density (number of people per unit of area)
#    is greater than 100, and “Sparsely populated” otherwise.

if population < 10_000_000:
    print("Population:", population)
elif 10_000_000 < population < 35_000_000:
    print("Population:", population)
else:
    print("Yo mama so fat, she counts as 35,000,000 million people to the city's population")

if (population/land_area > 100):
    print("Densely populated:", int(population/land_area), "people per sq km")
else:
    print("Sparsely populated")

# 5. Write a Python program to add 'ing' at the end of a given
#    string (length should be at least 3). If the given string
#    already ends with 'ing' then add 'ly' instead. If the string
#    length of the given string is less than 3, leave it unchanged.

# user_input = input("Please type in a word:")
# if len(user_input) >= 3:
#     if user_input[-3:] == "ing":
#         user_input = user_input+"ly"
#     else: 
#         user_input = user_input+"ing"
# print(user_input)

#################################################################################################
# Variables x and y refer to Boolean values.
x = True
y = False 

# 1. Write an expression that produces True
#     if both variables are True.
True if x and not y else False
print(True if x and not y else False)

# 2. Write an expression that produces True 
#     if x is False.
True if not x == False else False
print(True if not x == False else False)

# 3. Write an expression that produces True 
#     if at least one of the variables is True.
True if x or y else False
print(True if x or y else False)

#4. Variables full and empty refer to Boolean values. 
#     Write an expression that produces True if at most 
#     one of the variables is True. Test the different
#     combinations to be sure!
full = False
empty = False
True if not full or empty else False
print(True if not full or empty else False)
