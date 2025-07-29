# Modify the function from the previous exercise so it ignores
# non-alphabetic characters when determining whether it should uppercase
# or lowercase each letter. The non-alphabetic characters should still
# be included in the return value; they just don't count when toggling
# the desired case.

def staggered_case(string): # mine
    result = ''
    upper_char = True
    for char in string:
        if char.isalpha():
            result += char.upper() if upper_char else char.casefold()
            upper_char = not upper_char

        elif not char.isalpha():
            result += char

    return result
