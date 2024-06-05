# 1. Find all of the numbers from 1–1000 that are divisible by 8.
div_by_8 = [num for num in range(1,1001) if num % 8 == 0]
print("Nums that are divisible by 8: ", div_by_8)

# 2. Find all of the numbers from 1–1000 that have a 6 in them.
nums_with_six = [num for num in range(1,1001) if "6" in str(num)]
print("Nums with 6: ", nums_with_six)

# 3. Use the following for the questions below:
string = "Practice Problems to Drill List Comprehension into Your Head."

#    b. Count the number of spaces in a string (use string above).
list_of_space = [space for space in string if space == " "]
print("Number of empty space: ", len(list_of_space))

#    c. Remove all of the vowels in a string (use string above).
string_without_vowels = [word for word in string if word not in "aeiou"]
print("".join(string_without_vowels))

#    d. Find all of the words in a string that are less than 5 letters
#        (use string above).
string_list = string[:-1].split()
less_than_5_char = [word for word in string_list if len(word) < 5]
print("Words with less than 5 chars: ", less_than_5_char)

#    e. Use a dictionary comprehension to count the length of each word in
#        a sentence (use string above).

dict_comprehension = {word: len(word) for word in string_list}
print("Word: Length of word - ", dict_comprehension)

# 4. Use the following for the questions below:
nums = [i for i in range(1,1001)]

#    b. Write a list comprehension that produces a list of each number
#        doubled. (use nums list above).
double_nums = [num * 2 for num in nums]
print("Double nums in list: ", double_nums)

#    c. Write a list comprehension that produces a list of the squares of
#        each number (use nums list above).
square_nums = [num ** 2 for num in nums]
print("Square nums: ", square_nums)

#    d. Write a list comprehension that produces a list of only the even
#        numbers in that list (use nums list above).
even_nums = [num for num in nums if num % 2 == 0]
print("List of even nums: ", even_nums)

#    e. Write a list comprehension that produces a list of only the odd
#        numbers in that list (use nums list above).
odd_nums = [num for num in nums if num % 2 == 1]
print("List of odd nums: ", odd_nums)

#    f. Write a list comprehension that produces a list of only the positive
#        numbers in that list (use nums list above).
print("Positive nums: ", nums)


# 5. Create a dictionary from the following list with same key:value pairs.
#     eg. {"key": "key"}.
lst = ["NY", "FL", "CA", "VT"]
state_dict = {key: key for key in lst}
print("State Dictionary: ", state_dict)


# 6. Using dict comprehension, create a dictionary where each number in the
#     range is the key and each item divided by 100 is the value. Use a
#     range from 100 to 160 with steps of 10.
num_dict = {num: num/100 for num in range(100,161,10)}
print("Num Dict: ", num_dict)


# 7. Using dict comprehension and a conditional argument, create a
#     dictionary from the following dictionary where only the key:value
#     pairs with value above 2000 are taken to the new dictionary.
stonks = { "NFLX": 4950, "TREX": 2400, "FIZZ": 1800, "XPO": 1700 }
bigly_stonks_dict = {key:value for key, value in stonks.items() if value > 2000}
print("Bigly stonks: ", bigly_stonks_dict)