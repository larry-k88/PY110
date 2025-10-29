# Find the Missing Number

# Write a function that takes a list of unique numbers from 1 to n
# (inclusive) with one number missing and returns the missing number.

'''
Problem:

  - Take a list of numbers and determine the missing one and return it

     
  - Explicit requirements:
      - List contains unique numbers
      - Only one element is missing
  - Implicit requirements:
      - Number of items in the list is one fewer than 'n'
      - List is in ascending order
  - Questions
      - 

Examples/Test Cases:
    - print(find_missing_number([1, 2, 4, 5]))  # Expected output: 3
    - print(find_missing_number([1, 3]))        # Expected output: 2
    - print(find_missing_number([1, 2, 3, 4, 5, 6, 7, 8, 10])) # Expected output: 9

Data Structure:
  - Input: List
  - Output: Integer
    
  - Intermediate: Sets - set difference 

High-level strategies:
  - Get sets of the argument and the full set. Then take the difference
  between the two

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - Set the argument as set1
  - Set the full set as set2 (i.e. range(1, len(arg) + 2))
  - Return the set difference as in integer

'''
def find_missing_number(numbers):
    set1 = set(numbers)
    set2 = set(range(1, len(numbers) + 2))
    return (set2 - set1).pop()


print(find_missing_number([1, 2, 4, 5]))  # Expected output: 3
print(find_missing_number([1, 3]))        # Expected output: 2
print(find_missing_number([1, 2, 3, 4, 5, 6, 7, 8, 10])) # Expected output: 9