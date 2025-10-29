# Predict the output of the following code snippet and explain why the
# final output is what it is.

import copy

original_list = [
    {'name': 'apple', 'details': {'color': 'red', 'quantity': 10}},
    {'name': 'banana', 'details': {'color': 'yellow', 'quantity': 15}},
]

copied_list = copy.copy(original_list)

copied_list[0]['details']['quantity'] = 20
copied_list.append({'name': 'orange', 'details': {'color': 'orange', 'quantity': 5}})

print(original_list)

"""
The `copy.copy()` function creates a shallow copy of the argument - the argument
can be any data type, including lists as in this case.
The shallow copy created is a new object and assigned to the variable `copied_list`.
The new object copies the outer structure, but only includes references to any 
nested structures'

In this case, we have a list of 2 elements, each element is a dictionary. Each 
of the dictionaries contains 2 key/value pairs (one of these values is
another dictionary).
The `copied_list` variable therefore contains 2 dictionary elements, but each
of these elements contain pointers to key/value pairs from the dictionaries in
the `original_list`.

`copied_list[0]['details']['quantity'] = 20`
This contained chained indexing and a reassignment. Python will read the code
from left to right, first indexing the first dictionary in the copied list.
`[details]` is chained on to this and will reference the value associated with 
the `details` key from the original list. Finally, the code reassigns the value
associated with `quantity` to `20` (from `10`). As we are referencing the dictionary
values from `original_list`, we will see the changes reflected there

`copied_list.append({'name': 'orange', 'details': {'color': 'orange', 'quantity': 5}})`
This line appends (mutates) the copied list by adding a third dictionary to it.
However, as this list is a copy, we won't see the changes in `original_list`
"""

