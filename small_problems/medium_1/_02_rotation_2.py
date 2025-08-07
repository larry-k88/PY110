# Write a function that rotates the last `count` digits of a `number`.
# To perform the rotation, move the first of the digits that you want to
# rotate to the end and shift the remaining digits to the left.

'''
Problem:

  - Take a number and move the digit that is `count`-th from the end to
  the end
     
  - Explicit requirements:
      - if 2 is the count, the number 2nd from the end needs to become 
      the last digit
  - Implicit requirements:
      - Integers are immutable so a new object will be returned
      - `-count` is the index position of the number we want to move
  - Questions
      - How to deal with negative values of `count`?

Examples/Test Cases:
    - print(rotate_rightmost_digits(735291, 2) == 735219)
    - print(rotate_rightmost_digits(735291, 3) == 735912)
    - print(rotate_rightmost_digits(735291, 1) == 735291)
    - print(rotate_rightmost_digits(735291, 4) == 732915)
    - print(rotate_rightmost_digits(735291, 5) == 752913)
    - print(rotate_rightmost_digits(735291, 6) == 352917)
    - print(rotate_rightmost_digits(1200, 3) == 1002)    

Data Structure:
  - Input: 2 integers
  - Output: 1 integer
    
  - Intermediate: convert to string (or list of digits)

High-level strategies:
  - Convert the `count` to an index, convert to string, then return a sliced
  string 

  - Convert int to string, then enumerate the list in order to rebuild the
  sting, then convert back to an integer

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo

  - Convert the integer to a string and note the index we need to move 
  is `number[-count]`.
  - Rebuild the string using slices
  - Convert back to int

'''

# my answer, but didn't use previous function
'''
def rotate_rightmost_digits(number, count):
    if count == 1:
        return number
    
    num_str = str(number)
    str_result = num_str[:-count] + num_str[-count + 1:] + num_str[-count]
    return int(str_result)
'''

# using previous function
def rotate_list(lst):
    if not isinstance(lst, list):
        return None
    
    result = lst[1:] + lst[:1]
    
    return result

def rotate_rightmost_digits(number, count):
    num_list = list(str(number))
    first_part = num_list[:-count]
    second_part = num_list[-count:]

    return int(''.join(first_part + rotate_list(second_part)))