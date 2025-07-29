# You have a function that is supposed to reverse a string passed as an
# argument. However, it's not producing the expected output. Explain the
# bug, and provide a solution.

''' `string` (Line 8) is being reassigned (not mutated) to each letter 
from the argument (i.e. h, e, l, l, o) prepended to the argument
def reverse_string(string):
    for char in string:
        string = char + string
        # hhello
        # ehhello
        # lehhello
        # llehhello
        # ollehhello

    return string
'''
# string being iterated over (argument) is not being modified here:
def reverse_string(string): 
    new_string = ''
    for char in string:
        new_string = char + new_string

    return new_string

# string slicing
# def reverse_string(string):
#     return string[::-1]

print(reverse_string("hello") == "olleh")

