# 1. Write a Python function to filter a list of integers to only include
#     even numbers using a lambda.

even_list = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8]))

print(even_list)

def get_even_list(user_list):
    even_list = list(filter(lambda x: x % 2 == 0, user_list))
    return even_list

# 2. Write a Python function to square every number in a given list of
#     integers using a lambda.

square_nums_list = list(map(lambda x: x ** 2, [1,2,3,4,5,6,7,8]))

print(square_nums_list)

print(list(filter(lambda x: x % 5 == 0, list(range(1,101)))))

