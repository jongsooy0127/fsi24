# 1. Write a function to find the largest of three numbers, without using
#     the built-in `max` function.

def find_max_num(a,b,c):
    list_of_nums = [a,b,c]
    max_num = list_of_nums[0]
    for num in list_of_nums:
        if num > max_num:
            max_num = num
    return max_num

print("Prints the largest num:", find_max_num(900,4900,200))

# 2. Write a function to sum all the numbers in a list, without using the
#     built-in `sum` function.

def add_nums_list(num_list):
    total_sum = 0
    for i in range(0,len(num_list)):
        total_sum += num_list[i]
    return total_sum

print("SUM OF TOTAL IN LIST:", add_nums_list([88,24,93,1234,9085]))

# 3. Write a function to multiply all the numbers in a list, without using
#     any library functions.

def multiply_nums_in_list(num_list):
    final_num = 1
    for i in range(0,len(num_list)):
        final_num *= num_list[i]
    return final_num

print("ALL NUMS MULTIPLIED:",multiply_nums_in_list([3,5,12,2,3]))


# 4. Write a function to reverse a string, without using the built-in
#     `reverse` function.
def reverse_str(word):
    word = list(word)
    # print(word)
    new_word_list = []
    for i in range(len(word)-1, -1, -1):
        new_word_list.append(word[i])
    reverse_word = "".join(new_word_list)
    return reverse_word

print("REVERSE STR:", reverse_str("I HECKING LOVE PYTHON"))
    


# 5. Write a function called 'withinRange' that takes three parameters,
#     a number you are checking for, the first number to check against and
#     the last number to check against. Check whether the first number falls
#     in the other numbers (inclusive) and return a boolean.
def within_range(check_num,min,max):
    if min <= check_num <= max:
        return True
    else: 
        return False
    
print(within_range(0,1,5))


# 6. Write a function that takes a list and returns a new list with
#     unique elements of the first list.

def unique_elem_list(user_list):
    unique_list = []
    for item in user_list:
        if (item in unique_list) == False:
            unique_list.append(item)
    return unique_list

print(unique_elem_list(["a","b","c","a","b","d","y","g","a","g"]))

# 7. Write a function that takes a number as a parameter and checks if the
#     number is prime or not.
def check_prime(num):
    for i in range(2,num-1):
        if num % i == 0:
            return str(num) + " is not a prime number"
    return str(num) + " is a prime number"

print("Is num a prime?", check_prime(2))

# 8. Write a function to print only the even numbers from a given list.
def check_even(user_list):
    empty_list = []
    for i in range(0,len(user_list)):
        if (user_list[i] % 2) == 0:
            empty_list.append(user_list[i])
    return empty_list

print("EVEN NUMBER LIST:", check_even([1,2,3,4,5,6,7,8,9,10,71,100]))


# 9. Write a function to create and print the list of squares for the
#      numbers between 1 and 30 (both included).
def square_1_to_30():
    empty_list = []
    for i in range(1,31):
        empty_list.append(i**2)
    return empty_list

print("Square nums 1 to 30:", square_1_to_30())