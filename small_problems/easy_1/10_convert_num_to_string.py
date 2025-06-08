# Write a function that converts a non-negative integer value
# (e.g., 0, 1, 2, 3, and so on) to the string representation of that
# integer.

# You may not use any of the standard conversion functions available in
# Python, such as str. Your function should do this the old-fashioned
# way and construct the string by analysing and manipulating the number.

'''
Problem:

    - Function that does the job that `str()` does

    - Input - integer
    - Output - string
     
    - Explicit requirements:
        - Int input will be >= 0
    - Implicit requirements:
        - 
    - Questions
        - 

Examples/Test Cases:
    - print(integer_to_string(4321) == "4321")              # True
    - print(integer_to_string(0) == "0")                    # True
    - print(integer_to_string(5000) == "5000")              # True
    - print(integer_to_string(1234567890) == "1234567890")  # True

Data Structure:
    - divmod() function   

Algorithm:  

    - SET divisor to 1
    - Iterate through the loop the same number of times as the length
        - divmod (input, divisor)
        - append the return value to a list
        - divisor * 10
    - join the list

'''

DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

def integer_to_string(number):
    output = ''
    while number > 0:
        number, remainder = divmod(number, 10)
        output += DIGITS[remainder]

    return output[::-1] or '0'

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True