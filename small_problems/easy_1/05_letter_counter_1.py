# Write a function that takes a string consisting of zero or more
# space-separated words and returns a dictionary that shows the number
# of words of different sizes.
# Words consist of any sequence of non-space characters.

'''
Problem:

    - Function that takes a string (could be empty but words must be 
    space-separated) and returns a dict with keys showing the word
    length and the value showing how many words are that length

    - Input - string (empty or space-separated)
    - Output - dictionary
     
    - Explicit requirements:
        - Any sequence of characters between spaces in a word (could
        be punctuation)
        - String could be empty - returns an empty dictionary
    - Implicit requirements:
        - Each value will be at least 1
        - Sum of the value will be the length of the word
        - Case is irrelevant - only concerned with the length
    - Questions
        - 

Examples/Test Cases:
    - See below

Data Structure:
    - Dictionary for the output
    - Consider `split()` to get the words
    - Use `len()` to get the length

Algorithm:  

    - Split the input into a list of words
    - SET an empty dict
    - Iterate over words in the list
    - GET the length of the words
    - IF the length is not in the dictionary:
        - ADD the length to the dict with 1 as value
    - ELSE:
        - add 1 to the value 

'''

''' # my solution
def word_sizes(text):
    output_dict = {}
    for word in text.split():
        word_length = len(word)
        if word_length not in output_dict:
            output_dict[word_length] = 1
        else:
            output_dict[word_length] += 1
    
    return output_dict'''

# Use output_dict[word_length] = output_dict.get(word_length, 0) + 1
# This will negate the need for the if/else

def word_sizes(text):
    output_dict = {}

    for word in text.split():
        word_length = len(word)
        output_dict[word_length] = output_dict.get(word_length, 0) + 1

    return output_dict 

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})