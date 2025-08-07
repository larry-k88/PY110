# Take the number 735291 and rotate it by one digit to the left, getting
# 352917. Next, keep the first digit fixed in place and rotate the
# remaining digits to get 329175. Keep the first two digits fixed in place
# and rotate again to get 321759. Keep the first three digits fixed in
# place and rotate again to get 321597. Finally, keep the first four
# digits fixed in place and rotate the final two digits to get 321579.
# The resulting number is called the maximum rotation of the original
# number.

# Write a function that takes an integer as an argument and returns the
# maximum rotation of that integer. You can (and probably should) use
# the rotate_rightmost_digits function from the previous exercise.

'''
Problem:

  - Function to take a number and perform (len(number) - 1) rotations on it
  - Rotations: rotate one digit to the left, then keep first digit and 
  rotate the remaining ones etc.

     
  - Explicit requirements:
      - Rotations move the first digit to the end
      - Subsequent rotations perform the same process on gradually 
      smaller integers
  - Implicit requirements:
      - Number of rotations is one fewer than the length of the number
      - No. of digits in input not always the same as output (leading
      zeros will be dropped)
  - Questions
      - 

Examples/Test Cases:
    - print(max_rotation(735291) == 321579)          # True
    - print(max_rotation(3) == 3)                    # True
    - print(max_rotation(35) == 53)                  # True
    - print(max_rotation(8703529146) == 7321609845)  # True
    - 
    - # Note that the final sequence here is `015`. The leading
    - # zero gets dropped, though, since we're working with
    - # an integer.
    - print(max_rotation(105) == 15)                 # True

Data Structure:
  - Input: integer
  - Output: integer
    
  - Intermediate: list or a string (to iterate over)

High-level strategies:
  - Perform a rotation on the integer, and then repeat, having fixed the
    next digit

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - 

'''
def rotate_str(str_segment):
    
    result = str_segment[1:] + str_segment[:1]
    
    return result

def rotate_rightmost_digits(number, count):
    num_list = str(number)
    first_part = num_list[:-count]
    second_part = num_list[-count:]

    return first_part + rotate_str(second_part)

def max_rotation(number):
    str_number = str(number)
    for i in range(len(str_number), 1, -1):
        str_number = rotate_rightmost_digits(str_number, i)

    return int(str_number)

print(rotate_rightmost_digits(12345, 2))