# Write a function that takes a string as an argument and returns that
# string with every occurrence of a "number word" -- 'zero', 'one',
# 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' --
# converted to its corresponding digit character.

# You may assume that the string does not contain any punctuation.

'''
Problem:

  - Take a string argument and output a string but with any 'number
  word' changed to a digit

     
  - Explicit requirements:
      - Argument has no punctuation
  - Implicit requirements:
      - 
  - Questions
      - 

Examples/Test Cases:
    - message = 'Please call me at five five five one two three four'
    - print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
    - # Should print True

Data Structure:
  - Input: string
  - Output: string
    
  - Intermediate: list (to iterate over), dict to access the values, 
  list comp to build the output

High-level strategies:
  - Set a dictionary with number words as keys and corresponding digits
  as value (digits are strings); split the string and iterate over the
  words, append to the output if the string is a key; if not, append the
  word

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - Set dictionary with key/value pairs
  - Split the string into a list of words
  - Iterate over the list of words:
    - If the word is in the dict, value to list
    - If not, append the word
  - Join the list and return

'''
import string

NUMBER_WORDS = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def word_to_digit(message):
    processed_words = [NUMBER_WORDS.get(word, word)
                    for word in message.split()]
    return ' '.join(processed_words)

'''
Can you solve this problem if the individual words can end with
punctuation?
'''
def word_to_digit_2(message):
    processed_words = []
    for word in message.split():
        ending = ''
        if word[-1] in string.punctuation:
            ending = word[-1]
            word = word[:-1]
        processed_words.append(NUMBER_WORDS.get(word, word) + ending)

    return ' '.join(processed_words)

# def word_to_digit_2(message):
#     punctuation = string.punctuation
#     processed_words = [NUMBER_WORDS.get(word.rstrip(punctuation), word)
#                     for word in message.split()]
#     return ' '.join(processed_words)

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit_2(message))

print(word_to_digit_2('one, two'))