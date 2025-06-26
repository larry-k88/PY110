# Write a function that takes a list as an argument and reverses its
# elements, in place. That is, mutate the list passed into the function.
# The returned object should be the same object used as the argument.

# You may not use the list.reverse method nor may you use a slice
# ([::-1]).

'''
Problem:

  - Perform the actions of the reverse method, without calling it

     
  - Explicit requirements:
      - Cannot use reverse method or slice
      - List must be mutated
  - Implicit requirements:
      - 
  - Questions
      - 

Examples/Test Cases:
    - list1 = [1, 2, 3, 4]
    - result = reverse_list(list1)
    - print(result == [4, 3, 2, 1])               # True
    - print(list1 is result)                      # True
    - 
    - list2 = ["a", "b", "c", "d", "e"]
    - result2 = reverse_list(list2)
    - print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
    - print(list2 is result2)                     # True
    - 
    - list3 = ["abc"]
    - result3 = reverse_list(list3)
    - print(result3 == ['abc'])                   # True
    - print(list3 is result3)                     # True
    - 
    - list4 = []
    - result4 = reverse_list(list4)
    - print(result4 == [])                        # True
    - print(list4 is result4)                     # True

Data Structure:
  - Input: list
  - Output: reversed list
    
  - Intermediate: 

High-level strategies:
  - Copy the list to another list, clear the first and then append the
  items back to the original

  - Pop() and then insert at position 0

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  - Set a new list to a copy of the original
  - Clear the original list
  - Append each item from the copied list to the original

  - for i in range(length of list):
    - temp_element = pop()
    - lst.insert(0, temp_element)
'''

def reverse_list(lst):
    temp_list = lst.copy()
    lst.clear()
    for i in range(len(temp_list) - 1, -1, -1):
        lst.append(temp_list[i])
    return lst

'''def reverse_list(lst):
    for i in range(len(lst)):
        lst.insert(i, lst.pop())
    return lst'''

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True