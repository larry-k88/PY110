'''
BOUNCY COUNT
Some numbers have only ascending digits, like 123, 3445, 2489, etc.
Some numbers have only descending digits, like 321, 5443, 9842, etc.
A number is "bouncy" if it has both ascending and descending digits, like 313, 92543, etc.
Write a method that takes a list of numbers and counts how many of them are bouncy.
'''

'''
Problem:

    - Given an array of integer inputs, return an integer representing
    the count of numbers that are considered "bouncy"

    - Input - list of numbers
    - Output - integer
     
    - Explicit requirements:
        - Bouncy numbers have both ascending and descending digits
    - Implicit requirements:
        - 
    - Questions
        - no digits?
        - empty list

Examples/Test Cases:
    - See below

Data Structure:
    - strings e.g. '11' for 11      

High-level strategies:  
    - If we only have 1 or 2 digits, return 0
    - Convert each number into a string
    - Set 2 flags: up and down
    - Iterate over each digit and compare to previous digit

Algorithm:
    - Helper function: `is_bouncy(number)` --> True if bouncy, False otherwise
        - Convert to str and check length:
        - If the number has 2 or fewer digits --> False
        - Set `asc_flag` and `desc_flag` to False
        - While not `asc_flag` and not `desc_flag`:
            - Iterate over the characters in the string and compare with
            the previous one.
            - If first is lower than first, set `asc_flag` to True
            - If second is lower than first, set `desc_flag` to True 
        - Return `asc_flag` and `desc_flag`
    
    - main function:
     - iterate over the numbers in the list and call the helper
     - count the number of True

'''
def is_bouncy(number):
    str_number = str(number)
    number_length = len(str_number)
    if number_length <= 2:
        return False
    
    asc_flag = desc_flag = False

    for i in range(number_length - 1):
        if str_number[i] < str_number[i + 1]:
            asc_flag = True
        elif str_number[i + 1] < str_number[i]:
            desc_flag = True

        if asc_flag and desc_flag:
            return True    
        
    return asc_flag and desc_flag


def bouncy_count(lst):
    count = []
    for number in lst:
        count.append(is_bouncy(number))
    return sum(count)

# Python test cases:
print(bouncy_count([]) == 0)
print(bouncy_count([11, 0, 345, 21]) == 0)
print(bouncy_count([121, 4114]) == 2)
print(bouncy_count([176, 442, 80701644]) == 2)

'''# James
def is_bouncy(number):
    goes_up = goes_down = False
    digits = [digit for digit in str(number)]

  
    if len(digits) > 2:
        for i in range(len(digits)):
            if i > 0:
                prev = digits[i - 1]
                curr = digits[i]
                if prev < curr:
                    goes_up = True
                if curr < prev:
                    goes_down = True
    return goes_up and goes_down

def bouncy_count(numbers):
    total = 0
    if len(numbers) == 0:
        return total
    for num in numbers:
        if is_bouncy(num):
            total += 1
    return total
'''

'''# Crystal
def is_bouncy(number):
    ascending = descending = False
    digits = [digit for digit in str(number)]

    for left, right in zip(digits, digits[1:]):
        if left < right:
            ascending = True
        elif left > right:
            descending = True

    if ascending and descending:
        return True
    else:
        return False

def bouncy_count(lst):
    count = []
    for number in lst:
        count.append(is_bouncy(number))
    return sum(count)
'''

'''
# Kyle
def bouncy_count(lst):
    count = 0
    for number in lst:
        number = str(number)
        sorted_asc = ''.join(sorted(number))
        sorted_desc = ''.join(sorted(number, reverse=True))
        if number == sorted_asc or number == sorted_desc:
            continue
        else:
            count += 1
    return count

# Python test cases:
print(bouncy_count([]) == 0)
print(bouncy_count([11, 0, 345, 21]) == 0)
print(bouncy_count([121, 4114]) == 2)
print(bouncy_count([176, 442, 80701644]) == 2)
'''