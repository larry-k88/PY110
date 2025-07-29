# Given a sequence of integers, filter out instances where the same value
# occurs successively, retaining only the initial occurrence. Return the
# refined sequence.

def unique_sequence(sequence):
    unique_nums = [sequence[0]]

    for num in sequence[1:]:
        if num != unique_nums[-1]:
            unique_nums.append(num)

    return unique_nums
