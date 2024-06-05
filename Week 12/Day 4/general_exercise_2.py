# 1. A pair of strings form a strange pair if both of the following are true:
#    - The 1st string's first letter = 2nd string's last letter.
#    - The 1st string's last letter = 2nd string's first letter.
#     Create a function that returns True if a pair of strings constitutes
#     a strange pair, and False otherwise.
#    EXAMPLES:
#     is_strange_pair("ratio", "orator")  # => True
#     is_strange_pair("sparkling", "groups")  # => True
#     is_strange_pair("bush", "hubris")  # => False
#     is_strange_pair("", "")  # => True
def is_strange_pair(str1, str2):
    if str1 == "" and str2 == "":
        return True
    elif str1[0] == str2[-1] and str1[-1] == str2[0]:
        return True
    else: return False

print("1a TRUE: ", is_strange_pair("ratio", "orator"))
print("1b TRUE: ", is_strange_pair("sparkling", "groups"))
print("1c FALSE: ", is_strange_pair("bush", "hubris"))
print("1d TRUE: ", is_strange_pair("", ""))

# 2. Create a function that accepts a string as an argument and returns the
#     first non-repeated character. Return False if all characters repeat
#     or if a blank string is provided.
#    EXAMPLES:
#     first_nrc("g")  # => "g"
#     first_nrc("it was then the frothy word met the round night")  # => "a"
#     first_nrc("the quick brown fox jumps then quickly blows air")  # => "f"
#     first_nrc("hheelloo")  # => False
#     first_nrc("")  # => False
def first_nrc(word):
    filtered_letters = [letter for letter in word if word.count(letter) < 2]
    if len(filtered_letters) >= 1:
        return filtered_letters[0]
    else: return False

print("2a: ", first_nrc("g"))
print("2b: ", first_nrc("it was then the frothy word met the round night"))
print("2c: ", first_nrc("hheelloo"))
print("2d: ", first_nrc(""))

# 3. Create a function that takes a phrase and transforms each word using the
#     following rules:
#    - Keep first and last character the same.
#    - Transform middle characters into a dash -.
#    - Words with two or fewer letters should not be hidden at all.
#    EXAMPLES:
#     ltr_hide("skies were pretty")  # => "s---s w--e p----y"
#     ltr_hide("red is not my color")  # => "r-d is n-t my c---r"
#     ltr_hide("She rolled her eyes")  # => "S-e r----d h-r e--s"

#     ltr_hide("Harry went to fight the basilisk")
#     Outputs:
#      "H---y w--t to f---t t-e b------k"
def ltr_hide(sentence):
    words_list = sentence.split()
    words_list = [word[:1] + ("-" * (len(word)-2)) + word[-1:] if (len(word) >= 3) else word \
                  for word in words_list]
    return " ".join(words_list)

print("3a: ", ltr_hide("skies were pretty"))
print("3b: ", ltr_hide("red is not my color"))
print("3c: ", ltr_hide("She rolled her eyes"))
print("3d: ", ltr_hide("Harry went to fight the basilisk"))

# 4. Create a function that counts the number of towers.
#    EXAMPLES:
#     count_towers([
#       ["     ##         "],
#       ["##   ##        ##"],
#       ["##   ##   ##   ##"],
#       ["##   ##   ##   ##"]
#     ])  # => 4
#     count_towers([
#       ["                         ##"],
#       ["##             ##   ##   ##"],
#       ["##        ##   ##   ##   ##"],
#       ["##   ##   ##   ##   ##   ##"]
#     ])  # => 6
#     count_towers([
#       ["##"],
#       ["##"]
#     ])  # => 1
def count_towers(tower_list):
    foundation = tower_list[-1][0]
    return len(foundation.split())

print("4a: ", count_towers([
      ["     ##         "],
      ["##   ##        ##"],
      ["##   ##   ##   ##"],
      ["##   ##   ##   ##"]
    ]))
print("4b: ", count_towers([
      ["                         ##"],
      ["##             ##   ##   ##"],
      ["##        ##   ##   ##   ##"],
      ["##   ##   ##   ##   ##   ##"]
    ]))
print("4c: ", count_towers([
      ["##"],
      ["##"]
    ]))

# 5. Given a list of integers, find the pair of adjacent elements that have
#     the largest product and return that product.
#    EXAMPLES:
#     adjacent_product([3, 6, -2, -5, 7, 3])  # => 21
#     adjacent_product([5, 6, -4, 2, 3, 2, -23])  # => 30
#     adjacent_product([0, -1, 1, 24, 1, -4, 8, 10])  # => 80
def adjacent_product(num_list):
    max = 0
    for i in range(len(num_list)-1):
        if num_list[i] * num_list [i+1] > max:
            max = num_list[i] * num_list[i+1]
    return max

print("5a: ", adjacent_product([3, 6, -2, -5, 7, 3]))
print("5b: ", adjacent_product([5, 6, -4, 2, 3, 2, -23]))
print("5c: ", adjacent_product([0, -1, 1, 24, 1, -4, 8, 10]))
        
# 6. You are to read each part of the date into its own integer type variable.
#     The year should be a 4 digit number. You can assume the user enters a
#     correct date (no error checking required). Determine whether the
#     entered date is a magic date. Here are the rules for a magic date:
#    - mm * dd is a 1-digit number that matches the last digit of yyyy or
#    - mm * dd is a 2-digit number that matches the last 2 digits of yyyy or
#    - mm * dd is a 3-digit number that matches the last 3 digits of yyyy
#     The program should then display True if the date is magic, or
#     False if it is not.
#    EXAMPLES:
#     magic("1 1 2011")  # => True
#     magic("4 1 2001")  # => False
#     magic("5 2 2010")  # => True
#     magic("9 2 2011")  # => False
def magic(date):
    date_list = date.split()
    date_list = [int(num) for num in date_list]
    if len(str(date_list[0] * date_list[1])) == 1:
        return str(date_list[0] * date_list[1]) == str(date_list[2])[-1:]
    elif len(str(date_list[0] * date_list[1])) == 2:
        return str(date_list[0] * date_list[1]) == str(date_list[2])[-2:]
    elif len(str(date_list[0] * date_list[1])) == 3:
        return str(date_list[0] * date_list[1]) == str(date_list[2])[-3:]
    
print("6a: ", magic("1 1 2011"))
print("6b: ", magic("4 1 2001"))
print("6c: ", magic("5 2 2010"))
print("6d: ", magic("9 2 2011"))