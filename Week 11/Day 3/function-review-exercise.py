# 1. Ask the user for a number. Depending on whether the number is even or
#     odd, print out an appropriate message to the user. If the number is a
#     multiple of 4, print out yet a different message.

def check_even_odd_4s(num):
    if num % 4 == 0:
        return (f"{num} is a multiple of 4")
    elif num % 2 == 0:
        return (f"{num} is an even number")
    else: return (f"{num} is an odd number")

user_num = int(input("Provide me a number:"))

print(check_even_odd_4s(user_num))

# 2. Use the following list and write a function that prints out all the
#     elements of the list that are less than 5.
arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def nums_less_than_5(arr):
    random_list = []
    for num in arr:
        if num < 5:
            print(num)

nums_less_than_5(arr)

#    b. Instead of printing the elements one by one, make a new list that
#        has all the elements from arr that are less than 5 and print
#        out this new list.

def list_of_nums_less_than_5(arr):
    new_list = []
    for num in arr:
        if (num < 5):
            new_list.append(num)
    return new_list

print("List of nums less than 5:", list_of_nums_less_than_5(arr))


# 3. Create a function that asks the user for a number and then prints out a
#     list of all the divisors of that number.
def print_all_divisor(num):
    num_list = []
    for i in range(1,num+1):
        if num % i == 0:
            num_list.append(i)
    return num_list

print("Divisor of 135:", (print_all_divisor(135)))


# 4. Use the following lists and write a function that returns a new list that
#     contains only the elements that are common between the lists (without 
#     duplicates).
arr1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def unique_element(arr1, arr2):
    new_list = []
    for item in arr1:
        new_list.append(item)
    for item in arr2:
        new_list.append(item)
    new_list = list(set(new_list))
    return new_list

print("All unique elements:", unique_element(arr1, arr2),
       "Length of list:", len(unique_element(arr1, arr2)))

#================================ANOTHER ONE!===================================

def unique_element_in_2lists(arr1, arr2):
    new_list = []
    for item in arr1:
        if item not in new_list: #OR if (item in new_list) == False
            new_list.append(item)
    for item in arr2:
        if item not in new_list: #OR if (item in new_list) == False
            new_list.append(item)
    return new_list

print("All unique elements #2:", unique_element_in_2lists(arr1, arr2),
       "Length of list:", len(unique_element_in_2lists(arr1, arr2)))


# 5. Write a function that asks the user for a string and prints out whether
#     this string is a palindrome or not. (A palindrome is a string that
#     reads the same forwards and backwards.)
def check_palindrome(word):
    if (word.replace(" ","").upper()) == (word.replace(" ","").upper()[::-1]):
        return (f"[{word}]: is a palindrome")
    else: return (f"[{word}]: is not a palindrome")

print(check_palindrome("Was it a car or a cat I saw"))

print(check_palindrome("Sally sells seashells by the seashore"))