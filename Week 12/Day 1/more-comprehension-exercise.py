# Generate your own lists of numbers, sentences, and strings for these
#  exercises and use several permutations to verify that they work
#  as intended!

# 1. Given a list of numbers, write a list comprehension that produces a
#     list of strings of each number that is divisible by 5.
def list_of_nums_div_by_5(num_list):
    return [str(num) for num in num_list if num % 5 == 0]
print(list_of_nums_div_by_5([2,5,10,1,7]))

# 2. Given a sentence, produce a list of the lengths of each word in the
#     sentence, but only if the word is not 'the'.
def length_of_sentence(sentence):
    return [len(word) for word in sentence.lower().split() if "the" != word]

print("Hello world!: ", length_of_sentence("Hello world!"))
print("The boy ate meat: ", length_of_sentence("The boy ate meat"))

# 3. Given a string representing a word, write a list comprehension that
#     produces a list of all the vowels in that word.
random_string = "I am a random sentence, and I have no purpose"

vowels_in_random_string = [letter for letter in random_string.lower() if letter in "aeiou"]
print("List of vowels in random string: ", vowels_in_random_string)

# 4. Given a string representing a word, write a set comprehension that
#     produces a set of all the vowels in that word.
set_of_vowels_in_random_string = set([letter for letter in random_string.lower() if letter in "aeiou"])
print("Set of vowels: ", set_of_vowels_in_random_string)

# 5. Given a sentence, return the sentence with all vowels removed.
random_string_no_vowels = [letter for letter in random_string.lower() if letter not in "aeiou"]
print("Sentence of no vowels: ", "".join(random_string_no_vowels))

# 6. Given a list of numbers, return the list with all even numbers doubled,
#     and all odd numbers turned negative.
random_list_nums = [1,2,3,4,5,6,7,8]
even_odd_calc_list = [num*2 if num % 2 == 0 else num*-1 for num in random_list_nums]
print(even_odd_calc_list)

# 7. Given a sentence, return a new sentence with all its letters transposed
#     by 1 letter right in the alphabet, but only if the new letter is
#     between b and y, inclusive.
alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","z","y","z"]

def return_new_sent(sentence):
    letter_list = [letter for letter in sentence.lower()]
    for i in range(0,len(letter_list)):
        for j in range(0,len(alphabet_list)-1):
            if letter_list[i] == alphabet_list[j] and letter_list[i] != "y":
                letter_list[i] = alphabet_list[j+1]
                break
    return "".join(letter_list)

print(return_new_sent("Carry out a random act of kindness, with no expectation of reward, safe in the knowledge that one day someone might do the same for you."))

sentence = "Carry out a random act of kindness, with no expectation of reward, safe in the knowledge that one day someone might do the same for you."
alphas = "abcdefghijklmnopqrstuvwxy"
print("".join([alphas[alphas.index(letter)+ 1] if letter in alphas and letter != "y" else letter for letter in sentence.lower()]))


# 8. Given a list of floats and ints, remove the floats (numbers with decimals).
list_of_floats_ints = [1.1, 2, 3.5, 2.0, 9, 10]
return_ints = [num for num in list_of_floats_ints if isinstance(num,int)]
print("All integers: ", return_ints)