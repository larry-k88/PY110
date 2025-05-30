# Given the following string, create a dictionary that represents the
# frequency with which each letter occurs.
# The frequency count should be case-sensitive:

statement = "The Flintstones Rock"

letter_frequency = {}
for char in statement.replace(' ', ''):
    letter_frequency[char] = letter_frequency.get(char, 0) + 1

print(letter_frequency)

'''output
{
    'T': 1,
    'h': 1,
    'e': 2,
    'F': 1,
    'l': 1,
    'i': 1,
    'n': 2,
    't': 2,
    's': 2,
    'o': 2,
    'R': 1,
    'c': 1,
    'k': 1
}
'''