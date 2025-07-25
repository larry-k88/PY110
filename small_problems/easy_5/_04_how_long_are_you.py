# Write a function that takes a string as an argument and returns a list
# that contains every word from the string, with each word followed by a
# space and the word's length. If the argument is an empty string or if
# no argument is passed, the function should return an empty list.

# You may assume that every pair of words in the string will be
# separated by a single space.

def word_lengths(words=''):
    if not words:
        return []
    return [f'{word} {len(word)}' for word in words.split()]