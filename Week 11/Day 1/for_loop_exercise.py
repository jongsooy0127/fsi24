# 1. Print the first 10 natural numbers.
display = ""
for num in [1,2,3,4,5,6,7,8,9,10]:
    display += str(num) + " "
print(display)
# 2. Print the following pattern:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
display = ""
for num in [1,2,3,4,5]:
    display += str(num) + " "
    print(display)
# 3. Print the first 10 multiples of a given number on a single line.
#     For example: 2 4 6 8 10 12 14 16 18 20
display = ""
factor = 2
for num in [1,2,3,4,5,6,7,8,9,10]:
    display += str(num * factor) + " "
print(display)

# 4. Given the following list, display numbers divisible by five, 
#     and if you find a number greater than 150, stop the loop.
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 173, 180, 200]
for number in list1:
    if number > 150:
        break
    elif number % 5 == 0:
        print("\nNUMBER DIVISIBLE BY 5:", number)

# 5. Display numbers from -10 to -1.
for number in [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]:
    print(number)