# Write a function that converts a dictionary into a list of lists,
# where each inner list contains a key-value pair.

'''
Problem:

  - Convert a dictionary into nested lists with key/pair values as the
  nested lists

     
  - Explicit requirements:
      - Rules
  - Implicit requirements:
      - Empty dict returns empty list
  - Questions
      - 

Examples/Test Cases:
    - print(to_list_of_lists({'a': 1, 'b': 2}))
    - # Expected output: [['a', 1], ['b', 2]]
    - 
    - print(to_list_of_lists({}))
    - # Expected output: []
    - 
    - print(to_list_of_lists({'name': 'John', 'age': 30, 'city': 'New York'}))
    - # Expected output: [['name', 'John'], ['age', 30], ['city', 'New York']]

Data Structure:
  - Input: Dictionary
  - Output: List (nested)
    
  - Intermediate: List comp?

High-level strategies:
  - Iterate over the elements and unpack the dictionary item - append to
a new list

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - Create an empty output list
  - Unpack the items in the dictionary: key:value
  - Convert to a list
  - Append that list to the output
  - Return the output list

'''
def to_list_of_lists(dictionary):
    return [[key, value] for key, value in dictionary.items()]

print(to_list_of_lists({'a': 1, 'b': 2}))
# Expected output: [['a', 1], ['b', 2]]

print(to_list_of_lists({}))
# Expected output: []

print(to_list_of_lists({'name': 'John', 'age': 30, 'city': 'New York'}))
# Expected output: [['name', 'John'], ['age', 30], ['city', 'New York']]
