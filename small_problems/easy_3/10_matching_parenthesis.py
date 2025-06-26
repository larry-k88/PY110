# Write a function that takes a string as an argument and returns True
# if all parentheses in the string are properly balanced, False
# otherwise. To be properly balanced, parentheses must occur in matching
# '(' and ')' pairs.

# Note that balanced pairs must start with a (, not a ).

'''
Problem:

  - Take a string and return bool depending on whether every `(` is 
  paired with a `)`

     
  - Explicit requirements:
      - If the first one is `)`, it fails as it can't ever be paired
  - Implicit requirements:
      - Number of open must equal the number of closed
      - None of each is fine
  - Questions
      - The order of the brackets is irrelevant?

Examples/Test Cases:
    - print(is_balanced("What (is) this?") == True)        # True
    - print(is_balanced("What is) this?") == False)        # True
    - print(is_balanced("What (is this?") == False)        # True
    - print(is_balanced("((What) (is this))?") == True)    # True
    - print(is_balanced("((What)) (is this))?") == False)  # True
    - print(is_balanced("Hey!") == True)                   # True
    - print(is_balanced(")Hey!(") == False)                # True
    - print(is_balanced("What ((is))) up(") == False)      # True

Data Structure:
  - Input: string
  - Output: Boolean
    
  - Intermediate: 

High-level strategies:
  - Track open and closed with integers - +1 for open, -1 for closed
  - Iterate through the string and update the value with each char, if
  it's ever negative, ) precedes ( so would be False.


Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
    - Set value to 0
    - Iterate over the chars and +1 for `(` and -1 for `)`
    - Check if value is negative, if so, return False

'''

def is_balanced(string): # from LS
    value = 0
    for char in string:
        if char == '(':
            value += 1
        elif char == ')':
            value -= 1
        if value < 0:
            return False
        
    return value == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
