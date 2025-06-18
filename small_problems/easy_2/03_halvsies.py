# Write a function that takes a list as an argument and returns a list
# that contains two elements, both of which are lists. Put the first half
# of the original list elements in the first element of the return value
# and put the second half in the second element. If the original list
# contains an odd number of elements, place the middle element in the
# first half list.

'''
Problem:

    - Take a list and half it (if odd, make first list bigger) - add the 
    half lists to a new list (made of 2 lists)

    - Input - one list
    - Output - one list containing 2 lists
     
    - Explicit requirements:
        - If number of elements is odd, add the middle element to list1
        - The output is a new list which contains only 2 lists.
    - Implicit requirements:
        - The lists will be of equal length if even number of elements
        - The first list will be longer by 1 if odd number of elements
        - Empty list - return two empty lists within
    - Questions
        - 

Examples/Test Cases:
    - # All of these examples should print True
    - print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
    - print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
    - print(halvsies([5]) == [[5], []])
    - print(halvsies([]) == [[], []])

Data Structure:
    - len()
   

Algorithm:  
    - Determine midpoint of input list - account for odd AND even
    - SET slice from start to midpoint
    - SET slice from midpoint to end
    - Return list([slice1, slice2])

'''
def halvsies(lst):
    mid_point = (len(lst) + 1) // 2
    lst1 = lst[:mid_point]
    lst2 = lst[mid_point:]

    return [lst1, lst2]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])