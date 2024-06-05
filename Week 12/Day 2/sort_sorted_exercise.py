from random import randint

# 1. Sort this list of people by age in ascending order without
#     changing the list.
people = [
  {'name': 'Jim', 'salary': 1_000, 'age': 30},
  {'name': 'Bob', 'salary': 2_000, 'age': 260},
  {'name': 'Anne', 'salary': 3_000, 'age': 123},
]

def sort_by_age(list):
  return list['age']

sorted_list_by_age = sorted(people, key = sort_by_age)
print("1A: ", sorted_list_by_age)

#    b. Sort by salary in descending order without changing the list.
def sort_by_salary(list):
  return list["salary"]

sorted_list_by_salary_reversed = sorted(people, key = sort_by_salary, reverse = True)
print("1B: ", sorted_list_by_salary_reversed)

#    c. Sort by their names in ascending order in a way that
#        modifies the list.
def sort_by_name(list):
  return list["name"]

people.sort(key = sort_by_name)
print("1C: ", people)

# 2. Fill in the missing items in the constructor for the following class.
class Monster:
  def __init__(self, speed, height, health):
    # Fill in here!
    self.speed = speed
    self.height = height
    self.health = health
  
  # Special dunder function used when converting this object into a string
  # For example, when printing. This function will be called.
  # Similar to __str__, too. You can think of the two as:
  # __repr__ for developers (debugging or logging)
  # __str__ for users (UI and reports)
  def __repr__(self):
    desc = f'Monster: speed->{self.speed}, '
    desc += f'height->{self.height}, '
    desc += f'health->{self.health}, '
    return desc

m1 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))
m2 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))
m3 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))
m4 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))

monsters = [m1, m2, m3, m4]

#    b. Sort this list of monsters by speed in ascending order without
#        changing the list.
for monster in monsters:
  print("2A: ", monster)

# sorted_by_speed = sorted(monster.speed for monster in monsters)
sorted_by_speed = sorted(monsters, key = lambda monster: monster.speed)
print("2B: ", sorted_by_speed)

#    c. Sort this list of monsters by height in descending order
#        without changing the list.
# sorted_by_height = sorted((monster.height for monster in monsters),reverse=True)
sorted_by_height = sorted(monsters, key = lambda monster: monster.height, reverse = True)
print("2C: ", sorted_by_height)

#    d. Sort this list of monsters by health in ascending order
#        without changing the list.
# sorted_by_health = sorted(monster.health for monster in monsters)
sorted_by_health = sorted(monsters, key = lambda monster: monster.health)
print("2D: ", sorted_by_health)

#    e. Sort this list of monsters by their health x height in
#        ascending order and modify the original list.
monster_height_squared = [(i,monster.health * monster.height) for i,monster in enumerate(monsters)]
monster_height_squared.sort(key=lambda m:m[1])
new_list = []
for m in monster_height_squared:
  new_list.append(monsters[m[0]])
print("2E: ", new_list)
