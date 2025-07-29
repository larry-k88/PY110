# Write a function that takes a list of numbers and returns the sum of
# the sums of each leading subsequence in that list. Examine the
# examples to see what we mean. You may assume that the list always
# contains at least one number.

def sum_of_sums(num_list):
    current_total = 0
    temp_nums = []
    for num in num_list:
        current_total += num
        temp_nums.append(current_total)

    return sum(temp_nums)


# [3, 5, 2] --> (3) + (3 + 5) + (3 + 5 + 2) --> 21

# [1, 5, 7, 3] --> (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

# [1, 2, 3, 4, 5] --> (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

# [4] --> 4