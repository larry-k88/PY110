# You want to multiply all elements of a list by 2. However, the
# function is not returning the expected result. Explain the bug, and
# provide a solution.

''' ints are immutable so when each one is assigned to the local variable
`item`, the are correctly doubled. But the list is not being updated/mutated
def multiply_list(lst):
    for item in lst:
        item *= 2

    return lst
'''
    
def multiply_list(lst):
   return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]))
print(multiply_list([1, 2, 3]) == [2, 4, 6])