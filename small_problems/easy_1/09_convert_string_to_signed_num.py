# In the previous exercise, you developed a function that converts
# simple numeric strings to integers. In this exercise, you're going to
# extend that function to work with signed numbers.

# Write a function that takes a string of digits and returns the
# appropriate number as an integer. The string may have a leading + or
# - sign; if the first character is a +, your function should return a
# positive number; if it is a -, your function should return a negative
# number. If there is no sign, return a positive number.

# You may assume the string will always contain a valid number.

# You may not use any of the standard conversion functions available in
# Python, such as int. You may, however, use the string_to_integer
# function from the previous exercise.

'''
Problem:

    - Perform the operation that `int(numeric_string)` does without 
    using the int function

    - Input - numeric string
    - Output - integer
     
    - Explicit requirements:
        - Assume correct input - numeric string
    - Implicit requirements:
        - 
    - Questions
        - 

Examples/Test Cases:
    - print(string_to_signed_integer("4321") == 4321)  # True
    - print(string_to_signed_integer("-570") == -570)  # True
    - print(string_to_signed_integer("+100") == 100)   # True

Data Structure:
    - Convert to a list
    - Dictionary
    - If/else structure


Algorithm:  

    - Create a dictionary mapping numbers to their string equivalents
    - SET value = 0
    - Iterate over the chars in string
        - GET each digit and add it to (10 x previous value)

     
'''
DIGITS_MAP = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
}

def string_to_integer(numeric_string):
    value = 0
    for char in numeric_string:
        value = (10 * value) + DIGITS_MAP[char]
        
    return value

def string_to_signed_integer(num_string):
    match num_string[0]:
        case '-':
            return -string_to_integer(num_string[1:])
        case '+':
            return string_to_integer(num_string[1:])
        case _:
            return string_to_integer(num_string)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
