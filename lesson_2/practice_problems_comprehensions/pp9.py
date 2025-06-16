# Given the following data structure, write some code to return a list
# that contains only the dictionaries where all the numbers are even.

# Expected: [{'e': [8], 'f': [6, 10]}]

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def is_list_even(collection):
    return all(num % 2 == 0 for num in collection)

def is_value_even(dictionary):
    return all(is_list_even(list_value) for list_value in dictionary.values())

output = [dictionary for dictionary in lst if is_value_even(dictionary)]

print(output)