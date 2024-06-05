import math
#===============================IMPORTS ABOVE=================================


# 1. Your task is to create a Circle constructor that creates a circle with a
#     radius provided by an argument. The circles constructed must have two
#     instance methods: get_area() (πr^2) and get_circumference() (2πr)
#     which give both respective areas and circumference.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)
        
    def get_circumference(self):
        return 2 * math.pi * self.radius
    
#    EXAMPLES:
#     circy = Circle(11)
#     circy.get_area()
#     Should return 380.132711084365
circy = Circle(11)
print("Area of circle: ", circy.get_area())

#     circy = Circle(4.44)
#     circy.get_circumference()
#     Should return 27.897342763877365
circy = Circle(4.44)
print("Circumference of new circle: ", circy.get_circumference())

# 2. Create methods for the Calculator class that can do the following:
#    - Add two numbers
#    - Subtract two numbers
#    - Multiply two numbers
#    - Divide two numbers
class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        return num1 / num2
    
#    EXAMPLES:
#     calculator = Calculator()
#     calculator.add(10, 5)  # => 15
#     calculator.subtract(10, 5)  # => 5
#     calculator.multiply(10, 5)  # => 50
#     calculator.divide(10, 5)  # => 2
calculator = Calculator()
print("Addition: ", calculator.add(10,5))
print("Subtraction: ", calculator.subtract(10, 5))
print("Multiplication: ", calculator.multiply(10, 5))
print("Division: ", calculator.divide(10, 5))

# 3. Create a method in the Person class which returns how another person's
#     age compares. Given the objects p1, p2 and p3, which will be
#     initialised with the attributes name and age, return a sentence in
#     the following format:
#     {other_person} is {older than / younger than / the same age as} me.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def compare_age(self, other_person):
        if self.age > other_person.age:
            return f"{other_person.name} is younger than me"
        elif self.age < other_person.age:
            return f"{other_person.name} is older than me"
        else:
            return f"{other_person.name} is the same age as me."
#    EXAMPLES:
#     p1 = Person("Samuel", 24)
#     p2 = Person("Joel", 36)
#     p3 = Person("Lily", 24)
#     p1.compare_age(p2)  # => "Joel is older than me."
#     p2.compare_age(p1)  # => "Samuel is younger than me."
#     p1.compare_age(p3)  # => "Lily is the same age as me."
p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)
print("Compare Samuel to Joel: ", p1.compare_age(p2))
print("Compare Joel to Samuel: ", p2.compare_age(p1))
print("Compare Samuel to Lily: ", p1.compare_age(p3))

# 4. Create the instance attributes fullname, firstname, lastname and email
#     in an Employee class. Given a person's first and last names:
#    - Form the fullname by simply joining the first and last name together,
#       separated by a space.
#    - Form the email by joining the first and last name together with
#       a . in between, and follow it with @company.com at the end. Make
#       sure the entire email is in lowercase.
class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = f"{firstname} {lastname}"
        self.email = f"{firstname.lower()}.{lastname.lower()}@company.com"

#    EXAMPLES:
#     emp_1 = Employee("John", "Smith")
#     emp_2 = Employee("Mary", "Sue")
#     emp_3 = Employee("Antony", "Walker")
#     emp_1.fullname  # => "John Smith"
#     emp_2.email  # => "mary.sue@company.com"
#     emp_3.firstname  # => "Antony"
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary", "Sue")
emp_3 = Employee("Antony", "Walker")
print("John Smith: ", emp_1.fullname)
print("mary.sue@company.com: ", emp_2.email)
print("Antony: ", emp_3.firstname)

# 5. Create a class that takes the following four arguments for a particular
#     football player:
#    - name
#    - age
#    - height
#    - weight
#     Also, create three instance methods for the class that returns the
#     following strings:
#    - get_age() returns "<name> is age <age>"
#    - get_height() returns "<name> is <height>cm"
#    - get_weight() returns "<name> weighs <weight>kg"
class Player():
    def __init__(this, name, age, height, weight):
        this.name = name
        this.age = age
        this.height = height
        this.weight = weight

    def get_age(this):
        return f"{this.name} is {this.age} years old"
    
    def get_height(this):
        return f"{this.name} is {this.height}cm"
    
    def get_weight(this):
        return f"{this.name} weighs {this.weight}kg"
    
#    EXAMPLES:
#     p1 = Player("David Jones", 25, 175, 75)
#     p1.get_age()  # => "David Jones is age 25"
#     p1.get_height()  # => "David Jones is 175cm"
#     p1.get_weight()  # => "David Jones weighs 75kg"
p1 = Player("David Jones", 25, 175, 75)
print("David's age: ", p1.get_age())
print("David's height: ", p1.get_height())
print("David's weight: ", p1.get_weight())