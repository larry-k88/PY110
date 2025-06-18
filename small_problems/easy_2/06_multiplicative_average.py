# Write a function that takes a list of positive integers as input,
# multiplies all of the integers together, divides the result by the
# number of entries in the list, and returns the result as a string with
# the value rounded to three decimal places.

'''
Problem:

    - Calculate the product of the integers in the list, divide by the 
    length and round to 3dp before returning the str rep of the value

    - Input - list of integers
    - Output - string
     
    - Explicit requirements:
        - All list elements are positive integers
        - Rules:
            - Product of all integers
            - Divide by the length of the list
            - Round to 3dp
    - Implicit requirements:
        - 
    - Questions
        - 

Examples/Test Cases:
    - print(multiplicative_average([3, 5]) == "7.500")
    - print(multiplicative_average([2, 5, 8]) == "26.667")
    - print(multiplicative_average([2, 5]) == "5.000")
    - print(multiplicative_average([1, 1, 1, 1]) == "0.250")
    - print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

Data Structure:
    - Maybe helper function - product
    - f-strings to round
    - str()      

Algorithm:  

    - For item in the list:
        - Multiply by the previous
    - Divide by the length
    - Format the f-string output

'''
def multiplicative_average(lst):
    product = 1
    for num in lst:
        product *= num
    product_average = product / len(lst)
    return f'{product_average:.3f}'

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")