'''
Write a function that returns True if the string passed as an argument
is a palindrome, False otherwise. A palindrome reads the same forwards
and backwards. For this problem, the case matters and all characters
matter.

Problem:    Create a function which outputs True/False depending on
            whether the string argument is a palindrome - every 
            character and case is important
            Input - string
            Output - True/False
            Explicit requirements:
                - Argument must be a string
                - White space counts as a character
                - Case of the characters matters

            Implicit requirements:
                - Characters can be anything in Unicode

Examples/Test Cases:    True: 'madam', '356653'
                        False: 'Madam', 'madam i'm adam'

Data Structure:     No need to deviate from strings
                    Booleans required for the return value       

Algorithm:  

    Pseudocode:
        Check the argument is a string using `if not type(arg) == str`
            If no, return a message saying it's not valid
            If yes, check if the reverse of the argument == the argument
                If no, False
                If yes, True 
'''

# All of these examples should print True

def is_palindrome(phrase):
    # if phrase[::-1] == phrase:
    #     return True
    # return False

    return phrase [::-1] == phrase

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)