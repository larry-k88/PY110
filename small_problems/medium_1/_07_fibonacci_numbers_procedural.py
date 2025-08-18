# The Fibonacci series is a sequence of numbers in which each number is
# the sum of the previous two numbers. The first two Fibonacci numbers
# are 1 and 1. The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3,
# the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. In
# mathematical terms, this can be represented as:

# F(1) = 1
# F(2) = 1
# F(n) = F(n - 1) + F(n - 2)    (where n > 2)

# Write a function called fibonacci that computes the nth Fibonacci
# number, where nth is an argument passed to the function:

'''
Problem:

  - Function that works out Fibonacci sequence

     
  - Explicit requirements:
      - F(1) = 1
      - F(2) = 1
      - F(n) = Number is the sum of previous 2
  - Implicit requirements:
      - n needs to be > 0
  - Questions
      - 

Examples/Test Cases:
    - print(fibonacci(1) == 1)                  # True
    - print(fibonacci(2) == 1)                  # True
    - print(fibonacci(3) == 2)                  # True
    - print(fibonacci(4) == 3)                  # True
    - print(fibonacci(5) == 5)                  # True
    - print(fibonacci(6) == 8)                  # True
    - print(fibonacci(12) == 144)               # True
    - print(fibonacci(20) == 6765)              # True
    - print(fibonacci(50) == 12586269025)       # True
    - print(fibonacci(75) == 2111485077978050)  # True

Data Structure:
  - Input: integer
  - Output: integer
    
  - Intermediate: 

High-level strategies:
  - Deal with n = 1 and n = 2, set to 1
  - Assign 2 variables to hold n = 1 and n = 2

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - If n is 1 or 2 set to 1
  - fib_a = f(1) and fib_b = f(2)
  - fib_n = fib_a + fib_b

'''

def fibonacci(n):
    if n <= 2:
        return 1
    previous, current = 1, 1
    for _ in range(n - 2):
        previous, current = current, previous + current

    return current

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(12))
print(fibonacci(20))
print(fibonacci(50))
print(fibonacci(75))