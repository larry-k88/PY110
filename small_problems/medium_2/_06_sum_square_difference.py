# Write a function that computes the difference between the square of
# the sum of the first `count` positive integers and the sum of the
# squares of the first `count` positive integers

'''
Problem:

  - Function returns the difference between the sum of the digits 
  squared and the sum of the squared digits
     
  - Explicit requirements:
      - Rules
  - Implicit requirements:
      - 
  - Questions
      - 

Examples/Test Cases:
    - print(sum_square_difference(3) == 22)          # True
    - # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

    - print(sum_square_difference(10) == 2640)       # True
    - print(sum_square_difference(1) == 0)           # True
    - print(sum_square_difference(100) == 25164150)  # True

Data Structure:
  - Input: integer
  - Output: integer
    
  - Intermediate: str or list for the digits, list comprehensions

High-level strategies:
  - Convert the digits into a string and assign them to variables; then
  perform the mathematical procedures and return the result

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - Convert the argument into a list of digits
  - Sum the digits and square the result
  - Square the digits and sum them

'''
def sum_square_difference(number):
    nums = range(1, number + 1)
    square_of_sum = sum(nums) ** 2
    sum_of_squares = sum(num ** 2 for num in nums)
    return square_of_sum - sum_of_squares

print(sum_square_difference(3)) # 22
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10)) #2640
print(sum_square_difference(1))# 0
print(sum_square_difference(100)) # 25164150