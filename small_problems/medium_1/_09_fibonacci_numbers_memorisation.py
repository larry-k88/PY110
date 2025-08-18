# For this exercise, your objective is to refactor the recursive
# fibonacci function to use memoization.

# Hint: One approach to memoization is to use a lookup table, such as an
# object, for storing and accessing previously computed values.

'''
Problem:

  - Function that works out Fibonacci sequence, using memorisation

     
  - Explicit requirements:
      - Once a value has been completed, save it and access it for
      the next call
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
    
  - Intermediate: get() function with default being the function

High-level strategies:
  - Create a dictionary to track the value of n along with the fib value. 
  Deal with n = 1 and n = 2, 

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - Create empty dict
  - Deal with n = 1 and n = 2: add the values to dict
  - Capture value of fib as 

'''

def fibonacci(n, fib_dict=None):
    if fib_dict is None:
        fib_dict = {}
    if n in fib_dict:
        return fib_dict[n]
    
    if n <= 2:
        result = 1
    else:
        result = fibonacci(n - 1, fib_dict) + fibonacci(n - 2, fib_dict)

    fib_dict[n] = result
    return result

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