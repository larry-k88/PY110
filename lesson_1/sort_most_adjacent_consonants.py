'''
Problem:    Reorder a list of strings (high to low) based on the highest
            number of adjacent consonants in that string. 
            Input - list of strings
            Output - sorted list
            Explicit requirements:
                - adjacent consonants: next to each other in the same 
                word; or a space between them in adjacent words
                - if they have the same number, they retain original
                order

            Implicit requirements:
                - Strings may not be empty (assumed)
                - String output should be in descending order
                - Case not relevant (assumed)
                - Single consonants not relevant
                - Number of adjacent consonants will never be 1
            
            Questions
                - Space and punctuation? e.g. 'Stop, who are you?' - are
                p and w adjacent?

Examples/Test Cases:    See below

Data Structure:     Dictionary to track the string in the list and the 
                    number of adjacent consonants
                    Output will need to be a list of the dict values, 
                    sorted by the value

Algorithm:  

    - Iterate over the list of strings
    - For each string, determine how many adjacent consonants it has
    - Add the string to a dict, with this number as the value
    - Return the sorted list (reverse)

    - Adjacent consonants:
        - Take a string and return the highest number of adjacent
        consonants in that string
        - Input: string
        - Output: integer
        - Tests:
            - 'dddaa' --> 3
            - 'dddd' --> 4
            - 'ccaa' --> 2
            - 'aaaa' --> 0
        - Algorithm:
            - Remove spaces
            - Set a consonant count to 0
            - Set a temp consonant string to empty string
            - Iterate over each letter:
                - If a consonant, add to temp consonant string
                - If a vowel:   
                    - If len of temp consonant string > count:
                        - If count > 1:
                            Set count to the length
                    - Reset temp consonant string to empty
            - Return the count

'''

def max_adjacent_consonants(element):
    VOWELS = 'aeiou'
    consonant_count = 0
    temp_consonants_string = ''
    for char in element.replace(' ', ''):
        if char not in VOWELS: # If it's a consonant
            temp_consonants_string += char
        elif char in VOWELS: # If it's a vowel
            if (len(temp_consonants_string) > consonant_count and
                len(temp_consonants_string) > 1):
                consonant_count = len(temp_consonants_string)
            temp_consonants_string = ''
    return consonant_count if consonant_count else len(temp_consonants_string)

def sort_by_consonant_count(list_of_words):
    list_of_words.sort(key=max_adjacent_consonants, reverse=True)
    return list_of_words


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']