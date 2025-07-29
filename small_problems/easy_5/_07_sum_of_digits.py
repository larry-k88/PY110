# Write a function that takes one argument, a positive integer, and
# returns the sum of its digits.

def sum_digits(num):
    return sum([int(digit) for digit in str(num)])
