# Write a function that takes a string as an argument and returns that
# string with a staggered capitalization scheme. Every other character,
# starting from the first, should be capitalized and should be followed
# by a lowercase or non-alphabetic character. Non-alphabetic characters
# should not be changed, but should be counted as characters for
# determining when to switch between upper and lower case.

def staggered_case(string): # mine
    return ''.join(
        [char.upper()
         if position % 2 == 0 else char.casefold()
         for position, char in enumerate(string)]
        )

# def staggered_case(string): #LS demonstrating a concept
#     result = ''
#     for idx, char in enumerate(string):
#         func = char.upper if idx % 2 == 0 else char.lower
#         result += func()

#     return result

# def staggered_case(string): # more direct that LS
#     result = ''
#     for idx, char in enumerate(string):
#         result += char.upper() if idx % 2 == 0 else char.lower()

#     return result
