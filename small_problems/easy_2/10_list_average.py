# Write a function that takes one argument, a list of integers, and
# returns the average of all the integers in the list, rounded down to
# the integer component of the average. The list will never be empty,
# and the numbers will always be positive integers.

'''
Problem:

    - Take the average of a list of positive integers, rounded down to 
    whole number

    - Input - list of integers
    - Output - integer
     
    - Explicit requirements:
        - List will never be empty
        - List will have numbers that are positive
    - Implicit requirements:
        - 
    - Questions
        - 

Examples/Test Cases:
    - print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
    - print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
    - print(average([7]) == 7)                          # True

Data Structure:
    - List
    - sum() function
    - int() function     

Algorithm:  

    - Sum the numbers in the list
    - Divide by the list length
    - return int() of the value

'''
def average(lst):
    return sum(lst) // len(lst) # // better than int()

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True