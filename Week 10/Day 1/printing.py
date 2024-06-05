# print("HELLO WORLD!")

# print("Greeting","and","salutations","to","you")

# print("Hello, World", end="!")
# print("And then?")
# #Prints "Hello, world!And then?"

# print("Hello, World", end="!\n")
# print("And then?")
# #Prints "Hello, world!
# #And then?"

# print("Hello", "World!", sep="&")
# print("Hello", "World!", sep="\n")

"""
EVERYTHING IS COMMENTED OUT IN BETWEEN TRIPLE QUOTES (MULTILINE COMMENT)
"""

# print("This is a single line comment")
# print("This is a comment line #1", "Wow comment line #2", sep="\n")

#print(-7%3) ==> Answer is 2 (Subtract the denominator with the remainder when working with neg nums)

# first_name = "Jong Soo"
# middle_name = "Jay"
# last_name = "Yoon"

# full_name = first_name + " " + middle_name + " " + last_name

# print(full_name)

# Write a Python program to get a string made of the
# first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return the string
# instead of an empty string.

random_string = "League of Legends"
first_two_chars = random_string[:2]
last_two_chars = random_string[-2:]
concat_chars = first_two_chars + last_two_chars
print(concat_chars)

# Write a Python program to get a single string from two
# given strings, separated by a space and swap the first
# two characters of each string.

word_one = "hello"
word_two = "world"

first_two_of_word_one = word_one[:2]
first_two_of_word_two = word_two[:2]

rest_of_word_one = word_one[2:]
rest_of_word_two = word_two[2:]

concat_word = first_two_of_word_one + rest_of_word_two + " " + first_two_of_word_two + rest_of_word_one

print(concat_word)

#################################################################################################

name = "Kim Jung Un"
age = 50
job = "dictator of North Korea"

print(f"{name} is {age} years old. He works as the {job}")

##################################################################################################
# Create a variable called tongue_twister, assign your favorite tongue twister to that variable as a string.
tongue_twister = "The sixth sick sheik's sixth sheep's sick "

# Then, create a variable called count, assign a number between 2 and 1,000 to that variable.
count = 5

# Print out the uppercase version of that tongue twister repeated count number of times.
print(tongue_twister.upper() * count)


# Assign that repeated string to a new variable called tongue_twisters.
tongue_twisters = tongue_twister.upper() * count

# Print the lowercase version of that variable's (tongue_twisters) value.
print(tongue_twisters.lower())

# Then, print the result of multiplying the length of that variable's value by 15,000.
print(len(tongue_twisters.lower()) * 15_000)

# Reassign the value of tongue_twister to be the string 'haha'.
tongue_twister = "haha"

# Reassign the value of tongue_twisters to be the number 9000.
tongue_twisters = 9_000

# Combine the two variables into a single string using an f-string
two_var = f"{tongue_twister}{tongue_twisters}"

# Print the result. (eg. 'haha9000')
print(two_var)


# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
user_input = input("Enter a word: ")
user_input = user_input.lower()
first_letter = user_input[:1]
rest_of_user_input = user_input[1:]
print(first_letter + rest_of_user_input.replace(first_letter, "$"))

