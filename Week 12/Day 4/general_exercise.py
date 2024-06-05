# 1. Create a function that always returns True for every item in a given
#     list. However, if an element is the word "flick", switch to always
#     returning the opposite boolean value.
#    EXAMPLES:
#     flick_switch(["edabit", "flick", "eda", "bit"])
#      # => [True, False, False, False]
#     flick_switch(["flick", 11037, 3.14, 53])
#      # => [False, False, False, False]
#     flick_switch([False, False, "flick", "sheep", "flick"])
#      # => [True, True, False, False, True]
def flick_switch(input_list):
    rand_list = []
    bool_value = True
    for item in input_list:
        if item == "flick":
            bool_value = not bool_value
        item = bool_value
        rand_list.append(item)
    return rand_list

#TEST
print("1a: ", flick_switch(["edabit", "flick", "eda", "bit"]))
print("1b: ", flick_switch(["flick", 11037, 3.14, 53]))
print("1c: ", flick_switch([False, False, "flick", "sheep", "flick"]))


# 2. Create a function that ends the first word of a phrase with "ed",
#     essentially verbifying a noun. But, if the word ends with an "e"
#     only end the word with a "d"
#    EXAMPLES:
#     verbify("salt water")  # => "salted water"
#     verbify("cheese burger")  # => "cheesed burger"
#     verbify("orange juice")  # => "oranged juice"
#     verbify("shredd cheese")  # => "shredded cheese"
def verbify(word):
    list_of_word = word.split()
    if list_of_word[0][-1] != "e":
        list_of_word[0] = list_of_word[0] + "ed"
    else:
        list_of_word[0] = list_of_word[0] + "d"
    word = " ".join(list_of_word)
    return word

#TEST
print("2a: ", verbify("salt water"))
print("2b: ", verbify("cheese burger"))
print("2c: ", verbify("orange juice"))
print("2d: ", verbify("shredd cheese"))

# 3. With the following text, create a list of words that fulfill these
#     requirements:
#    - words are at least 2 characters in size.
#    - only include letters -- no punctuation, numbers, and symbols
#    - case-insensitive
pineapple_wiki = '''
The pineapple[2][3] (Ananas comosus) is a tropical plant with an edible fruit; it is the most economically significant plant in the family Bromeliaceae.[4]

The pineapple is indigenous to South America, where it has been cultivated for many centuries. The introduction of the pineapple to Europe in the 17th century made it a significant cultural icon of luxury. Since the 1820s, pineapple has been commercially grown in greenhouses and many tropical plantations.

Pineapples grow as a small shrub; the individual flowers of the unpollinated plant fuse to form a multiple fruit. The plant normally propagates from the offset produced at the top of the fruit[2][5] or from a side shoot, and typically matures within a year.

The pineapple is a herbaceous perennial, which grows to 1.0 to 1.5 m (3 ft 3 in to 4 ft 11 in) tall on average, although sometimes it can be taller. The plant has a short, stocky stem with tough, waxy leaves. When creating its fruit, it usually produces up to 200 flowers, although some large-fruited cultivars can exceed this. Once it flowers, the individual fruits of the flowers join together to create a multiple fruit. After the first fruit is produced, side shoots (called 'suckers' by commercial growers) are produced in the leaf axils of the main stem. These suckers may be removed for propagation, or left to produce additional fruits on the original plant.[5] Commercially, suckers that appear around the base are cultivated. It has 30 or more narrow, fleshy, trough-shaped leaves that are 30 to 100 cm (1 to 3+1⁄2 ft) long, surrounding a thick stem; the leaves have sharp spines along the margins. In the first year of growth, the axis lengthens and thickens, bearing numerous leaves in close spirals. After 12 to 20 months, the stem grows into a spike-like inflorescence up to 15 cm (6 in) long with over 100 spirally arranged, trimerous flowers, each subtended by a bract.

In the wild, pineapples are pollinated primarily by hummingbirds.[2][7] Certain wild pineapples are foraged and pollinated at night by bats.[8] Under cultivation, because seed development diminishes fruit quality, pollination is performed by hand, and seeds are retained only for breeding.[2] In Hawaii, where pineapples were cultivated and canned industrially throughout the 20th century,[9] importation of hummingbirds was prohibited.[10]

The ovaries develop into berries, which coalesce into a large, compact, multiple fruit. The fruit of a pineapple is usually arranged in two interlocking helices, often with 8 in one direction and 13 in the other, each being a Fibonacci number.[11]

The pineapple carries out CAM photosynthesis,[12] fixing carbon dioxide at night and storing it as the acid malate, then releasing it during the day aiding photosynthesis.
'''

pineapple_wiki = pineapple_wiki.strip()
empty_list = []
for letter in pineapple_wiki:
    if letter not in "1234567890-=!@#$%^&*()_+[];',./:<>?|":
        empty_list.append(letter)
empty_list = "".join(empty_list)
empty_list = empty_list.split()

another_empty_list = []

for item in empty_list:
    if len(item) >= 2:
        another_empty_list.append(item.lower())

#    b. Print out the number of total words in your new list.
print("3b: Total number of words - ", len(another_empty_list))

#    c. Print out how many times the word "fruit" appears in the list.
print("3c: Appearance of the word 'fruit' - ", another_empty_list.count("fruit"))

#    d. Print out the number of times the top 10 most frequent words appear
#        in your list, sorted with the most frequest word first.
from collections import Counter
print("3d: Top 10 common words - ", Counter(another_empty_list).most_common(10))