# A triangle is classified as follows:

# Equilateral: All three sides have the same length.
# Isosceles: Two sides have the same length, while the third is
# different.
# Scalene: All three sides have different lengths.

# To be a valid triangle, the sum of the lengths of the two shortest
# sides must be greater than the length of the longest side, and every
# side must have a length greater than 0. If either of these conditions
# is not satisfied, the triangle is invalid.

# Write a function that takes the lengths of the three sides of a
# triangle as arguments and returns one of the following four strings
# representing the triangle's classification: 'equilateral', 'isosceles',
# 'scalene', or 'invalid'.

 
'''
Problem:

  - Take 3 lengths and determine what sort of triangle it is based on 
  certain rules; if it doesn't adhere to another set of rules, it is
  invalid
     
  - Explicit requirements:
      - All lengths must be > 0 (if not, invalid)
      - When put in ascending order, the sum of the first 2 must be > the
      third (if not, invalid)
      - All lengths are different - scalene
      - Two are the same, one is different - isosceles
      - All three are the same - equilateral
  - Implicit requirements:
      - 
  - Questions
      - 

Examples/Test Cases:
    - print(triangle(3, 3, 3) == "equilateral")  # True
    - print(triangle(3, 3, 1.5) == "isosceles")  # True
    - print(triangle(3, 4, 5) == "scalene")      # True
    - print(triangle(0, 3, 3) == "invalid")      # True
    - print(triangle(3, 1, 1) == "invalid")      # True

Data Structure:
  - Input: 3 numbers (int or float)
  - Output: One of 4 strings
    
  - Intermediate: 

High-level strategies:
  - Sort the argument in place and check the validation rules; any that 
  pass should be checked against the triangle rules and the suitable 
  string returned

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - Get a list of the arguments and sort them in place
  - If shortest is <= 0 or the sum of first 2 <= third, invalid
  - If all are the same - equilateral
  - If any two are the sane - isosceles
  - Else - scalene

'''

def triangle(a, b, c):
    shortest, middle, longest = sorted([a, b, c])
    if shortest <= 0 or shortest + middle <= longest:
        return 'invalid'
    if shortest == middle == longest:
        return 'equilateral'
    if shortest == middle or middle == longest:
        return 'isosceles'
    return 'scalene'

print(triangle(3, 3, 3)) # "equilateral"
print(triangle(3, 3, 1.5)) # "isosceles"
print(triangle(3, 4, 5)) # "scalene"
print(triangle(0, 3, 3)) # "invalid"
print(triangle(3, 1, 1)) # "invalid"