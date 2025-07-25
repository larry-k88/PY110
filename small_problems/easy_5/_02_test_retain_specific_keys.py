from _02_retain_specific_keys import keep_keys

def test_keep_keys():
    assert keep_keys(input_dict, keys) == expected_dict

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True