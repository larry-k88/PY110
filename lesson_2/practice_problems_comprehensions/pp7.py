# Given the following data structure return a new list identical in
# structure to the original, but containing only the numbers that are
# multiples of 3.

# Expected: [[], [3, 12], [9], [15, 18]]

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

'''
No comprehensions
new_lst = []
for sublist in lst:
    new_sublist = []
    for number in sublist:
        if number % 3 == 0:
            new_sublist.append(number)

    new_lst.append(new_sublist)

print(new_lst)
'''

'''
Comprehensions - not best solution (nested comprehensions suggest it's bad)

new_lst = [[number for number in sublist if number % 3 == 0] for sublist in lst]

print(new_lst)
'''

# maybe better to break into 2 comprehensions:

def divisible_by_3(collection):
    return [number for number in collection if number % 3 == 0]

new_lst = [divisible_by_3(sublist) for sublist in lst]

print(new_lst)