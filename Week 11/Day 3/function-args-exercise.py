# 1. Create a function multi_print which takes advantage of *args, accepts
#     any number of positional arguments, and prints them all using a for
#     loop, also print the total number of arguments passed into multi_print.
def multi_print(*args):
    for item in args:
        print("ALL ARGS:", item)
    print("LENGTH OF ARGS:", len(args))

multi_print("hi", 2, 15.6, "bye")



# 2. Create a function that accepts any number of numbers as positional
#     arguments and prints the sum of those numbers.
def sum_of_nums(*args):
    return sum(args)

print("Sum of all the nums:", sum_of_nums(10,5,25,20,15))


# 3. Create a function that accepts any number of positional and keyword
#     arguments, and that prints them back to the user. Your output should
#     print the positional arguments on one line, each item separated with
#     the string 'and'. All the keyword arguments should be printed in the
#     format 'key - value', each on a separate line.
def echo(*args, **kwargs):
    # empt_str = ""
    # if len(args) > 0:
    #     for i in range(0,len(args)-1):
    #         empt_str += str(args[i]) + " and "
    #     empt_str += str(args[-1])
    #     print(empt_str)

    new_list = []
    for item in args:
        new_list.append(str(item))

    print(" and ".join(new_list))

    for item in kwargs:
        print(item + " - " + str(kwargs[item]))


echo("apple", 4, True, a="pear", b=12, c=False)
#
#    Examples:
#     echo("apple", "pear", "lime", a="8", b="4", c="3")
#    Outputs:
#     apple and pear and lime
#     a - 8
#     b - 4
#     c - 3
#
#     echo("apple", 4, True, a="pear", b=12, c=False)
#    Outputs:
#     apple and 4 and True
#     a - pear
#     b - 12
#     c - False
#
#     echo("apple")
#    Outputs:
#     apple
#
#     echo(a=8, what="sup")
#    Outputs:
#     a - 8
#     what - sup


# 4. Create a function called 'breakup' that accepts any number of strings or
#     lists of strings, and a 'sep' argument. Return all the strings and list
#     of strings combined, separated by the string given in 'sep'.
def breakup(*args, sep):
    empt_list = []
    for item in args:
        if isinstance(item, list):
            for i in range(0,len(item)):
                empt_list.append(item[i])
        else:
            empt_list.append(item)
    empt_list = sep.join(empt_list)
    print(empt_list)
     
breakup("pink", ["red"], "green", sep=" and ")
#    Examples:
#     breakup("red", "green", sep=" and ") => "red and green"
#     breakup("red", "green", "pink", sep=" and ") => "red and green and pink"
#     breakup(["red", "green"], sep=" and ") => "red and green"
#     breakup("pink", ["red"], "green", sep=" and ") => "pink and red and green"


