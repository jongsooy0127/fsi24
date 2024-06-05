# 1. Write a function called 'more_power' that takes one integer argument, called
#     'total' which will be a running total of the power.
#     This function will return another function called 'whatever' that also
#     takes one integer argument, which be added to the 'total' and then will
#     print out the current value of 'total'. Everytime the enclosed function
#     is called, the total will increase.
#    Example:
#     enhance = more_power(1)
#     enhance(32)  # => TOTAL: 33
#     enhance(84)  # => TOTAL: 117
#     enhance(12)  # => TOTAL: 129
#     enhance(93)  # => TOTAL: 222

# total = 0

# def more_power(num_1):
#     global total
#     total = num_1
#     def whatever(num_2):
#         global total
#         total += num_2
#         return total
#     return whatever

# enhance = more_power(1)
# print("ANS 33: ", enhance(32))  # => TOTAL: 33
# print("ANS 117: ", enhance(84))  # => TOTAL: 117
# print("ANS 129: ", enhance(12))  # => TOTAL: 129
# print("ANS 222: ", enhance(93))  # => TOTAL: 222


#=============================ALEX's ANSWER==================================

def more_power(total):
    def whatever(num):
        nonlocal total
        total += num
        print("TOTAL:", total)
    return whatever

enhance = more_power(1)
enhance(32)  # => TOTAL: 33
enhance(84)  # => TOTAL: 117
enhance(12)  # => TOTAL: 129
enhance(93)  # => TOTAL: 222