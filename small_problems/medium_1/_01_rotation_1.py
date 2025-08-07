# Write a function that rotates a list by moving the first element to the
# end of the list. Do not modify the original list; return a new list
# instead.

# If the input is an empty list, return an empty list.
# If the input is not a list, return None.
# Review the test cases below, then implement the solution accordingly.

'''
Problem:

  - Take a list and move the first element to the end - original list
  must not be mutated.

     
  - Explicit requirements:
      - Element at index 0 moved to index -1
      - Empty lists return empty lists
      - If not list, return None
  - Implicit requirements:
      - 
  - Questions
      - 

Examples/Test Cases:
    - print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
    - print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
    - print(rotate_list(['a']) == ['a'])
    - print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
    - print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
    - print(rotate_list([]) == [])

    - print(rotate_list(None) == None)
    - print(rotate_list(1) == None)

Data Structure:
  - Input: list (if not, return None)
  - Output: new list
    
  - Intermediate: 

High-level strategies:
  - Create a new list and populate it with all elements other than the 
  first, then add the first one to that list.

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo

  - Check the argument type, return None if not a list
  - Create a new list and add elements from index 1 to the end.
  - Add element 0 to the list

'''

def rotate_list(lst):
    if not isinstance(lst, list): # better than checking using `type()`
        return None
    
    result = lst[1:] + lst[:1]
    
    return result

