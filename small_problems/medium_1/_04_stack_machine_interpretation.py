'''
Write a function that implements a miniature stack-and-register-based
programming language that has the following commands (also called
operations or tokens):

n: Place an integer value, n, in the register. Do not modify the stack.
PUSH: Push the current register value onto the stack. Leave the value
    in the register.
ADD: Pop a value from the stack and add it to the register value,
    storing the result in the register.
SUB: Pop a value from the stack and subtract it from the register
    value, storing the result in the register.
MULT: Pop a value from the stack and multiply it by the register value,
    storing the result in the register.
DIV: Pop a value from the stack and divide the register value by the
    popped stack value, storing the integer result back in the register.
REMAINDER: Pop a value from the stack and divide the register value by
    the popped stack value, storing the integer remainder of the
    division back in the register.
POP: Remove the topmost item from the stack and place it in the
    register.
PRINT: Print the register value.

All operations are integer operations (which is only important with DIV
and REMAINDER).

Programs will be supplied to your language function via a string
argument. Your function may assume that all arguments are valid programs
-- i.e., they will not do anything like trying to pop a non-existent
value from the stack, and they won't contain any unknown tokens.

Initialize the stack and register to the values [] and 0, respectively.
'''

'''
Problem:

  - Create a function which performs various operations on a stack-and-
  register style language

     
  - Explicit requirements:
      - Programs (i.e. a set of operations) are given as the argument
      - Order of the operations is important
      - Stack is a list and register is an int
  - Implicit requirements:
      - When using DIV and REMAINDER, note that the output is an int
  - Questions
      - 

Examples/Test Cases:
    - minilang('PRINT')
    # 0

    - minilang('5 PUSH 3 MULT PRINT')
    # 15

    - minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
    # 5
    # 3
    # 8

    - minilang('5 PUSH POP PRINT')
    # 5

    - minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD
    PRINT')
    # 5
    # 10
    # 4
    # 7

    - minilang('3 PUSH PUSH 7 DIV MULT PRINT')
    # 6

    - minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
    # 12

    - minilang('-3 PUSH 5 SUB PRINT')
    # 8

    - minilang('6 PUSH')
    # (nothing is printed)

Data Structure:
  - Input: String containing the program (set of operations)
  - Output: Integer
    
  - Intermediate: List (to isolate the operations)

High-level strategies:
  - Break up the program into operations - iterate over them and use 
  match/case (or similar) to tell the function what to do

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  
  - Split the program into a list of operations/tokens
  - Iterate over the list and match the operation/token to some code:
    - n: set n to register
    - PUSH: append register to stack
    - ADD: pop() from stack, reassign register to register + popped
    - SUB: pop() from stack, reassign register to register - popped
    - MULT: pop() from stack, reassign register to register * popped
    - DIV: pop() from stack, reassign register to register // popped
    - REM: pop() from stack, reassign register to register % popped
    - POP: pop() from stack, reassign register to popped
    - PRINT: print register

Further Exploration:
Refactor the minilang function to include some error handling. In
particular, the function should detect and report empty stack conditions
(trying to use a value from the stack when there are no values), and
invalid tokens in the program. Ideally, the function should return an
error message if an error occurs, or None if the program runs
successfully.

'''

def minilang(program):
    stack = []
    register = 0

    for token in program.split():
        try:
            match token:
                case 'PUSH':
                    stack.append(register)
                case 'ADD':
                    register += stack.pop()
                case 'SUB':
                    register -= stack.pop()
                case 'MULT':
                    register *= stack.pop()
                case 'DIV':
                    register //= stack.pop()
                case 'REMAINDER':
                    register %= stack.pop()
                case 'POP':
                    register = stack.pop()
                case 'PRINT':
                    print(register)
                case _:
                    register = int(token)
        except IndexError:
            return (f'Error - empty stack: "{token}" requires at least '
                   f'one item in the stack')
        except ValueError:
            return f'Error - invalid token: "{token}" is invalid'

    return None

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)

minilang('POP ADD')
# Empty stack

minilang('6 PUSh')
# Invalid token