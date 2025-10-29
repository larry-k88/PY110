# Write a function that takes a list of strings and sorts it based on
# the last character of each string. If the last character is the same,
# the strings should be sorted alphabetically in their original case.

# Function signature
def sort_key(string):
    return (string[-1], string)

def sort_by_last_char(str_list):
    str_list.sort(key=sort_key)
    return str_list

# Example Data
str_list = ['date', 'banana', 'cherry', 'apple']
print(sort_by_last_char(str_list))
# Expected output: ['banana', 'apple', 'date', 'cherry']

str_list_2 = ['python', 'java', 'ruby', 'csharp']
print(sort_by_last_char(str_list_2))
# Expected output: ['java', 'csharp', 'python', 'ruby']