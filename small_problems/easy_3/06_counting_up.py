# Write a function that takes an integer argument and returns a list
# containing all integers between 1 and the argument (inclusive), in
# ascending order.

# You may assume that the argument will always be a positive integer.

'''
Problem:

  - Print a list containing integers from 1 up to and including the 
  value of the argument

     
  - Explicit requirements:
      - Argument will be a positive integer
  - Implicit requirements:
      - 
  - Questions
      - Is this the same as list(range(1, x + 1))?

Examples/Test Cases:
    - print(sequence(5) == [1, 2, 3, 4, 5])   # True
    - print(sequence(3) == [1, 2, 3])         # True
    - print(sequence(1) == [1])               # True

Data Structure:
  - Input: integer
  - Output: list of integers (ascending)
    
  - Intermediate: 

High-level strategies:
  - Recognise that this is a list of a range, from 1 to n + 1

  - Set a counter to 1, add it to list and increment it until counter 
  = argument

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  - list(range(1, num + 1))

  - Set counter = 1
  - Set output = []
  - If count not equal to num:
    - append counter
    - increment counter
    return output

'''
def sequence(num):
    return list(range(1, num + 1))


def sequence(num):
    output = []
    counter = 1
    while counter <= num:
        output.append(counter)
        counter += 1

    return output

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True