# Write a function that takes two lists as arguments and returns a set
# that contains the union of the values from the two lists. You may
# assume that both arguments will always be lists.

'''
Problem:

    - Function that takes 2 lists of equal lengths and returns a set 
    containing the union of their values

    - Input - 2 lists of equal length
    - Output - set with union of the lists (no duplicates by default)
     
    - Explicit requirements:
        - Arguments will be lists
        - Arguments will be the same length
        - 
    - Implicit requirements:
        - There should be no duplicates
    - Questions
        - Empty lists to produce an empty set?

Examples/Test Cases:
    - print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

Data Structure:
    - Lists to be compared
    - Converted into a set to get rid of duplicates      

Algorithm:  

    - Create an empty set
    - Merge the lists
    - Convert to set

'''
def union(lst1, lst2):
    return set(lst1 + lst2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True