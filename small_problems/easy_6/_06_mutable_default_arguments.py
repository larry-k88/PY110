# We want to create a function that appends a given value to a list.
# However, the function seems to be behaving unexpectedly:

''' 1st call: default lst is empty, so works as expected.
2nd call: `lst` now has a value associated with it (from 1st call) - 
therefore the default isn't used and instead, the previous value is mutated
def append_to_list(value, lst=[]):
    lst.append(value)
    return lst
    '''

def append_to_list(value, lst=None):
    if lst == None:
        lst = []
    
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])