# Write a function that takes a list of numbers and returns a list with
# the same number of elements, but with each element's value being the
# running total from the original list.

'''
Problem:

    - Take a list of numbers and return a list which shows the running 
    total from the original list

    - Input - list containing numbers 
    - Output - list containing numbers 
     
    - Explicit requirements:
        - Output list should have the same number of elements as
        original
        - Empty list returns empty list
    - Implicit requirements:
        - The first element of the returned list will be the same as 
        the original
        - Final element will the sum of the list elements
    - Questions
        - What if the list contains anything other than numbers (float)
        - What if the argument isn't a list?
        - Negative numbers?
    

Examples/Test Cases:
    - [2, 5, 13] --> [2, 7, 20]
    - [14, 11, 7, 15, 20] --> [14, 25, 32, 47, 67]
    - [3] --> [3]
    - [] --> []

Data Structure:
    - Lists to be iterated over
    - Enumerate() to get the index and the number
    - Use the list index to add the element of the previous index     

Algorithm:  

    - SET total = 0
    - SET output_list = []
    - FOR each number:
        - IF index == 0:
            append to output_list
        - ELSE:
            add to number when index is one less

'''
# def running_total(list_of_numbers):
#     output_list = []
#     for index, number in enumerate(list_of_numbers):
#         if index == 0:
#             output_list.append(number)
#         if index > 0:
#             output_list.append(number + output_list[index -1])
#     return output_list

def running_total(list_of_numbers):
    output_list = []
    total = 0
    for number in list_of_numbers:
        total += number
        output_list.append(total)
    return output_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True