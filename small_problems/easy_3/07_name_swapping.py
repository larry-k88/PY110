# Write a function that takes a string argument consisting of a first
# name, a space, and a last name. The function should return a new
# string consisting of the last name, a comma, a space, and the first
# name.

# You may assume that the names don't include middle names, initials, or
# suffixes ("Jr.", "Sr.").

'''
Problem:

  - Convert a string containing a first and last name into one with 
  last name, comma then first name

     
  - Explicit requirements:
      - Argument will be a string only containing 2 names and a space
  - Implicit requirements:
      - The names will not be changed
  - Questions
      - 

Examples/Test Cases:
    - print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

Data Structure:
  - Input: string
  - Output: string
    
  - Intermediate: f-string for the output

High-level strategies:
  - Split the argument and save the first and last names. Then use
  f-strings to format the output

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  - Split argument (by default = whitespace)
  - Set index 0 to the first name and index 1 to the last name
  - Format the output using f-strings

'''

'''def swap_name(name):
    first_name, last_name = name.split()
    return f'{last_name}, {first_name}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True'''

# Further Exploration:
# Suppose the named person has one or more middle names? Refactor the
# current solution so it can accommodate this. The middle names should
# be listed after the first name:

# def swap_name(name):
#     names = name.split()
#     first_name = names[0]
#     last_name = names[-1]
#     middle_names = names[1:-1]
#     if middle_names:
#         return f'{last_name}, {first_name} {' '.join(middle_names)}'
#     return f'{last_name}, {first_name}'

def swap_name(name):
    names = name.split()
    last_name = names.pop()
    return f'{last_name}, {' '.join(names)}'


print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True'