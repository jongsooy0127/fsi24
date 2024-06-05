x = 5
y = 10

def do_something(num):
    global x, y   # This allows access to the enclosing scope's variable
    print(x, y)   # => 5
    x = num    # global var x is now set to 43
    y = num
    print(x, y)   # => 43

do_something(43)
print(x, y)

count = 0

ran_list = [1,2,3,4,5]

for num in ran_list:
    count += 1

print(count)

step = 0

def raise_step(num):
    step = num
    print(step)

raise_step(10)

print(step)