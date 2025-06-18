# Write a function that combines two lists passed as arguments and
# returns a new list that contains all elements from both list
# arguments, with each element taken in alternation.

# You may assume that both input lists are non-empty, and that they have
# the same number of elements.

'''
Problem:

    - Merge 2 lists in turn

    - Input - 2 lists
    - Output - 1 list
     
    - Explicit requirements:
        - Both lists are non-empty
        - Lists have same number of elements
    - Implicit requirements:
        - 
    - Questions
        - 

Examples/Test Cases:
    - list1 = [1, 2, 3]
    - list2 = ['a', 'b', 'c']
    - expected = [1, "a", 2, "b", 3, "c"]
    - print(interleave(list1, list2) == expected)      # True

Data Structure:
    - zip()      

Algorithm:  

    - Loop over the zipped item
    - Add the zipped item to a list

'''
def interleave(lst1, lst2):
    output = []
    for tuple in zip(lst1, lst2):
        output.extend(tuple)
    return output

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
