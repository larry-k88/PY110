# Write a function that takes a positive integer as an argument and
# returns that number with its digits reversed.

'''
Problem:

  - Reverse the digits which are provided in the argument

     
  - Explicit requirements:
      - Integer will be positive
  - Implicit requirements:
      - Any argument with only 1 digit will return that digit
      - Any leading zeros in the output should be ignored (int function)
  - Questions
      - 

Examples/Test Cases:
    - print(reverse_number(12345) == 54321)   # True
    - print(reverse_number(12213) == 31221)   # True
    - print(reverse_number(456) == 654)       # True
    - print(reverse_number(1) == 1)           # True
    - print(reverse_number(12000) == 21)      # True

Data Structure:
  - Input: integer
  - Output: integer
    
  - Intermediate: strings/lists in order to reverse, then int() function

High-level strategies:
  - Convert the number to a string, reverse it, convert back to int

  - Convert number to a list of digits, reverse it, join and remove
  leading 0s

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  - Set number_string to str(num)
  - Reverse the string and convert to int

'''
def reverse_number(num):
    return int(str(num)[::-1])

# def reverse_number(num):
#     number_list = [digit for digit in str(num)]
#     return int(''.join((list(reversed(number_list)))))

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True