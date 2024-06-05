# 1. Write a function to find the sum of the series, up to n terms.
#     ie. 2 + 22 + 222 + 2222 + .. n terms
#     Call the function with number_of_terms to verify that your
#     function works as expected.
number_of_terms = 5  # => 24690 (total of 2 + 22 + 222 + 2222 + 22222)

def sum_of_all_2(var_num, repeat_num):
    empty_list = []
    for i in range(1,var_num+1):
        empty_list.append(str(repeat_num)*i)
    list_of_2s = list(map(lambda x: int(x), empty_list))
    return sum(list_of_2s)

print("Sum of 2s: ", sum_of_all_2(number_of_terms,2))

#    b. Change number_of_terms to verify that your function is correct.
number_of_terms = 10

print("Sum of 2s: ", sum_of_all_2(number_of_terms,10))

# 2. Print out the following pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

#===================================NOOB WAY===================================
# list_of_stars = ["*","**","***","****","*****","****","***","**","*"]

# for star in list_of_stars:
#     print(star)

#===============================CHALLENGING WAY=================================
def great_pyramid_of_giza(max_length):
    for i in range(1,max_length+1):
        print("*" * i)
    for i in range(max_length-1,0,-1):
        print("*" * i)

great_pyramid_of_giza(100)

# 3. Write a function calculation() such that it can accept two variables
#     and calculate the addition and subtraction of them. It must return
#     both addition and subtraction results in a single function call.
def calculation(x,y):
    add = x + y
    subtract = x - y
    return {add,subtract}

print("[sum,difference]: ", calculation(10,5))


# 4. Generate a Python list of all the even numbers between 4 and 30
def return_even_list():
    empty_num_list = []
    for i in range(4,31):
        if i % 2 == 0: empty_num_list.append(i)
    return empty_num_list

print("Print even num between 4-30:", return_even_list())


# 5. Write a function that returns the largest item from the following list:
lst = [4, 6, 8, 24, 12, 2]

def largest_num_in_list(user_list):
    return max(user_list)

print("Largest number in 1st list:", largest_num_in_list(lst))

#    b. Change the list to verify your function is correct.
another_list = [923, 7123, 9, 123, 8191029, 232]

print("Largest number in 2nd list:", largest_num_in_list(another_list))


# 6. Write a function that given a string of odd length greater than 7,
#     it returns a new string made up of the middle three characters of
#     the string.
def mid_3_string(word):
    if len(word) >= 7 and (len(word) % 2) == 1:
        mid_char = len(word) // 2
        return word[mid_char-1] + word[mid_char] + word[mid_char+1]
    else: return "The provided wrong does not contain at least 7 characters or contains even number of characters"

print("Middle 3 strings: ", mid_3_string("January"))
print("ERROR: ", mid_3_string("February"))
print("ERROR: ", mid_3_string("hello"))

# 7. Write a function that given two strings, s1 and s2, it returns a new
#     string with s2 in the middle of s1. If s1 has an odd number of
#     characters, bias s2 towards the right.
def grotesque_string(s1,s2):
    mid_char = len(s1) // 2
    if len(s1) % 2 == 0:
        return s1[0:mid_char] + s2 + s1[mid_char:len(s1)]
    else:
        return s1[0:mid_char+1] + s2 + s1[mid_char+1:len(s1)]

print("S1-ODD: ",grotesque_string("monkey","eytobuytur"))

print("S1-EVEN: ",grotesque_string("tulip", "rns"))

