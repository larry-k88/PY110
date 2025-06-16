# Given the following data structure, sort the list so that the
# sub-lists are ordered based on the sum of the odd numbers that they
# contain. You shouldn't mutate the original list.

# Note that the first sublist has the odd numbers 1 and 7; the second
# sublist has odd numbers 1, 5, and 3; and the third sublist has 1 and
# 3. Since (1 + 3) < (1 + 7) < (1 + 5 + 3), the sorted list should look
# like this:

# [[1, 8, 3], [1, 6, 7], [1, 5, 3]]

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_odds(collection):
    odds = [item for item in collection if item % 2 == 1]
    return sum(odds)
    
new_list = sorted(lst, key=sum_odds)

print(new_list)