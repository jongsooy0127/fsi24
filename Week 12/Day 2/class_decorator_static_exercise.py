import random
#================================MODULE IMPORT==============================

# Create a class called Country that has properties for name, population,
# language, and in_europe. Make sure that 'name' is always has a value,
# and 'population' can not be set to a number less than 0. The 'in_europe'
# property must be a boolean and defaults to False. Only the 'language'
# property can be deleted from a Country object.
class Country:
    terrain = "land"

    def __init__(self, name, population, language, in_europe = False):
        self._name = name
        self.population = population
        self._language = language
        self.in_europe = False

    def growpop(self, rate):
        if -1 <= rate <= 1:
            return int((self.population * rate) + self.population)
        
    def grow_pop_after_years(self, year):
        population = self.population
        for i in range(year):
            population += population * random.uniform(-.001,.023)
        return int(population)
   
    def show_lore(self):
        return f"{self.name} is a {self.terrain}-based entity with {self.population} souls"
    
    @property
    def population(self):
        return self._population
    @population.setter
    def population(self, num):
        if num > 0:
            self._population = int(num)
        else: print("Input an integer greater than 0")
    
    @population.deleter
    def population(self):
        print("You can't delete the population data")

    @property
    def in_europe(self):
        return self._in_europe
    @in_europe.setter
    def in_europe(self, in_europe):
        if isinstance(in_europe,bool):
            self._in_europe = bool(in_europe)
        else: print("Input a boolean value")
    @in_europe.deleter
    def in_europe(self):
        print("You can't delete the in_europe data")

    @property
    def name(self):
        return self._name
    @name.deleter
    def name(self):
        print("You can't delete the name data")

    @property
    def language(self):
        return self._language
    @language.deleter
    def language(self):
        del self._language

# Add the appropriate getters and setters for the behavior outlined above,
# and add an additional method called 'grow_pop' that accepts a 'rate'
# argument that will accept a float between -1 and 1 and change the
# Country object's population appropriately.
# EXAMPLE (assume 'spain' is a Country object with population of 1000):
# spain.grow_pop(0.05)  # spain's population is now 1050

# Also include a 'show_lore' function for each object that prints out
# a string in the following format: "<coutry name> is a <terrain>-based
# entity with <population> souls."

# All Country objects share a 'terrain' property set to the string "land".
# Create a method that is shared by all the objects called 'show_kind'
# that prints out "All countries are based on " followed by the current
# value of the 'terrain' property.

# Create at least 5 countries of your choosing, with at least 3 of them
# being in Europe, with the appropriate properties.
south_korea = Country("South Korea", 51_000_000, "Korean")
france = Country("France", 67_000_000, "French", True)
italy = Country("Italy", 58_000_000, "Italian", True)
united_states = Country("United States of America", 333_000_000, "English")
greece = Country("Greece", 10_000_000, "Greek", True)

# Simulate 1000 years of passing time by adjusting each countries'
# population with a random growth rate annually. Then print out each
# country and their resulting population in the following format:
#  === Population after 1000 years ===
#  <country1 name>: <country1 population>
#  <country2 name>: <country2 population>
#  ... etc.
print("South Korea: ",south_korea.grow_pop_after_years(1000))
print("France: ", france.grow_pop_after_years(1000))
print("Italy: ", italy.grow_pop_after_years(1000))
print("Greece: ", greece.grow_pop_after_years(1000))
print("United States: ", united_states.grow_pop_after_years(1000))

# Call 'show_lore' for the country with the highest population.
print("USA LORE:", united_states.show_lore())

# Then call 'show_lore' for only those countries that are in Europe, that
# still have a population greater than the population they started with
# 1000 years ago.


# Set the terrain property of the Country class to "water" and call 'show_lore'
# with the last country you created. Did it get updated appropriately? Can you
# set just the last country's terrain property to 'fire'? Call the 'show_kind'
# method to show the current value of the terrain for the class to confirm
# that the class is still set to "water".
Country.terrain = "water"
united_states.terrain = "fire"

print(south_korea.terrain)
print(united_states.terrain)