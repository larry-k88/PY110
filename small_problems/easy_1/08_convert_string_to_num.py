# Write a function that takes a string of digits and returns the
# appropriate number as an integer. You may not use any of the standard
# conversion functions available in Python, such as int. Your function
# should calculate the result by using the characters in the string.

# For now, do not worry about leading + or - signs, nor should you worry
# about invalid characters; assume all characters are numeric.

'''
Problem:

    - Perform the operation that `int(numeric_string)` does without 
    using the int function

    - Input - numeric string
    - Output - integer
     
    - Explicit requirements:
        - Assume correct input - numeric string
        - Ignore leading + or - signs
    - Implicit requirements:
        - 
    - Questions
        - 

Examples/Test Cases:
    - print(string_to_integer("4321") == 4321)  # True
    - print(string_to_integer("570") == 570)    # True

Data Structure:
    - Convert to a list
    - Dictionary
    - If/else structure


Algorithm:  

    - Create a dictionary mapping numbers to their string equivalents
    - SET power = 0
    - Iterate over the string in reverse 
        - GET numeric equivalent of last digit
        - Multiply by 10**power
        - Increment power
     
'''

'''def string_to_integer(numeric_string):
    MAPPING = {
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
    power = 0
    value = []
    for char in numeric_string[::-1]:
        value.append(MAPPING[char] * (10 ** power))
        power += 1

    return sum(value)

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True'''

def hexadecimal_to_integer(numeric_string):
    MAPPING = {
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
        'A' : 10,
        'B' : 11,
        'C' : 12,
        'D' : 13,
        'E' : 14,
        'F' : 15, 
    }

    value = 0
    for char in numeric_string.upper():
        value = (16 * value) + MAPPING[char]

    return value

print(hexadecimal_to_integer("4D9f") == 19871)  # True
print(hexadecimal_to_integer("2f") == 47)  # True
