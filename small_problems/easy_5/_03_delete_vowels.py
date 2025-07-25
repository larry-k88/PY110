# Write a function that takes a list of strings and returns a list of
# the same string values, but with all vowels (a, e, i, o, u) removed.

VOWELS = 'aeiou'

def remove_vowels(list_of_strings):
    return [strip_vowels(word) for word in list_of_strings]

def strip_vowels(word):
    return ''.join([char for char in word if char.casefold() not in VOWELS])
