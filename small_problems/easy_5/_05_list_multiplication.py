# Given two lists of integers of the same length, return a new list
# where each element is the product of the corresponding elements from
# the two lists.

def multiply_items(list_1, list_2):
    return [num_1 * num_2
            for num_1, num_2
            in zip(list_1, list_2)]

