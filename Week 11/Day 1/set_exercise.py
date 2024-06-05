# 1. Create a variable, name, with your first name as a string
name = "Jay"

#    b. Add to the name variable your last name with a space in between
name = name + " " + "Yoon"

#    c. Add to the name variable "Mr." or "Ms." or "Mrs." before your full
#        name with a space in between
name = "Mr." + " " + name

#    d. Create a variable, greeting, which contains the string "Hi my name
#        is [YOUR NAME]"
name = f"Hi my name is {name}"

#    e. Print out the greeting
print("GREETING:", name)

# 2. Create a variable, length, with the value 20
length = 20

#    b. Create a variable, height, with the value 15
height = 15

#    c. Create a variable, area, which is equal to length x height
area = length * height

#    d. Create a variable, analysis, which contains the string "the result
#        of [LENGTH] x [HEIGHT] is [AREA]"
analysis = f"The result of {length} x {height} is {area}"

#    e. Print out the analysis variable
print("AREA OF RECTANGLE:", analysis)


# 3. Create a variable, fruits, which is a list of three fruits
fruits = ["mango", "watermelon", "strawberry"]

#    b. Create a variable, veggies, which is a list of three vegetables
veggies = ["cabbage", "lettuce", "carrot"]

#    c. Create a variable, meats, which is a list of three meats
meats = ["beef", "chicken", "fish"]

#    d. Create a variable, food, which is the combination of fruits,
#        veggies, meats
food = fruits + veggies + meats

#    e. Update the value of the food variable by removing all duplicates
#        (food should still be a list)
for item in food:
    if food.count(item) > 1:
        food.remove(item)

#    f. Print out the food variable
print("LIST OF FOOD:", food)


# 4. Create a variable, salary, with the numeric value, 1,000,000
salary = 1_000_000

#    b. Update the salary variable by adding 2,000 to it
salary += 2_000

#    c. Update the salary variable by multiplying it by 5
salary *= 5

#    d. Update the salary variable by dividing it by 1000
salary /= 1_000

#    e. Update the salary variable by floor dividing it by 3
salary //= 3

#    f. Create a variable, phrase, which contains "my salary is $[SALARY]"
phrase = f"my salary is ${salary}"

#    g. Print out the phrase variable
print("SALARY PHRASE:", phrase)


# 5. Create a variable, grades, which contains 5 grades
grades = ["A", "F", "B", "A", "F"]

#    b. Create a variable, remove_duplicates, which contains True
remove_duplicates = True

#    c. Create an if/else statement:
#     * remove all duplicates from grades if remove_duplicates is True
#     * append 'F' to grades if remove_duplicates is False
if remove_duplicates:
    grades = list(set(grades))
else: 
    grades.append("F")
        
#    d. Print out the grades variable
print(grades)


