# Write a function that takes two list arguments, each containing a list
# of numbers, and returns a new list that contains the product of each
# pair of numbers from the arguments that have the same index. You may
# assume that the arguments contain the same number of elements.

'''
Problem:

    - Take 2 lists and return a new one with the products of the values
    at each index

    - Input - 2 lists
    - Output - 1 list 
     
    - Explicit requirements:
        - Lists are of the same length
        - New list required
    - Implicit requirements:
        - Numbers can be either positive/negative
    - Questions
        - 

Examples/Test Cases:
    - list1 = [3, 5, 7]
    - list2 = [9, 10, 11]
    - print(multiply_list(list1, list2) == [27, 50, 77])  # True

Data Structure:
    - Lists       

Algorithm:  

    - Iterate over the items using range(len of list)
    - SET empty list as output
    - For each index, multiply product of each lst at same index
        - append to the output
    - Return the output

'''
# def multiply_list(lst1, lst2):
#     output = []
#     for idx in range(len(lst1)):
#         output.append(lst1[idx] * lst2[idx])

#     return output

# list1 = [3, 5, 7]
# list2 = [9, 10, 11]
# print(multiply_list(list1, list2) == [27, 50, 77])  # True

# Using zip()

def multiply_list(lst1, lst2):
    return [a * b for a, b in zip(lst1, lst2)]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
