from _10_fibonacci_numbers_location import find_fibonacci_index_by_length

# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
def test_fibonacci_short():
    assert find_fibonacci_index_by_length(2) == 7
    assert find_fibonacci_index_by_length(3) == 12
    assert find_fibonacci_index_by_length(10) == 45
    assert find_fibonacci_index_by_length(16) == 74
    assert find_fibonacci_index_by_length(100) == 476
    assert find_fibonacci_index_by_length(1000) == 4782

def test_fibonacci_long():
    assert find_fibonacci_index_by_length(10000) == 47847
