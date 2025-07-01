# Write a function named join_or that produces the following results:

'''
Problem:

  - Take list and 2 delimiters - return the list as a string with
  delimiter 1 between the last 2 elements, and delimiter 2 between the others

     
  - Explicit requirements:
      - 
  - Implicit requirements:
      - Default delimiter1 is `,` and delimiter 2 is `or`
      - Include the whitespace with the delimiter
      - Empty list returns an empty string
      - Single element returns that element as a string
      - Two elements returns delimiter 2
  - Questions
      - 

Examples/Test Cases:
    - print(join_or([1, 2, 3]))               # => "1, 2, or 3"
    - print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
    - print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
    - print(join_or([]))                      # => ""
    - print(join_or([5]))                     # => "5"
    - print(join_or([1, 2]))                  # => "1 or 2"

Data Structure:
  - Input: list, 2x parameters with defaults
  - Output: string
    
  - Intermediate: a list?

High-level strategies:
  - iterate over the list and add delimiter1 after all but the last 2
  elements, add delimiter 2 after the penultimate, then join()


Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  - Determine the length of the list
  - empty --> empty
  - 1 --> str(element)
  - 2 --> str(element) + delimiter2 (or main code?)
  - 3 -- For each element until len - 2, append the element + delimiter1 to the list
    then append penultimate element and delimiter 2 and last element

'''

def join_or(lst, separator1=', ', separator2='or'):
    match len(lst):
        case 0:
            return ''
        case 1:
            return str(lst[0])
        case 2:
            return f"{lst[0]} {separator2} {lst[1]}"

    first_elements = ''.join([f'{element}{separator1}' for element in lst[0:-1]])
    final_element = f'{separator2} {lst[-1]}'

    return first_elements + final_element


print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"
