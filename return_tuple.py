"""
A python program that returns a tuple containing a new string
made of all and only the  vowels from the original  string and
the number of duplicates in the original string
"""
from collections import OrderedDict

def count_vowels(string):
    "A python method to returns a tuple"
    string = string.lower()
    string = string.replace(' ', '')
    vowel = "aeiou"

    #getting the first tupple
    final = [each for each in string if each in vowel]
    final_join = ''.join(final)
    final_tuple1 = tuple(final_join)
    get_unique_vowels = "".join(OrderedDict.fromkeys(final_tuple1))
    get_unique_vowels_tuple = (get_unique_vowels,)

    #getting the second tupple
    get_dup1_char = [letter for letter in string if string.count(letter) > 1]
    get_unique_char = "".join(OrderedDict.fromkeys(get_dup1_char))
    tuple_dup = tuple(get_unique_char)
    count_tuple_dup = len(tuple_dup)
    count_tuple_dup_final = (count_tuple_dup,)

    #combining the first and second tupple
    combine_tuple = get_unique_vowels_tuple + count_tuple_dup_final
    print(combine_tuple)
    #print(tuple_dup)
    #print(get_dup1_char)

count_vowels('dahdah')
