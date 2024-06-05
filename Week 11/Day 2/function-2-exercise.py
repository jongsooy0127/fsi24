# 1. Write a Python function that takes a list of words and returns the
#     longest word and the length of the longest word.
longest_word = ""

# #Function to find the longest word 
# def find_the_longest_word(*words):
#     words = list(words)
#     for i in range(0,len(words)-1):
#         longest_word = words[0]
#         if len(words[i+1]) > len(words[i]):
#             longest_word = words[i+1]
#             return [longest_word, len(longest_word)]
        
# #Print the longest word
# print("ANS: TEMPERATURE:", find_the_longest_word("hello","world","temperature"))

#Change the values in list according to your needs
my_list = ["hello", "worlds", "temperature"]

#Function to find the longest word
def find_the_longest_word(put_list_here):
    for i in range(0,len(put_list_here)-1):
        longest_word = put_list_here[0]
        if len(put_list_here[i+1]) > len(put_list_here[i]):
            longest_word = put_list_here[i+1]
    return [longest_word, len(longest_word)]

#    b. Call the function with positional arguments
print("Find the longest word:",find_the_longest_word(my_list))

#    c. Call the function with keyword arguments
print("Find the longest word:",find_the_longest_word(put_list_here = my_list))


# 2. Write a Python function to remove the n-th index character from a
#     nonempty string.
def remove_nth_letter(word, n):
    word = word[:n-1] + word[n:]
    return word

#    b. Call the function with positional arguments
print(remove_nth_letter("Monday",3))

#    c. Call the function with keyword arguments
print(remove_nth_letter(n = 5, word = "Pikachu"))


# 3. Create a function called add_title which takes a name and gender as
#     arguments and returns either "Mr. <name>" or "Ms. <name>"
#     (eg. Calling `add_title("Pam", "F")` returns "Ms. Pam")
def add_title(name, gender):
    if gender == "F":
        return "Ms." + name
    elif gender == "M":
        return "Mr." + name
    else: return "GET A NAME! AND A GENDER!"

#    b. Call the function with positional arguments
print("Add Mr to name:", add_title("Jay", "M"))

#    c. Call the function with keyword arguments
print("Add Ms to name:", add_title(gender = "F", name = "Laney"))


# 4. Create a function called multiply_elements which takes a list and a
#     number as arguments. It multiplies each element in the list by the
#     number, and returns the list
num_list = [1,2,3,4,5]

def multiply_elements(list_of_nums, multiply_num):
    for i in range(0,len(list_of_nums)):
        list_of_nums[i] = list_of_nums[i] * multiply_num
    return list_of_nums

#    b. Call the function with positional arguments
print("Multiply list by 2:", multiply_elements(num_list,2))

#    c. Call the function with keyword arguments
copy_list = [1,2,3,4,5]
print("Multiply list by 69:", 
      multiply_elements(multiply_num=69, list_of_nums=copy_list))