# 1. Get a 3-digit number from the user. Ask that all three digits are
#     different numbers. Store this number in a variable called 'first_num'.
first_num = input("Please provide a three digit number with all three digits being different numbers")
print("First Num", first_num)

# 2. Validate that all 3 digits are different numbers. If not, instruct
#    the user to run the exercise again with a valid number and stop
#    running the rest of the code by calling 'exit()'.
if (first_num[0] == first_num[1]) and (first_num[1] == first_num[2]) and (first_num[0] == first_num[2]) and (len(first_num) > 3):
    print("Please read the instructions and try again!")

# 3. Reverse the 3 digits in first_num, without using the list 'reverse'
#    or 'reversed' functions. Use only what you've learned so far.
#    Save this reversed number in another variable called 'second_num'.
else: 
    second_num = first_num[::-1]
    print("Second Num", second_num)

# 4. Subtract second_num from first_num and store the result in another
#    variable called 'third_num'. If third_num is a negative number
#    turn it into a positive number.
first_num = int(first_num)
second_num = int(second_num)
third_num = first_num - second_num
if third_num < 0:
    third_num = third_num * -1
    print("Third Num", third_num)
else:
    third_num = third_num
    print(third_num)

# 5. Reverse third_num and save it to a variable called 'fourth_num'.
fourth_num = (str(third_num))[::-1]
fourth_num = int(fourth_num)
print("Fourth Num:", fourth_num)

# 6. Add third_num and fourth_num and print out the result. (1089)
print("Add 3rd and 4th Num:", third_num + fourth_num)

# 7. Subtract the lesser number of first_num and second_num from the
#    greater number of first_num and second_num so that you end up
#    with a positive number for the difference. Save this difference
#    in a variable called 'fs_diff'.
fs_diff = third_num

hundreds = third_num // 100
tens = (fs_diff - (hundreds * 100)) // 10
ones = (fs_diff - (hundreds * 100) - (tens * 10))
print("HUNDREDS", hundreds)
print("TENS",tens)
print("ONES", ones)

fs_diff = str(third_num)
firstdig = fs_diff[0]
secdig = fs_diff[1]
thirddig = fs_diff[2]
firstdig = int(firstdig)
secdig = int(secdig)
thirddig = int(thirddig)

# 8. Add up the individual digits that make up fs_diff and print out
#    the resulting sum. (18)
fs_diff = firstdig + secdig + thirddig
print("FS_DIFF:", fs_diff)