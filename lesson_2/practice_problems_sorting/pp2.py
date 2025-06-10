# Repeat the previous exercise but, this time, perform the sort by
# mutating the original list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort()
print (f'Ascending: {lst}')


lst.sort(reverse=True)
print(f'Descending: {lst}')

'''
[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort
'''