# Write a function that takes one argument, a positive integer, and
# returns a list of the digits in the number.

'''
Problem:

    - Take an integer and output a list of numbers in the integer

    - Input - integer
    - Output - list (ordered)
     
    - Explicit requirements:
        - Number will be a positive integer
    - Implicit requirements:
        - Digits need to be in order
    - Questions
        - 

Examples/Test Cases:
    - print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
    - print(digit_list(7) == [7])                       # True
    - print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
    - print(digit_list(444) == [4, 4, 4])               # True

Data Structure:
    - List for the output     

Algorithm:  

    - 
'''
def digit_list(integer):
    str_int = str(integer)
    return [int(num) for num in str_int]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True