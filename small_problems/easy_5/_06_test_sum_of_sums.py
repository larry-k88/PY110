from _06_sum_of_sums import sum_of_sums

def test_sum_of_sums():
    assert sum_of_sums([3, 5, 2]) == 21
    assert sum_of_sums([1, 5, 7, 3]) == 36
    assert sum_of_sums([1, 2, 3, 4, 5]) == 35
    assert sum_of_sums([4]) == 4
