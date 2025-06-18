# Write a function that counts the number of occurrences of each element
# in a given list. Once counted, print each element alongside the number
# of occurrences. Consider the words case sensitive
# e.g. ("suv" != "SUV").

'''
Problem:

    - Count the number of times a word is in a list - print the results

    - Input - list of strings
    - Output - string (f-string)
     
    - Explicit requirements:
        - Case sensitive
    - Implicit requirements:
        - 
    - Questions
        - 

Examples/Test Cases:
     - vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
     -             'motorcycle', 'motorcycle', 'car', 'truck']
     - 
     - count_occurrences(vehicles)

Data Structure:
    - Store the data in a dictionary
    - print the info from the dictionary
    - try to only make one pass through the data   

Algorithm:  

    - Set empty dictionary --> vehicle_count
    - iterate over each list item:
        - if item in keys:
            - add 1 to value
        - else:
            add item and value = 1
    - iterate over items():
        - f-string for output
'''


def count_occurrences(list_of_veh):
    lower_list_of_veh = [veh.casefold() for veh in list_of_veh]
    vehicle_count = {}
    for vehicle in lower_list_of_veh:
        vehicle_count[vehicle] = vehicle_count.get(vehicle, 0) + 1
    print_occurrences(vehicle_count)    
    
def print_occurrences(dict_of_vehicles):
    for vehicle, count in dict_of_vehicles.items():
        print(f'{vehicle} => {count}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck', 'suv']

count_occurrences(vehicles)


'''
your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 2 # case insensitive
motorcycle => 2
'''

'''# Lack of order requirement, sets might be good, but O(n^2)
def count_occurrences(list_of_veh):
    lower_list_of_veh = [veh.casefold() for veh in list_of_veh]
    for veh in set(lower_list_of_veh):
        print(f'{veh} => {lower_list_of_veh.count(veh)}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck', 'suv']

count_occurrences(vehicles)'''
