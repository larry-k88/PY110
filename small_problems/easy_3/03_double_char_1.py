# Write a function that takes a string, doubles every character in the
# string, then returns the result as a new string.

'''
Problem:

  - Double each character of a string

     
  - Explicit requirements:
      - Rules:  New string to be returned
                Every char to be duplicated
  - Implicit requirements:
      - Case of the char being duplicated is relevant
      - Whitespace is a char
  - Questions
      - Multiple Whitespace?

Examples/Test Cases:
    - print(repeater('Hello') == "HHeelllloo")              # True
    - print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
    - print(repeater('') == "")                             # True

Data Structure:
  - Input: string
  - Output: string
    
  - Intermediate: list

High-level strategies:
  - Iterate over the string and build a new string with the char duplicated

  - Convert the string to a list, iterate over it and duplicate the char

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  - Set an empty output string
  - For char in string:
    - Concatenate the char with a duplicate

'''
def repeater(string):
    output = ''
    for char in string:
        output += char * 2
    return output

def repeater(string):
    return ''.join([char * 2 for char in string])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True