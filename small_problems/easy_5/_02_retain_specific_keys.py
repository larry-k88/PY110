# Given a dictionary and a list of keys, produce a new dictionary that
# only contains the key/value pairs for the specified keys.

# def keep_keys(dictionary, key_list): # "for every key, should I keep it?"
#     return {key: value for key, value in dictionary.items() if key in key_list}

def keep_keys(dictionary, key_list): # "for keys I want, let me get it"
    return {key: dictionary[key] for key in key_list if key in dictionary}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
