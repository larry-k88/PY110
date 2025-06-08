# In this exercise, you're going to extend the previous function by
# adding the ability to represent negative numbers as well.

# Write a function that takes an integer and converts it to a string
# representation.

# You may not use any of the standard conversion functions available in
# Python, such as str. You may, however, use integer_to_string from the
# previous exercise.

'''
Problem:

    - Function that does the job that `str()` does but with signs

    - Input - integer
    - Output - string
     
    - Explicit requirements:
        - Int input will be >= 0
    - Implicit requirements:
        - 
    - Questions
        - 

Examples/Test Cases:
    - print(signed_integer_to_string(4321) == "+4321")  # True
    - print(signed_integer_to_string(-123) == "-123")   # True
    - print(signed_integer_to_string(0) == "0")         # True

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

DIGITS =('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

def integer_to_string(number):
    output = ''
    while number > 0:
        number, remainder = divmod(number, 10)
        output += DIGITS[remainder]

    return output[::-1] or '0'

def signed_integer_to_string(number):
    if number == 0:
        return '0'
    elif number < 0:
        return f'-{integer_to_string(-number)}'
    else:
        return f'+{integer_to_string(number)}'
    

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True