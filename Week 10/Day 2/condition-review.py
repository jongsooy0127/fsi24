# # 1. Ask your user for a first name value using the input function and
# #     assign the result to a variable called first_name.
# first_name = input("What is your first name?: ")

# #    b. Ask your user for a last name value using the input function and
# #        assign the result to a variable called last_name.
# last_name = input("What is your last name?: ")

# #    c. Combine first_name and last_name into a single variable full_name
# #        and print out the length of the string contained in that variable.
# full_name = first_name + last_name
# print("Full Name Length:", len(full_name))

# # 2. Ask your user for a greeting and store it in a variable called greeting.
# greeting = input("Please enter a greeting: ")
# greeting = greeting + " "

# #    b. Ask your user for the number of times they want to repeat that
# #        greeting and store it in a variable called count.
# count = int(input("How many times shall we print out the greeting?"))

# #    c. Print out whether or not the count is less than 100.
# if count < 100:
#     print("We will repeat your greeting less than 100 times")
# else:
#     print("We will repeat your greeting more than 100 times")

# #    d. Print out the greeting repeated count number of times.
# print(greeting * count)


# # 3. Ask your user for the lowest value in a range and store it in a
# #     variable called low.
# low = int(input("Enter the lowest value in your range"))

# #    b. Ask your user for the highest value in a range and store it in
# #        a variable called high.
# high = int(input("Enter the highest value in your range"))

# #    c. Ask the user for a value, and print whether or not that value
# #        is in the range (inclusive).
# user_value = int(input("What number would you like to store in the range?"))
# if low <= user_value <= high:
#     print("Your number is within the range")
# else: 
#     print("Your number is outside the range")

################################################################################################ 

# Try multiplying a string by 3
random_string = "string"
print(random_string * 2)

# Try multiplying a list by 3
li = [1,2,3,4]
print(li * 2)

# What do predict you get with the following?
# 'haha' and 'hoho' # True => Ans: 'hoho' (Both values are true, so the right most value wins)
# '' and 'yala' # False => Ans: '' ('' is false so that value of '' wins due to it being False)
# 'yolo' or '' #True => Ans: 'yolo' (True so 'yolo' takes precendence)
# Print the expressions to confirm.

# What do predict you get with the following?
# 5 and 4 #True => Ans: 4
# 1 and 1 #True => Ans: 1
# 0 and 6 #False => Ans: 0
# Print the expressions to confirm.

# What do predict you get with the following?
# 1 and 'nana' and True #True => Ans: True
# Print the expressions to confirm.

# Given the variables:
name = 'John'
job = 'engineer'

# Rewrite the following using an f-string:
# print('Hi my name is ' + name + ' and I am an ' + job)
print(f"Hi my name is {name} and I am an {job} job")

# Rewrite the following using a '+' operator:
# print(f'I heard that {name} is a really great {job}')
print("I heard that " + name + " is a really great " + job)

# Print this list in reverse:
# [1, 5, 8, 'Bob']
random_li = [1,5,8,'Bob']
print(random_li[::-1])

# Make the following statement print out 10 using parentheses:
# print(2 + 3 * 2 - 1 - 1)
print((2 + 3) * 2 - (1 - 1))

