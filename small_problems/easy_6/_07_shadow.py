# We defined a function intending to multiply the sum of numbers by a
# factor. However, the function raises an error. Why? How would you fix
# this code?

''' `sum` is a built-in function that has been redefined. We try to use the 
built-in version on line 8, but it's already been redefined.
def sum(numbers, factor):
    return factor * sum(numbers)
'''

def multiply_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(multiply_sum(numbers, 2))