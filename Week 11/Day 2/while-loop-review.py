# 1. Create a movies list containing a single tuple. 
#     The tuple should contain a movie title, the director’s 
#     name, the release year of the movie, and the movie’s budget.
movies_list = [("Interstellar","Christopher Nolan",2014,165_000_000)]

#    b. Use an f-string to print the movie name and release year 
#        by accessing your new movie tuple.
for movie in movies_list:
    for title, director, year, budget, in movies_list:
        print("Title:", title, "Year:", year)

#    c. Add another new movie tuple to the movies collection using append.
movies_list.append(("Martian", "Ridley Scott", 2015, 108_000_000))

#    d. Print both movies in the movies collection.
for title,director,year,budget in movies_list:
    print(title,director,year,budget)


#    e. Remove the first movie from movies.
movies_list.pop(0)
print("Removed Interstellar:", movies_list)

# 2. Below is a list of tuples, where each tuple contains details about an
#     employee of a shop: their name, the number of hours worked last week,
#     and their hourly rate. Print how much each employee is due to be paid
#     at the end of the week in a nice, readable format.
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

average = 0 

for name, hour, rate in employees:
    print(f"Name: {name} Wage: ${hour * rate}")
#    b. For the employees above, print out those who are earning an hourly
#        wage above average.
    average += rate
average = round(average / len(employees),2)
print("AVG rate:", average)

for name, hour, rate in employees:
    if rate > average:
        print("Employees who make more than avg:", name, "makes $",rate)

# 3. Consider the following data structure. Remove all the * that do not have a
#     neighboring *. Then print out the number of *'s that remain.
field = [
    "....**....*..***...*",
    "**..*...**...**.*...",
    "*...***...*...****..",
    "...*********......**",
    "****.........*...***",
    "....*.....*....*...."
]

count = 0

new_list = []

# for row in field:
#     row = row.replace(".*.", "...")
#     row = row[:2].replace("*.","..") + row[2:len(row)-2] + row[-2:].replace(".*","..")
#     for i in range(0,len(row)):
#         if row[i] == "*":
#             count += 1
#     new_list.append(row)

# print(count)
# print(new_list)
    
total_stars = 0

for row in field:
    row = row.replace(".*.", "...")
    if row.find("*.") == 0:
        row = "." + row[1:]
    elif row.find(".*",-2) != -1:
        row = row[:-1] + "."
    total_stars += row.count("*")
    new_list.append(row)
print(new_list)

print("3. Total stars:", total_stars)