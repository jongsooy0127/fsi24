# 1. Reverse the following integer number:
num = 83275
num = str(num)
i = len(num)-1
empty_list = []

while(i >= 0):
    empty_list.append(num[i])
    i -= 1
empty_list = "".join(empty_list)
print(empty_list)


# 2. Display the subsequent cubes of the following number up to 1 million:
grow = 3
while (grow < 1_000_000):
    grow = grow ** 3
print(grow)
    

# 3. Ask the user for numbers until they enter no number. Then throw out the
#     max and min numbers (if max or min appear more than once, throw those
#     out, as well) and print out the mean of all the numbers up to 2
#     decimal places.
playing = True
user_arr = set()
while playing:
    user_input = input("Provide a number:")
    if user_input != "":
        user_arr.add(int(user_input))
    else:
        break

user_arr = list(user_arr)
user_arr.remove(min(user_arr))
user_arr.remove(max(user_arr))
user_mean = sum(user_arr)/len(user_arr)
print(f"FINAL RESULTS: {user_mean}")