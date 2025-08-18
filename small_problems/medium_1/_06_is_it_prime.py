# A prime number is a positive number that is evenly divisible only by
# itself and 1. Thus, 23 is prime since its only divisors are 1 and 23.
# However, 24 is not prime since it has divisors of
# 1, 2, 3, 4, 6, 8, 12, and 24. Note that the number 1 is not prime.

# Write a function that takes a positive integer as an argument and
# returns True if the number is prime, False if it is not prime.

# You may not use any of Python's add-on packages to solve this problem.
# Your task is to programmatically determine whether a number is prime
# without relying on functions that already do that for you.

'''
Problem:

  - Function that determines if a number is prime - boolean

     
  - Explicit requirements:
      - Number must have only 2 divisors - 1 and itself
      - Number must be positive
  - Implicit requirements:
      - If even, it is not prime
  - Questions
      - 

Examples/Test Cases:
    - print(is_prime(1) == False)              # True
    - print(is_prime(2) == True)               # True
    - print(is_prime(3) == True)               # True
    - print(is_prime(4) == False)              # True
    - print(is_prime(5) == True)               # True
    - print(is_prime(6) == False)              # True
    - print(is_prime(7) == True)               # True
    - print(is_prime(8) == False)              # True
    - print(is_prime(9) == False)              # True
    - print(is_prime(10) == False)             # True
    - print(is_prime(23) == True)              # True
    - print(is_prime(24) == False)             # True
    - print(is_prime(997) == True)             # True
    - print(is_prime(998) == False)            # True
    - print(is_prime(3_297_061) == True)       # True
    - print(is_prime(23_297_061) == False)     # True

Data Structure:
  - Input: integer
  - Output: boolean
    
  - Intermediate: 

High-level strategies:
  - Check if even, if not check if the remainder when dividing by every
  odd number less than the number - it needs to be not 0 to be prime.

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - If n is even, return False
  - For i in range(n - 2, 1, -2):
    - if n % i == 0, return False

'''
def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False

    return True

# LS: import math and using sqrt(n) as the upper limit for the range

def is_prime(n):
    # deals with 1 (but also 0 and anything negative)
    if n < 2:
        return False

    # deals with any even numbers, except 2
    if n % 2 == 0 and n != 2:
        return False

    # checks odd divisors from 3 to sqrt(n)
    for divisor in range(3, int(n ** 0.5) + 1, 2):
        if n % divisor == 0:
            return False

    return True