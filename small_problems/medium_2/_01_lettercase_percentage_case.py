# Write a function that takes a string and returns a dictionary
# containing the following three properties:

# the percentage of characters in the string that are lowercase letters
# the percentage of characters that are uppercase letters
# the percentage of characters that are neither
# All three percentages should be returned as strings whose numeric
# values lie between "0.00" and "100.00", respectively. Each value
# should be rounded to two decimal points.

# You may assume that the string will always contain at least one
# character.

'''
Problem:

  - Take a string and calculate the percentage of uppercase, lowercase
    and neither (i.e. the rest)

     
  - Explicit requirements:
      - Percentage is between 0.00 and 100.00 but returned as a string
      - All rounded to 2 dp
      - String will have length at least 1
  - Implicit requirements:
      - The 3 percentages should equal 100%
  - Questions
      - 

Examples/Test Cases:
  - See below

Data Structure:
  - Input: string
  - Output: dictionary
    
  - Intermediate: 

High-level strategies:
  - Determine the overall length, number of uppercase and lowercase
    letters,then calculate the percentages and return them as a
    dictionary

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - Get the length of the string
  - Iterate over the string and count the uppercase, lowercase and neither
  - Calculate % of each by dividing the counts by the length * 100
  - Put each into a dictionary and return

'''

def percentage(value, total):
    return f'{(value / total) * 100:.2f}'

def letter_percentages(string):
    string_length = len(string)
    upper = 0
    lower = 0

    for char in string:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1

    neither = string_length - upper - lower

    return {'lowercase': percentage(lower, string_length),
            'uppercase': percentage(upper, string_length),
            'neither': percentage(neither, string_length),
    }

print(letter_percentages('abCdef 123'))

print(letter_percentages('AbCd +Ef'))

print(letter_percentages('123'))