# Write a function that takes a string and returns the length of the
# longest substring without repeating characters.

'''
Problem:

  - Return the longest substring from a string that doesn't contain any
  characters that have appeared before

  - Explicit requirements:
      - Rules
  - Implicit requirements:
      - 
  - Questions
      - 

Examples/Test Cases:
    - print(length_of_longest_substring("abcabcbb"))  # Expected output: 3 (for "abc")
    - print(length_of_longest_substring("bbbbb"))     # Expected output: 1 (for "b")
    - print(length_of_longest_substring("pwwkew"))    # Expected output: 3 (for "wke")
    - print(length_of_longest_substring(""))          # Expected output: 0
    - print(length_of_longest_substring(" "))         # Expected output: 1

Data Structure:
  - Input: 
  - Output:
    
  - Intermediate: 

High-level strategies:
  - Iterate over all the substrings and add them to a list, unless they
   have duplicate letters, in which case, ignore them. Then return the max

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - Helper function to generate the substrings
  - substrings = []
    - for char in string:
        - append string[char:len(string)]

  - Set substring_lengths = []
  - Iterate over the substrings
  - If the len(set(substring)) < len(substring):
    - pass
  - Else:
    - append the len(substring) to substring_lengths
  - Return the max(substring_lengths)


'''

def get_substrings(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i + 1,len(string) + 1):
            substrings.append(string[i:j])
    
    return set(substrings)

def length_of_longest_substring(string):
    max_substring_length = 0
    for substring in get_substrings(string):
        if len(set(substring)) < len(substring):
            continue
        elif len(substring) > max_substring_length:
            max_substring_length = len(substring)

    return max_substring_length

print(length_of_longest_substring("abcabcbb"))  # Expected output: 3 (for "abc")
print(length_of_longest_substring("bbbbb"))     # Expected output: 1 (for "b")
print(length_of_longest_substring("pwwkew"))    # Expected output: 3 (for "wke")
print(length_of_longest_substring(""))          # Expected output: 0
print(length_of_longest_substring(" "))         # Expected output: 1