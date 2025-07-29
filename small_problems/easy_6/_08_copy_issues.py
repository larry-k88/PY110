# We have a list of lists and want to duplicate it. After making the
# copy, we modify the original list, but the copied list also seems to
# be affected:

''' `copy` creates a shallow copy - the reference to the nested lists are 
copied, not the lists themselves. Therefore, when a change is made to the 
original, it is reflected in shallow copies. A deep copy will ensure all values
in the copy are separate from the original.
import copy

original = [[1], [2], [3]]
copied = copy.copy(original)

original[0][0] = 99
'''

import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])