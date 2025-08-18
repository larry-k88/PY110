# Write a function that calculates and returns the index of the first
# Fibonacci number that has the number of digits specified by the
# argument. The first Fibonacci number has an index of 1. You may assume
# that the argument is always an integer greater than or equal to 2.

'''
Problem:

  - Function that returns the first Fibonacci number that has the number
  of digits in the argument, starting at index 1.
  - The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144

     
  - Explicit requirements:
      - Argument will be >= 2
  - Implicit requirements:
      - Start index at 1, not 0
  - Questions
      - 

Examples/Test Cases:
    - print(find_fibonacci_index_by_length(2) == 7)
    - print(find_fibonacci_index_by_length(3) == 12)
    - print(find_fibonacci_index_by_length(10) == 45)
    - print(find_fibonacci_index_by_length(16) == 74)
    - print(find_fibonacci_index_by_length(100) == 476)
    - print(find_fibonacci_index_by_length(1000) == 4782)
    - print(find_fibonacci_index_by_length(10000) == 47847)

Data Structure:
  - Input: integer
  - Output: integer
    
  - Intermediate: will need a list to get the index

High-level strategies:
  - Create a dictionary to track the value of n along with the fib value. 
  Deal with n = 1 and n = 2, 

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - Create empty dict
  - Deal with n = 1 and n = 2: add the values to dict
  - Capture value of fib as 

'''
import sys
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
def find_fibonacci_index_by_length(length):
    sys.set_int_max_str_digits(50000)
    previous, current = 1, 1
    count = 2

    while len(str(current)) < length:
        previous, current = current, previous + current
        count += 1

    return count

print(find_fibonacci_index_by_length(2))          # 7
print(find_fibonacci_index_by_length(3))          # 12
print(find_fibonacci_index_by_length(10))         # 45
print(find_fibonacci_index_by_length(16))         # 74
print(find_fibonacci_index_by_length(100))        # 476
print(find_fibonacci_index_by_length(1000))       # 4782


print(find_fibonacci_index_by_length(10000))    # 47847