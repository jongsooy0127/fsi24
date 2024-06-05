# 1. Write a function named 'difference' that has two parameters, a and b.
#     The function should return b subtracted from a.
def difference(a,b):
    return a - b 

#    b. Call the function with positional arguments
print("Diff 10-5:", difference(5,10))

#    c. Call the function with keyword arguments
print("Diff 10-5:", difference(b=10, a=5))


# 2. Write a convert_temperatures(t, source, target) function to convert
#     temperature t from source units to target units, where source and
#     target are each one of: "Kelvin", "Celsius", "Fahrenheit", "Rankine",
#     "Delisle", "Newton", "Reaumur", and "Romer" units.
def convert_temperatures(t, source, target):

    if source == "Celsius":
        t = t + 273.15
    elif source == "Fahrenheit":
        t = (t + 459.67) * (5/9)
    elif source == "Rankine":
        t = t * (5/9)
    elif source == "Delisle":
        t = 373.15 - (t * 2/3)
    elif source == "Newton":
        t = (t * 3.03030303) + 273.15
    elif source == "Reaumur":
        t = (t * 1.25) + 273.15
    elif source == "Romer":
        t = ((t - 7.5) * 1.9047619) + 273.15
    elif source == "Kelvin":
        t = t
        
    if target == "Kelvin":
        return t
    if target == "Celsius":
        return round(t - 273.15,2)
    elif target == "Fahrenheit":
        return round((t * (9/5)) - 459.67,2)
    elif target == "Rankine":
        return round(t * 1.8,2)
    elif target == "Delisle":
        return round((373.15 - t) * (3/2),2)
    elif target == "Newton":
        return round((t - 273.15) / 3.03030303,2)
    elif target == "Reaumur":
        return round(((t - 273.15) / 1.25),2)
    elif target == "Romer":
        return round(((t - 273.15) / 1.9047619) + 7.5,2)

#    b. Call the function with positional arguments
print("Test Kelvin to Kelvin return 420:", convert_temperatures(420, "Kelvin", "Kelvin"))

#    c. Call the function with keyword arguments

print("2b: 38.75:", convert_temperatures(31, target="Celsius", source="Reaumur"))
print("2b: 101.75:", convert_temperatures(31, target="Fahrenheit", source="Reaumur"))
print("2b: 561.42:", convert_temperatures(31, target="Rankine", source="Reaumur"))
print("2b: 91.88:", convert_temperatures(31, target="Delisle", source="Reaumur"))
print("2b: 12.79:", convert_temperatures(31, target="Newton", source="Reaumur"))
print("2b: 31:", convert_temperatures(31, target="Reaumur", source="Reaumur"))
print("2b: 311.90:", convert_temperatures(31, target="Kelvin", source="Reaumur"))


# 3. Write a function `first_and_last(str, num)` to get a string (str) and
#     num (int). It should return the first 'num' and the last 'num' chars
#     from the given str. If str's length is less than num, return '???'
#     instead of an empty or partial string.
#watermelon, 3 => wat, lon

def first_and_last(str, num):
    if len(str) < num:
        return "???"
    else:
        first = str[:num]
        last = str[-num:]
        return {first,last}

#    b. Call the function with positional arguments
print("heh:", first_and_last("heheheh", 3))
print("???:", first_and_last("Hello World!", 1_000_000))


#    c. Call the function with keyword arguments
print("wate, elon:", first_and_last(num=4, str="watermelon"))

print("first item in set:", list(first_and_last(num=4, str="watermelon"))[0])
print("second item in set:", list(first_and_last(num=4, str="watermelon"))[1])