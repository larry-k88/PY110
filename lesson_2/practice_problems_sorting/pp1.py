# Sort the following list of numbers first in ascending numeric order,
# then in descending numeric order. Do not mutate the list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

ascending_lst = sorted(lst)
print (f'Ascending: {ascending_lst}')
print(f'Original: {lst}')

descending_lst = sorted(lst, reverse=True)
print(f'Descending: {descending_lst}')
print(f'Original: {lst}')

'''
[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort
'''