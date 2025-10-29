# A featured number (something unique to this exercise) is an odd number
# that is a multiple of 7, with all of its digits occurring exactly once
# each. For example, 49 is a featured number, but 98 is not (it is not
# odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit
# 3 appears twice).

# Write a function that takes an integer as an argument and returns the
# next featured number greater than the integer. Issue an error message
# if there is no next featured number.

# NOTE: The largest possible featured number is 9876543201.

'''
Problem:

  - {Rewrite in own words}

     
  - Explicit requirements:
      - Rules
  - Implicit requirements:
      - 
  - Questions
      - 

Examples/Test Cases:
    - print(next_featured(12) == 21)                  # True
    - print(next_featured(20) == 21)                  # True
    - print(next_featured(21) == 35)                  # True
    - print(next_featured(997) == 1029)               # True
    - print(next_featured(1029) == 1043)              # True
    - print(next_featured(999999) == 1023547)         # True
    - print(next_featured(999999987) == 1023456987)   # True
    - print(next_featured(9876543186) == 9876543201)  # True
    - print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfils those requirements.")
print(next_featured(9876543201) == error)       # True

Data Structure:
  - Input: 
  - Output:
    
  - Intermediate: 

High-level strategies:
  - 

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - 

'''

def next_featured(number):
    pass

print(next_featured(12))
print(next_featured(20))
print(next_featured(21))
print(next_featured(997))
print(next_featured(1029))
print(next_featured(999999))
print(next_featured(999999987))
print(next_featured(9876543186))
print(next_featured(9876543200))

error = ("There is no possible number that "
         "fulfils those requirements.")
print(next_featured(9876543201))