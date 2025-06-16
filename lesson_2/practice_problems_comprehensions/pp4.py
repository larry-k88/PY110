# Given the following data structure, write some code that uses
# comprehensions to define a dictionary where the key is the first item in
# each sublist, and the value is the second.

# Expected: Pretty printed for clarity
'''
expected = {
    'a': 1,
    'b': 'two',
    'sea': {'c': 3},
    'D': ['a', 'b', 'c']
}
'''

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

new_dict = {item1: item2 for item1, item2 in lst}

print(new_dict)

'''
LS uses indexing:
new_dict = {item[0]: item[1] for item in lst}
print(new_dict)
'''
