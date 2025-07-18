# Write a function that takes a list of integers between 0 and 19 and
# returns a list of those integers sorted based on the English word for
# each number:

# zero, one, two, three, four, five, six, seven, eight, nine, ten,
# eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen,
# eighteen, nineteen"

'''
Problem:

  - Take a list of integers (0-19) and sort them alphabetically (when
  written out in English)
     
  - Explicit requirements:
      - Must return the list of integers
      - spelling are given above
  - Implicit requirements:
      - Case-insensitive
  - Questions
      - Do we need to keep the original, or can we mutate it?

Examples/Test Cases:
    - input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                  10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    
    - expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                        7, 17, 6, 16, 10, 13, 3, 12, 2, 0]
    
    - print(alphabetic_number_sort(input_list) == expected_result) #True


Data Structure:
  - Input: list of integers
  - Output: list of integers (same or different)
    
  - Intermediate: 

High-level strategies:
  - Sort the input list using a key - the key acts on each element and 
  therefore needs to return the string word representing the number. The 
  sort/sorted function will then put them in alphabetical order based on 
  those strings.
  - Helper function needed to return the word related to each number

Algorithm:  

    - Helper function: Takes a number and returns the written version of it
        - either use a dict: {0: 'zero'}, or
        - just use a list: 'zero' is in position 0 anyway
        - (LSBot suggests using a tuple as they won't change)
    - Need to create the tuple from the string of words, using split()
    - Pass in the input list, using the helper as the key

'''
numbers = "zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen"
NUMBERS_TUP = tuple(numbers.split(', '))

def word_for_number(item):
    return NUMBERS_TUP[item]

def alphabetic_number_sort(int_list):
    return sorted(int_list, key=word_for_number)

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
