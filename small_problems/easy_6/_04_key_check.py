# You have a function that should check whether a key exists in a
# dictionary and returns its value. However, it's raising an error. Why
# is that? How would you fix this code?

''' We will get a key error when trying to access a key that doesn't exist. 
Using, `dict.get(key)` doesn't raise an error, it returns None. Could also use
`if key in my_dict` on line 9.
def get_key_value(my_dict, key):
    if my_dict[key]:
        return my_dict[key]
    else:
        return None
'''

def get_key_value(my_dict, key):
    return my_dict.get(key) # could be (key, None) for clarity

print(get_key_value({"a": 1}, "b"))