# We want to remove certain items from a set while iterating over it,
# but the code below throws an error. Why is that and how can we fix it?

data_set = {1, 2, 3, 4, 5}

''' Changing the size of a collection during iteration causes the error 
Some collections (e.g. lists) allow it, but some (set/dictionaries) do not

for item in data_set:
    if item % 2 == 0:
        data_set.remove(item)
        
'''

data_set = {1, 2, 3, 4, 5}

data_set = {item for item in data_set if item % 2 != 0 }

print(data_set)