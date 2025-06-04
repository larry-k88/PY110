# Given a string of words separated by spaces, write a function that
# swaps the first and last letters of every word.

# You may assume that every word contains at least one letter, and that
# the string will always contain at least one word. You may also assume
# that each string contains nothing but words and spaces, and that there
# are no leading, trailing, or repeated spaces.

'''
Problem:

    - Swap the first and last letters of every word in a string of words

    - Input - string 
    - Output - string
     
    - Explicit requirements:
        - Each word has length at least 1
        - Each string will have at least one word
        - Strings contain only words and single spaces
    - Implicit requirements:
        - Case is important
    - Questions
        - Words with punctuation?

Examples/Test Cases:
    - print(swap('Oh what a wonderful day it is')
            == "hO thaw a londerfuw yad ti si")  # True
    - print(swap('Abcde') == "ebcdA")            # True
    - print(swap('a') == "a")                    # True

Data Structure:
    - Convert to a list using `split()`
    - Index into the words in the list
    - use `join()` to combine changed words in the list
  

Algorithm:  

    - Split phrase into a list of words
    - Iterate over the words:
        - Index the first and last letters
        - Build the new string (string concat)
    - Join the list of words together

'''
def swap(phrase):
    list_of_words = phrase.split()
    altered_word = [word if len(word) ==1 else word[-1] + word[1:-1] + word[0]
                     for word in list_of_words]
    return ' '.join(altered_word)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True