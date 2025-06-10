# Given the following code, what will the final values of a and b be? Try
# to answer without running the code.

a = 2
b = [5, 8]
lst = [a, b]
# a = 2 , b = [5, 8], lst = [2, [5, 8]]

lst[0] += 2
# a = 2 , b = [5, 8], lst = [4, [5, 8]] --> int is immutable

lst[1][0] -= a
# a = 2 , b = [3, 8], lst = [4, [3, 8]] --> list is mutable

print(a)
print(b)
print(lst)
