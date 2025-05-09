"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.

P

input: string
output: list of strings (new object)
rules:
    Explicit:
        - Palindromes of 2 or more characters (i.e. no single characters) must be 
    added to a list
        - Palindromes are case-sensitive ('AA' is a palindrome, 'Aa' is not)

    Implicit:
        - Empty strings return an empty list
        - If no palindromes present, return an empty list
"""

def palindrome_substrings(s):
    result = []
    substrings_list = substrings(s)

    for substring in substrings_list:
        if is_palindrome(substring):
            result.append(substring)

    return result


# Test cases:

# Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]