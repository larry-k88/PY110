# Create a function that takes two integers as arguments. The first
# argument is a count, and the second is the starting number of a
# sequence that your function will create. The function should return a
# list containing the same number of elements as the count argument. The
# value of each element should be a multiple of the starting number.

# You may assume that count will always be an integer greater than or
# equal to 0. The starting number can be any integer. If the count is 0,
# the function should return an empty list.

'''
Problem:

  - Function returns a list of integers the same length as arg1; and the
  elements in the list are multiples of arg2.

     
  - Explicit requirements:
      - Arg1 is the length of the list
      - Arg2 is the starting number
      - Elements are the index + 1 * arg2
      - arg1 will be greater or equal to 0
      - Arg1 == 0 will return an empty list
  - Implicit requirements:
      - 
  - Questions
      - 

Examples/Test Cases:
    - print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
    - print(sequence(4, -7) == [-7, -14, -21, -28])     # True
    - print(sequence(3, 0) == [0, 0, 0])                # True
    - print(sequence(0, 1000000) == [])                 # True

Data Structure:
  - Input: 2 integers
  - Output: list of integers
    
  - Intermediate: range()

High-level strategies:
  - If count = 0, return []. Otherwise, iterate over range(count) and
  add index +1 * start to the output list

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  - output = []
  - If count != 0:
    - Append (index + 1) * start for range(count)
  - return output

'''
def sequence(count, start):
    return [(i + 1) * start for i in range(count)]


print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True