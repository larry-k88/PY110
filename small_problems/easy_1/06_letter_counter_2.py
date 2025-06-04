# WModify the word_sizes function from the previous exercise to exclude
# non-letters when determining word size. For instance, the word size of
#  "it's" is 3, not 4.

'''
Problem:

    - Function that takes a string (could be empty but words must be 
    space-separated) and returns a dict with keys showing the word
    length and the value showing how many words are that length

    - Input - string (empty or space-separated)
    - Output - dictionary
     
    - Explicit requirements:
        - *word length must not include non-letters
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
    - IF the word is not isalpha:
        - iterate over the letters and update a new string
        - length of that string 
    - ELSE:
        - as before

'''

def word_sizes(text):
    output_dict = {}

    for word in text.split():
        if not word.isalpha():
            alpha_word = [char for char in word if char.isalpha()]
            word_length = len(alpha_word)

        else:
            word_length = len(word)

        output_dict[word_length] = output_dict.get(word_length, 0) + 1

    return output_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

print(word_sizes('.?')) 