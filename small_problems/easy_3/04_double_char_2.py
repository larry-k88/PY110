# Write a function that takes a string, doubles every consonant in the
# string, and returns the result as a new string. The function should
# not double vowels ('a','e','i','o','u'), digits, punctuation, or
# whitespace.

# You may assume that only ASCII characters will be included in the
# argument.

'''
Problem:

  - Double each character of a string but only if it's a consonant 

     
  - Explicit requirements:
      - Only consonants do be doubled
      - Only ASCII chars will be in the argument
  - Implicit requirements:
      - 
  - Questions
      - 

Examples/Test Cases:
    - # All of these examples should print True
    - print(double_consonants('String') == "SSttrrinngg")
    - print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
    - print(double_consonants('July 4th') == "JJullyy 4tthh")
    - print(double_consonants('') == "")

Data Structure:
  - Input: string (ASCII)
  - Output: string with consonants doubled
    
  - Intermediate: list, to be joined 

High-level strategies:
  - Iterate over the chars and duplicate those that are consonants,
  using isalpha() and not in VOWELS

  - List comprehension for the chars that fit the criteria

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  - Set VOWELS to 'aeiou'
  - Join the result of: char * 2 for char in string if consonant, else
    char

'''
VOWELS = 'aeiouAEIOU'

def double_consonants(string):
    return ''.join([char * 2
                    if (char.isalpha() and char not in VOWELS)
                    else char
                    for char in string ])

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")