# Repeat the previous exercise using for loops and 'range'.

# 1. Print the first 10 natural numbers.
for i in range(1,11):
    print(i,end="")

print()

# 2. Print the following pattern:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
display = ""
for i in range(1,6):
    display += str(i) + " "
    print(display)

# 3. Print the first 10 multiples of a given number on a single line.
#     For example: 2 4 6 8 10 12 14 16 18 20
display = ""
for i in range(2,22,2):
    display += str(i) + " "
print(display)

# 4. Given the following list, display numbers divisible by five, 
#     and if you find a number greater than 150, stop the loop.
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 173,180, 200]
for num in list1:
    if num > 150:
        break
    elif num % 5 == 0:
        print("NUM DIVISIBLE BY 5", num)

# 5. Display numbers from -10 to -1.
display = ""
for i in range(-10,0):
    display += str(i) + " "
print(display)


