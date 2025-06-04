'''
Problem:

Write another function that returns True if the string passed as an
argument is a palindrome, or False otherwise. This time, however, your
function should be case-insensitive, and should ignore all
non-alphanumeric characters. If you wish, you may simplify things by
calling the is_palindrome function you wrote in the previous exercise.

    - Function that determines if a string is a palindrome, but is 
    case-insensitive and only alpha-numeric characters should be
    included

    - Input - string
    - Output - boolean
     
    - Explicit requirements:
        - True if the string is a palindrome (subject to requirements)
        - Rules:
            - Case-insensitive
            - Ignore non-alphanumeric characters
    - Implicit requirements:
        - `ispalindrome()` can be used (from 02_palindromic_strings_2.py)
        - whitespace is not alphanumeric so is ignored

Examples/Test Cases:
    - See below

Data Structure:
    - `ispalindrome()` can be used after other requirements are dealt with
    - `isalpha()`, `replace()` and `casefold()` could be used


Algorithm:  

    - FOR char in the string, add to a new string if:
        - char is alphanumeric and not a space
    - SET a variable in lowercase
    - pass the return value to is_real_palindrome()

'''
def is_real_palindrome(phrase):
    cleaned_phrase = ''
    for char in phrase:
        if char.isalnum():
            cleaned_phrase += char
    return is_palindrome(cleaned_phrase.casefold())

def is_palindrome(phrase):
    return phrase [::-1] == phrase


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True